import pickle
from StudentClass import Student
from copy import deepcopy
from random import randint

names = ["Alex","Stefan","Marius","Andreea","Daria","Andreea","Ambra","Andra","Daria"]
surnames = ["George","Iordache","Constantin","Stefania","Antal","Stefanescu","Pirvu","Enache","Ivancov"]


class BinaryRepo:

    def __init__(self):
        self._students = []
        self._undos = []
        self._file = open("students.pickle", "rb+")
        try:
            while True:
                self._students = pickle.load(self._file)
        except EOFError:
            print("Students loaded!")
        if not self._students:
            pickle.dump(self._students, self._file)

    def add(self, stud: Student):
        """
        Adds a student to the repository
        :param stud: the student to be added
        :return: nothing
        """
        if stud is None:
            return
        if self.bad_id(stud.ident):
            print("Student ID already exists!")
            return
        self._undos.append(deepcopy(self._students))
        self._students.append(stud)
        self.save_changes()

    def get_all(self):
        return self._students

    def print_all(self):
        for x in self._students:
            print(str(x))

    def filter(self, group):
        self._undos.append(deepcopy(self._students))
        self._students = [x for x in self._students if x.group != group]
        self.save_changes()

    def undo(self):
        if len(self._undos) == 0:
            return
        self._students = self._undos.pop()
        self.save_changes()

    def save_changes(self):
        self._file.close()
        pickle.dump(self._students, open("students.pickle", "wb+"))
        self._file = open("students.pickle", "rb+")
        pickle.dump(self._students, self._file)

    def generate_students(self, n):
        rez = []
        for i in range(n):
            ident = randint(0, 100000)
            while self.bad_id(ident):
                ident = randint(0, 100000)
                print(str(ident))
            name = f"{surnames[randint(0, len(surnames) - 1)]} {names[randint(0, len(names) - 1)]}"
            group = randint(1, 5)
            rez.append(Student(ident, name, group))
        return rez

    def bad_id(self, ident):
        for x in self._students:
            if x.ident == ident:
                return True
        return False

    def close(self):
        self._file.close()
        exit()
