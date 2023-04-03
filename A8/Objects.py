class Movie:
    def __init__(self,movie_id,title,descr,genre):
        self.__movie_id=movie_id
        self.__title=title
        self.__descr=descr
        self.__genre=genre

    def __str__(self):
        return f"{self.__movie_id} | {self.__title} | {self.__descr} | {self.__genre}"
    @property
    def movie_id(self):
        return self.__movie_id
    @property
    def title(self):
        return self.__title
    @property
    def descr(self):
        return self.__descr
    @property
    def genre(self):
        return self.__genre
    @title.setter
    def title(self,new):
        self.__title=new
    @descr.setter
    def descr(self,new):
        self.__descr=new
    @genre.setter
    def genre(self,new):
        self.__genre=new



class Client:
    def __init__(self,client_id,name):
        self.__client_id=client_id
        self.__name=name
    def __str__(self):
        return f"{self.__client_id} | {self.__name}"
    @property
    def id(self):
        return self.__client_id
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new):
        self.__name=new




class Rental:
    def __init__(self,rental_id,movie_id,client_id,rented_date,due_date,returned_date=None):
        self.__rental_id=rental_id
        self.__movie_id=movie_id
        self.__client_id=client_id
        self.__rented_date=rented_date
        self.__due_date=due_date
        self.__returned_date=returned_date
    def __str__(self):
        return f"{self.__rental_id} | {self.__movie_id} | {self.__client_id} | {self.__rented_date} | {self.__due_date} | {self.__returned_date}"
    @property
    def rental_id(self):
        return self.__rental_id
    @property
    def movie_id(self):
        return self.__movie_id
    @property
    def client_id(self):
        return self.__client_id
    @property
    def rented_date(self):
        return self.__rented_date
    @property
    def due_date(self):
        return self.__due_date
    @property
    def returned_date(self):
        return self.__returned_date

