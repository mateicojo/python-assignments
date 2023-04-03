from Objects import Movie as Movie
from Objects import Client as Client
from Objects import Rental as Rental

class MovieRepo:
    def __init__(self):
        self.__movies=[]
    def __str__(self):
        movies_str=""
        for i in range(len(self.__movies)):
            movies_str+= str(self.__movies[i])+'\n'
        return movies_str
    def __add__(self,movie_id,title,descr,genre):
        for movie in self.__movies:
            if movie_id==movie.movie_id:
                return "ID not unique!"
        new_movie=Movie(movie_id,title,descr,genre)
        self.__movies.append(new_movie)
        return None
    def __del__(self,id):
        for i in range(len(self.__movies)):
            if self.__movies[i].__movie_id==id:
                self.__movies[i].pop()
    @property
    def movies(self):
        return self.__movies
    @movies.setter
    def movies(self,new_movies):
        self.__movies=new_movies



class ClientRepo:
    def __init__(self):
        self.__clients=[]
    def __str__(self):
        client_str=""
        for i in range(len(self.__clients)):
            client_str+= str(self.__clients[i])+'\n'
        return client_str
    def __add__(self,client_id,name):
        for i in range(len(self.__clients)):
            if client_id==self.__clients[i].id:
                return "ID not unique!"
        new_client=Client(client_id,name)
        self.__clients.append(new_client)
    @property
    def clients(self):
        return self.__clients
    @clients.setter
    def clients(self,new_clients):
        self.__clients=new_clients

class RentalRepo:
    def __init__(self):
        self.__rentals=[]
    def __str__(self):
        rental_str=""
        for i in range(len(self.__rentals)):
            rental_str+= str(self.__rentals[i])+'\n'
        return rental_str
    def __add__(self, rental_id,movie_id,client_id,rented_date,due_date,returned_date=None):
        for i in range(len(self.__rentals)):
            if self.__rentals[i]
                return "ID not unique!"
    @property
    def rentals(self):
        return self.__rentals

