document.addEventListener("DOMContentLoaded", function() {
    const editLinks = document.querySelectorAll('a[href*="/_edit/"]');
    editLinks.forEach(link => {
        let href = link.getAttribute('href');
        href = href.replace('/_edit/', '/');
        href = href.replace('.md', '/_edit')
        link.setAttribute('href', href);
    });
});
