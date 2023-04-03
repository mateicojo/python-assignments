from MemoryRepo import MemoryRepo as MemoryRepository
from TextFileRepo import TextRepo as TextFileRepository
#from BinaryFileRepository import BinaryRepo as BinaryFileRepository
from StudentClass import Student


class Service:
    def __init__(self):
        self._repo = self.get_repo()

    def get_repo(self):
        repofile = open("settings.properties", "r")
        repo = repofile.readline().split("=")[1]
        repofile.close()
        if repo == "memory":
            return MemoryRepository()
        elif repo == "text":
            return TextFileRepository()
        elif repo == "pickle":
            return MemoryRepository()

    def add_student(self, student):
        """
        Adds a student to the repository depending on the repository in use
        :param student: the student to be added
        :return: nothing
        """
        self._repo.add(student)

    def get_students(self):
        return self._repo.get_all()

    def print_students(self):
        self._repo.print_all()

    def filter_students(self, group):
        self._repo.filter(group)

    def undo(self):
        self._repo.undo()

    def generate_students(self, n):
        self._repo.generate_students(n)

    def close(self):
        self._repo.close()

#TEST
def test_add():
    try:
        service = Service()
        initial_len = len(service.get_students())

        assert len(service._repo.get_all()) == initial_len
        service.add_student(Student(12444, "Ionut Zapada", 1))
        assert service._repo.get_all()[-1].name == "Ionut Zapada"
        service.add_student(Student(33532, "Maria Dragon", 3))
        assert len(service._repo.get_all()) == initial_len + 2
        service.add_student(Student(434433, "Petru Calamar", 4))
        service.filter_students(4)
    except:
        print("0")

test_add()