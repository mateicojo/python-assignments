from Service import Service
from StudentClass import Student


class Ui:
    def __init__(self):
        self._service = Service()

    def start_app(self):
        '''
        starts the app
        :return:
        '''
        while True:
            self.print_menu()
            self.read_command()

    def print_menu(self):
        print("""------------------------------------------------------------------------------
                1. Add a student.
                2. Display the list of students.
                3. Filter the list so that students in a given group are deleted from the list.
                4. Undo
                0. Exit
------------------------------------------------------------------------------""")

    def read_command(self):
        '''

        :return:
        '''
        command = input("Please enter a command: ")
        if command == "1":
            self._service.add_student(self.read_student())
        elif command == "2":
            self._service.print_students()
        elif command == "3":
            try:
                self._service.filter_students(self.read_group())
            except ValueError:
                print("Invalid group!")
        elif command == "4":
            self._service.undo()
        elif command == "0":
            exit(0)

    def read_student(self):
        """
        Reads a student from the console and returns it
        :return: the student read
        """
        try:
            ident = int(input("Please enter the id: "))
            name = input("Please enter the name: ")
            group = int(input("Please enter the group: "))
            if group < 0:
                raise ValueError("Invalid group!")
            return Student(ident, name, group)
        except ValueError:
            print("Invalid input!")
            return None

    def read_group(self):
        print("Please enter the group to filter out: ")
        return int(input())
