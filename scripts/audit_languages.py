"""Offline locale coverage, navigation, links and technical-content audit.

Compare each route to its newest recorded content revision in alignment-sources.json,
falling back to Chinese when no provenance manifest exists. Localization mappings
normalize human-readable inline labels, while runnable code remains protected.

Run: python scripts/audit_languages.py [--output reports/language-alignment.json]
Technical differences are review candidates, not proof of a mistranslation.
"""
import argparse
import collections
import json
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = ('en', 'jp', 'ru', 'ko', 'es')
FENCE = r'^[ \t]*```[^\n]*\n.*?^[ \t]*```[ \t]*$'
SPANISH_GLOSSARY = json.loads((ROOT / 'scripts/spanish-inline-glossary.json').read_text(encoding='utf-8'))

def pages(locale):
    root = ROOT if locale == 'cn' else ROOT / locale
    return {p.relative_to(root).with_suffix('').as_posix(): p for p in root.rglob('*.mdx')
            if locale != 'cn' or p.relative_to(root).parts[0] not in LOCALES}

def routes(node):
    result = []
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'pages':
                result += [s for s in v if isinstance(s, str)]
            result += routes(v)
    elif isinstance(node, list):
        for v in node:
            result += routes(v)
    return result

def normalize(route):
    return re.sub(r'^(?:en|jp|ru|ko|es)/', '', route)

def technical(text):
    # Inline literals retain parameter names, models, numbers and API paths.
    literals = set(re.findall(r'(?<!`)`([^`\n]+)`(?!`)', text))
    # Natural-language inline labels are excluded from this machine comparison.
    literals = {v for v in literals if re.fullmatch(r'[A-Za-z0-9_./:{}*+?=&%\-]+', v)}
    endpoints = set(re.findall(r'\b(?:GET|POST|PUT|PATCH|DELETE)\s+(/[A-Za-z0-9_./:{}?=&%\-]+)', text))
    # Model IDs and base URLs inside runnable examples can drift even if prose matches.
    for key, value in re.findall(r'["\'](model|model_name|base_url|baseURL)["\']\s*:\s*["\']([^"\']+)["\']', text):
        literals.add(key + '=' + value)
    for key, value in re.findall(r'\b(model|base_url|baseURL)\s*=\s*["\']([^"\']+)["\']', text):
        literals.add(key + '=' + value)
    return literals, endpoints

def content_integrity(source, translation, mapping, language):
    def norm(text):
        return re.sub(r'https://docs\.crazyrouter\.com/(?:en|jp|ru|ko|es)/', 'https://docs.crazyrouter.com/', text)
    def blocks(text):
        return [norm(block) for block in re.findall(FENCE, text, re.S | re.M)]
    def prose(text):
        return re.sub(FENCE, '', text, flags=re.S | re.M)
    def structure(text):
        text = prose(text)
        return (re.findall(r'^#{1,6} ', text, re.M), re.findall(r'</?([A-Z][A-Za-z]+)\b', text),
                len(re.findall(r'^\s*\|.*\|\s*$', text, re.M)))
    def inline(text, translate=False):
        return collections.Counter(norm(html.unescape(mapping.get(value, value) if translate else value)) for value in re.findall(r'`([^`\n]+)`', prose(text)))
    issues = []
    if blocks(source) != blocks(translation):
        issues.append('code_blocks_differ')
    if structure(source) != structure(translation):
        issues.append('headings_components_or_tables_differ')
    if inline(source, True) != inline(translation):
        issues.append('inline_literals_differ')
    clean = re.sub(r'\{/\*.*?\*/\}', '', prose(translation), flags=re.S)
    if language in ('es', 'en', 'ru', 'ko') and re.search(r'[\u4e00-\u9fff]', clean):
        issues.append('untranslated_chinese_prose')
    return issues

