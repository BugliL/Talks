
module.exports = (markdown) => {
    // Regex to remove everything between <!-- hidden-start --> and <!-- hidden-end -->
    return markdown.replace(/<!-- hidden-start -->[\s\S]*?<!-- hidden-end -->/g, '');
};