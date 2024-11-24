
module.exports = () => {
  return {
    hooks: {
      'markdown:before': function (markdown) {
        return markdown.replace(/\{([^}]+)\}\{([^}]*)\}/g, (match, text, classes) => {
          const classAttr = classes ? ` class="${classes.trim().replace(/\s+/g, ' ')}"` : '';
          return `<span${classAttr}>${text}</span>`;
        });
      }
    }
  };
};