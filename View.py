class View:
    def greeting(self):
        print("Вас приветствует приложение для управления личными заметками!")

    def showMainMenu(self):
        print("Что вы хотите сделать? Выберите пункт меню:\n"
              "\t1. Добавить заметку\n"
              "\t2. Прочитать/Изменить/Удалить заметку\n"
              "\t3. Показать список всех заметок\n"
              "\t4. Сохранить заметки\n"
              "\t0. Выйти из приложения")

    def showManageNoteMenu(self):
        print("Что вы хотите сделать? Выберите пункт меню:\n"
              "\t1. Прочитать заметку\n"
              "\t2. Изменить заметку\n"
              "\t3. Удалить заметку\n")

    def error(self):
        print("!!! Введите корректное число")
    def notFound(self):
        print("Такого значения не найдено. Попробуйте еще раз.")

    def savedInfo(self):
        print("Заметки сохранены в файл!")

    def showNote(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_text())}\n"
        print(result)

    def showReadAllBanner(self, count):
        result = f"\t***Все заметки***\n" \
                 f"Найдено заметок: {count}\n"
        print(result)

    def infoNoteMsg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def inputNoteName(self):
        return input(f"Введите название заметки:")

    def inputNoteText(self):
        return input(f"Текст заметки:")

    def editNote(self, note):
        note.setText(self.inputNoteText())
        note.updateDate()
        self.infoNoteMsg('edit')

    def inputNumber(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.notFound()
        return value

    def exitMsg(self):
        print("Всего хорошего!")