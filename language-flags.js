// Mintlify loads root-level custom JS after hydration. Keep React-owned
// language labels and navigation intact; only annotate the trigger for CSS.
(() => {
  const languages = new Map([
    ['简体中文', 'cn'],
    ['中文', 'cn'],
    ['English', 'en'],
    ['日本語', 'jp'],
    ['Русский', 'ru'],
    ['한국어', 'ko'],
  ]);
  const selector = '[data-component-part="localization-select-trigger"]';
  let scheduled = false;

  function updateFlags() {
    scheduled = false;
    document.querySelectorAll(selector).forEach((trigger) => {
      const language = languages.get(trigger.textContent.trim());
      if (language) {
        trigger.setAttribute('data-docs-flag', language);
      } else {
        trigger.removeAttribute('data-docs-flag');
      }
    });
  }

  // Language changes and the mobile navigation can replace the trigger.
  // Attribute changes are excluded so our own updates never retrigger this.
  new MutationObserver(() => {
    if (scheduled) return;
    scheduled = true;
    requestAnimationFrame(updateFlags);
  }).observe(document.body, { childList: true, characterData: true, subtree: true });
  updateFlags();
})();
