from StudentClass import Student
from copy import deepcopy
from random import randint

names = ["Alex","Stefan","Marius","Andreea","Daria","Andreea","Ambra","Andra","Daria"]
surnames = ["George","Iordache","Constantin","Stefania","Antal","Stefanescu","Pirvu","Enache","Ivancov"]

class MemoryRepo:
    def __init__(self):
        self._students = []
        self._undos = []
        self.generate_students(10)

    def add(self, stud: Student):
        """
        Adds a student to the repository
        :param stud: the student to be added
        """
        if stud is None:
            return
        if self.bad_id(stud.ident):
            print("Student ID already exists!")
            return
        self._undos.append(deepcopy(self._students))
        self._students.append(stud)

    def get_all(self):
        '''

        :return:
        '''
        return self._students

    def print_all(self):
        '''

        :return:
        '''
        for x in self._students:
            print(str(x))

    def filter(self, group):
        '''
        Filters the students by a certain group
        :param group:
        :return:
        '''
        self._undos.append(deepcopy(self._students))
        self._students = [x for x in self._students if x.group != group]

    def undo(self):
        '''
        Undos the last command
        :return:
        '''
        if len(self._undos) == 0:
            return
        self._students = self._undos.pop()

    def generate_students(self, n):
        '''
        Generates n students with random credentials
        :param n:
        :return:
        '''
        for i in range(n):
            ident = randint(0, 100000)
            while self.bad_id(ident):
                ident = randint(0, 100000)
                print(str(ident))
            name = f"{surnames[randint(0, len(surnames) - 1)]} {names[randint(0, len(names) - 1)]}"
            group = randint(1, 5)
            self.add(Student(ident, name, group))

    def bad_id(self, ident):

        for x in self._students:
            if x.ident == ident:
                return True
        return False

    def save_changes(self):
        pass

    def close(self):
        exit()
