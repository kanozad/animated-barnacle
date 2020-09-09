const fs = require('fs');
const chalk = require('chalk');

const NOTES_FILE = 'notes.json';

const addNote = (title, body) => {
    const notes = loadNotes();
    //const duplicateNotes = notes.filter((note) => note.title === title);
    const duplicateNote = notes.find((note) => note.title === title);

    if (!duplicateNote) {
        notes.push({
            title: title,
            body: body,
        });

        saveNotes(notes);

        console.log(chalk.green.inverse("New note '" + title + "' added."));
    } else {
        console.log(chalk.red.inverse("Note '" + title + "' already exists!"));
    }
}

const removeNote = (title) => {
    const notes = loadNotes();
    const keepNotes = notes.filter((note) => title !== note.title);

    if (notes.length === keepNotes.length) {
        console.log(chalk.red.inverse("Note '" + title + "' not found!"));
    } else {
        saveNotes(keepNotes);
        console.log(chalk.green.inverse("Note '" + title + "' removed!"));
    }
}

const listNotes = () => {
    console.log(chalk.blue.inverse("Your notes:"));
    loadNotes().forEach((note) => {
        console.log(chalk.blue('*'), chalk.blue(note.title));
    });
}

const readNote = (title) => {
    const note = loadNotes().find((note) => note.title === title);
    if(note) {
        console.log(chalk.blue(note.title));
        console.log(note.body);
    } else {
        console.log(chalk.red.inverse("Note '" + title + "' not found"));
    }
}

const saveNotes = (notes) => {
    const dataJSON = JSON.stringify(notes);
    fs.writeFileSync(NOTES_FILE, dataJSON);
}


const loadNotes = () => {
    try {
        const dataBuffer = fs.readFileSync(NOTES_FILE);
        const dataJson = dataBuffer.toString();
        return JSON.parse(dataJson);
    } catch (e) {
        return [];
    }
}



module.exports = {
    addNote: addNote,
    removeNote: removeNote,
    listNotes: listNotes,
    readNote: readNote,
}
