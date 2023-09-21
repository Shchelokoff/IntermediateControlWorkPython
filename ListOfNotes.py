import pickle
from Note import Note
from View import View


class ListOfNotes:
    notes = []
    view = View()
    index = 0
    indexStack = []

    def __init__(self):
        try:
            with open('notes.pkl', 'rb') as file:
                self.notes = pickle.load(file)
                self.index = len(self.notes)
            with open('indexes.pkl', 'rb') as file:
                self.indexStack = pickle.load(file)
        except EOFError:
            self.notes = []
            self.view = View()
            self.index = 0
            self.indexStack = []

    def addNote(self):
        note = Note()
        note.setName(self.view.inputNoteName())
        note.setText(self.view.inputNoteText())
        note.updateDate()
        if len(self.indexStack) == 0:
            note.setId(self.index)
        else:
            note.setId(self.indexStack.pop())
        self.notes.append(note)
        self.index = len(self.notes)
        self.view.infoNoteMsg('add')

    def deleteNote(self, note):
        self.indexStack.append(note.getId())
        self.notes.remove(note)
        if len(self.notes) == 0:
            self.indexStack.clear()
        self.view.infoNoteMsg('del')


    def readAllNotes(self):
        self.view.showReadAllBanner(len(self.notes))
        for note in self.notes:
            self.view.showNote(note)

    def manageNoteById(self):
        commands =  {1: self.view.showNote,
                     2: self.view.editNote,
                     3: self.deleteNote}
        flag = False
        self.view.showManageNoteMenu()
        choice = self.view.inputNumber(len(commands.keys()), 'menu')
        value = self.view.inputNumber(self.index, 'id')
        for note in self.notes:
            if note.getId() == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.view.notFound()

    def saveNotesToFile(self):
        with open('notes.pkl', 'wb') as file:
            pickle.dump(self.notes, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes.pkl', 'wb') as file:
            pickle.dump(self.indexStack, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.view.savedInfo()



