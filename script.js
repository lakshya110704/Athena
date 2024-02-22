<<<<<<< HEAD
function addLink() {
    var linkContainer = document.getElementById('linkContainer');
    var newLink = document.createElement('a');
    newLink.href = 'https://v2.tailwindcss.com/docs';
    newLink.textContent = 'New Link';
    linkContainer.appendChild(newLink);
}
=======
function saveNote() {
    var noteInput = document.getElementById('noteInput');
    var noteText = noteInput.value.trim();

    if (noteText !== '') {
        var noteElement = document.createElement('div');
        noteElement.classList.add('note');
        noteElement.textContent = noteText;

        var notesContainer = document.getElementById('notesContainer');
        notesContainer.appendChild(noteElement);

        noteInput.value = '';

        // Save the note to Local Storage
        var notes = JSON.parse(localStorage.getItem('notes')) || [];
        notes.push(noteText);
        localStorage.setItem('notes', JSON.stringify(notes));
    }
}

function loadNotes() {
    var notes = JSON.parse(localStorage.getItem('notes')) || [];
    var notesContainer = document.getElementById('notesContainer');
    notesContainer.innerHTML = '';

    notes.forEach(note => {
        var noteElement = document.createElement('div');
        noteElement.classList.add('note');
        noteElement.textContent = note;
        notesContainer.appendChild(noteElement);
    });
}

loadNotes();
>>>>>>> refs/remotes/origin/main
