class Student:
    def __init__(self, ident, name, group):
        self.ident = ident
        self.name = name
        self.group = group

    @property
    def ident(self):
        return self._ident

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @ident.setter
    def ident(self, ident):
        self._ident = ident

    @name.setter
    def name(self, name):
        self._name = name

    @group.setter
    def group(self, group):
        self._group = group

    def print_nice(self):
        return f"{self.ident} {self.name} {self.group}"

    def __str__(self):
        return self.print_nice()



    def from_list(self, lst):
        self.ident = lst[0]
        self.name = lst[1]
        self.group = lst[2]
        return self


