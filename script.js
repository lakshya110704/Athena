function addLink() {
    var linkContainer = document.getElementById('linkContainer');
    var newLink = document.createElement('a');
    newLink.href = 'https://v2.tailwindcss.com/docs';
    newLink.textContent = 'New Link';
    linkContainer.appendChild(newLink);
}