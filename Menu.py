from ListOfNotes import ListOfNotes
from View import View


class Menu:
    view = View()
    notes = ListOfNotes()
    commands = {1: notes.addNote, 2: notes.manageNoteById, 3: notes.readAllNotes,
                  4: notes.saveNotesToFile}

    def start(self):
        self.view.greeting()
        while(True):
            self.view.showMainMenu()
            choice = self.view.inputNumber(len(self.commands.keys()), 'menu')
            if choice == 0:
                self.view.exitMsg()
                break
            else:
                self.commands[choice]()