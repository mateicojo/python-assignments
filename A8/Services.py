from Objects import Movie as Movie
from Objects import Client as Client
from Objects import Rental as Rental
from Repos import MovieRepo as MovieRepo
from Repos import ClientRepo as ClientRepo
from Repos import RentalRepo as RentalRepo
clientrepo=ClientRepo()
clientrepo.__add__(1,"Alex Popescu")
clientrepo.__add__(2,"Stefan Iordache")
clientrepo.__add__(3,"Stefania Borza")
clientrepo.__add__(4,"Marius Asac")
clientrepo.__add__(5,"Andreea Isopescu")
movierepo=MovieRepo()
movierepo.__add__(1,"Intersterllar","abc","action")
movierepo.__add__(2,"Matrix","abcde","action")
movierepo.__add__(3,"Rocknrolla","","comedy")
movierepo.__add__(4,"Avatar","","fantasy")
movierepo.__add__(5,"Avatar 2", "", "fantasy")
rentalrepo= RentalRepo()

class Services:
    def __init__(self,movierepo,clientrepo,rentalrepo):
        self.__movierepo=movierepo
        self.__clientrepo=clientrepo
        self.__rentalrepo=rentalrepo
    def add_movie(self,movie_id,title,descr,genre):
        '''
        adds a movie to the movierepo
        :param movie_id:
        :param title:
        :param descr:
        :param genre:
        :return:
        '''
        movierepo.__add__(movie_id,title,descr,genre)
    def update_movie(self,movie_id,new_title,new_descr,new_genre):
        '''
        updates a movie with a given ID
        :param movie_id:
        :param new_title:
        :param new_descr:
        :param new_genre:
        :return:
        '''
        new_movies=movierepo.movies
        for movie in new_movies:
            if movie.movie_id==movie_id:
                movie.title=new_title
                movie.descr=new_descr
                movie.genre=new_genre
        movierepo.movies=new_movies
    def list_movies(self):
        '''
        lists existing movies
        :return:
        '''
        print(movierepo)
    def remove_movie(self,id):
        '''
        removes a movie with a given ID
        :param id:
        :return:
        '''
        new_movies=movierepo.movies
        for i in range(len(movierepo.movies)):
            if new_movies[i].movie_id==id:
                new_movies.pop(i)
        movierepo.movies=new_movies
    def add_client(self,id,name):
        '''
        adds a client to the clientrepo
        :param id:
        :param name:
        :return:
        '''
        clientrepo.__add__(id,name)
    def update_client(self,id,new_name):
        '''
        updates a client with a fiven ID
        :param id:
        :param new_name:
        :return:
        '''
        for client in clientrepo:
            if client.id==id:
                client.name=new_name
    def remove_client(self,id):
        new_clients=clientrepo.clients
        for i in range(len(clientrepo.clients)):
            if new_clients[i].id==id:
                new_clients.pop(i)
        clientrepo.clients=new_clients
    def list_clients(self):
        print(clientrepo)

ser = Services(movierepo,clientrepo,rentalrepo)