def audit():
    config = json.loads((ROOT / 'docs.json').read_text(encoding='utf-8'))
    baseline = pages('cn')
    navbase = routes(config['navigation']['languages'][0])
    source_file = ROOT / 'reports/alignment-sources.json'
    sources = {e['page']: e for e in json.loads(source_file.read_text(encoding='utf-8'))['pages']} if source_file.exists() else {}
    state_file = ROOT / 'reports/alignment-state.json'
    state = json.loads(state_file.read_text(encoding='utf-8'))['translations'] if state_file.exists() else {}
    result = {'baseline': 'newest substantive content revision per page' if sources else 'cn', 'baseline_pages': len(baseline), 'locales': {},
              'missing_languages': sorted({'cn', *LOCALES} - {l['language'] for l in config['navigation']['languages']}),
              'broken_links': [], 'cross_locale_links': [], 'language_review': [], 'technical_review': [], 'spanish_integrity': [], 'localized_integrity': [], 'content_date_mismatches': [],
              'limitations': 'Static checks do not establish semantic equivalence. Technical differences require review; code examples may intentionally differ.'}
    for entry in config['navigation']['languages']:
        lang = entry['language']
        files = pages(lang)
        nav = routes(entry)
        normal = [normalize(r) for r in nav]
        result['locales'][lang] = {'pages': len(files), 'missing_pages': sorted(baseline.keys() - files.keys()),
            'extra_pages': sorted(files.keys() - baseline.keys()),
            'missing_navigation': sorted(set(navbase) - set(normal)),
            'extra_navigation': sorted(set(normal) - set(navbase)),
            'navigation_order_matches': normal == navbase,
            'broken_navigation': [r for r in nav if not (ROOT / (r + '.mdx')).exists()],
            'unlisted_pages': sorted(files.keys() - set(normal))}
        for route, file in files.items():
            text = file.read_text(encoding='utf-8')
            prose = re.sub(FENCE, '', text, flags=re.S | re.M)
            if lang in ('jp', 'ru', 'ko'):
                body = re.sub(r'^---\n.*?\n---\n|<[^>]+>|`[^`]+`|https?://\S+', '', prose, flags=re.S)
                body = re.sub(r'^>[^\n]*20\d\d[^\n]*', '', body, flags=re.M)
                body = re.split(r'\{/\* crazyrouter-model-links', body)[0]
                native = {'jp': r'[\u3040-\u30ff\u4e00-\u9fff]', 'ru': r'[\u0400-\u04ff]', 'ko': r'[\uac00-\ud7af]'}[lang]
                native_count = len(re.findall(native, body))
                if native_count < 20 and len(re.findall(r'[A-Za-z]', body)) > 200:
                    result['language_review'].append({'language': lang, 'page': route, 'native_characters': native_count,
                        'reason': 'Very little target-language prose; possible untranslated English fallback.'})
            for link in re.findall(r'(?:\]\(|href=["\'])(/[^\s)"\']+)', prose):
                target = link.split('#')[0].split('?')[0].rstrip('/')
                if target and not (ROOT / (target.lstrip('/') + '.mdx')).exists() and not (ROOT / target.lstrip('/')).exists():
                    result['broken_links'].append({'file': file.relative_to(ROOT).as_posix(), 'target': link})
                canonical = normalize(target.lstrip('/'))
                expected = '/' + ('' if lang == 'cn' else lang + '/') + canonical
                if canonical in baseline and target != expected:
                    result['cross_locale_links'].append({'file': file.relative_to(ROOT).as_posix(), 'target': link, 'expected': expected})
            source_entry = sources.get(route)
            source_language = source_entry['selected_language'] if source_entry else 'cn'
            relative = file.relative_to(ROOT).as_posix()
            record = state.get(relative)
            if source_entry:
                expected_date = source_entry['source_timestamp'][:10]
                actual_date = re.search(r'^>[^\n]*(20\d\d-\d\d-\d\d)', text, re.M)
                if not actual_date or actual_date[1] != expected_date:
                    result['content_date_mismatches'].append({'file': relative, 'expected': expected_date})
            if lang != source_language and route in baseline:
                source_path = ROOT / source_entry['source_path'] if source_entry else baseline[route]
                src = source_path.read_text(encoding='utf-8')
                mapping = record['inline_translations'] if record else (SPANISH_GLOSSARY if lang == 'es' else {})
                if lang == 'es' or record:
                    issues = content_integrity(src, text, mapping, lang)
                    if issues:
                        result['localized_integrity'].append({'language': lang, 'page': route, 'issues': issues})
                        if lang == 'es':
                            result['spanish_integrity'].append({'page': route, 'issues': issues})
                technical_source = src
                if mapping:
                    technical_source = re.sub(r'`([^`\n]+)`', lambda m: '`' + html.unescape(mapping.get(m[1], m[1])) + '`', src)
                a, ae = technical(technical_source)
                b, be = technical(html.unescape(text))
                if a != b or ae != be:
                    result['technical_review'].append({'language': lang, 'page': route, 'source_language': source_language,
                        'missing_literals': sorted(a-b), 'extra_literals': sorted(b-a),
                        'missing_endpoints': sorted(ae-be), 'extra_endpoints': sorted(be-ae)})
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='reports/language-alignment.json')
    parser.add_argument('--strict-content', action='store_true', help='Also fail on technical differences and possible untranslated prose.')
    args = parser.parse_args()
    result = audit()
    out = ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'locales': result['locales'], 'broken_links': len(result['broken_links']),
                      'cross_locale_links': len(result['cross_locale_links']), 'language_review': len(result['language_review']),
                      'technical_review': len(result['technical_review']), 'spanish_integrity': len(result['spanish_integrity']),
                      'localized_integrity': len(result['localized_integrity']), 'content_date_mismatches': len(result['content_date_mismatches'])}, ensure_ascii=False, indent=2))
    failed = bool(result['missing_languages'] or result['broken_links'] or result['cross_locale_links'] or result['localized_integrity'] or result['content_date_mismatches'])
    failed |= any(v['missing_pages'] or v['extra_pages'] or v['broken_navigation'] or v['missing_navigation'] or v['extra_navigation'] or not v['navigation_order_matches'] for v in result['locales'].values())
    if args.strict_content:
        failed |= bool(result['technical_review'] or result['language_review'])
    raise SystemExit(int(failed))
