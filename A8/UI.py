from Services import Services as Services

class UI:
    def __init__(self, services:Services):
        self.service=services
    def print_menu(self):
        print("""
        1.  Add Movie
        2.  Update Movie
        3.  Remove Movie
        4.  List Movies
        
        5.  Add Client
        6.  Update Client
        7.  Remove Client
        8.  List Clients
        
        9.  Rent Movie
        10. Return Movie
        
        11. Search for a Movie
        12. Search for a Client
        
        13. Most rented Movies
        14. Most active Clients
        15. Late Rentals
        
        0.  Exit""")

    def user_input(self):
        ans=input(">")
        return ans

    def exec_command(self,command):
        try:
            match command:
                case "1":
                    movie_id = input("Enter movie ID")
                    title = input("Enter movie title")
                    descr = input("Enter movie description")
                    genre = input("Enter movie genre")
                    self.service.add_movie(movie_id, title, descr, genre)
                case "2":
                    movie_id = input("Enter movie ID to update")
                    new_title = input("Enter new movie title")
                    new_descr = input("Enter new description")
                    new_genre = input("Enter new genre")
                    self.service.update_movie(movie_id, new_title, new_descr, new_genre)
                case "3":
                    movie_id=input("Enter the movie ID to remove")
                    self.service.remove_movie(movie_id)
                case "4":
                    self.service.list_movies()
                case "5":
                    client_id=input("Enter new client ID")
                    client_name=input("Enter new client name")
                    self.service.add_movie(client_id,client_name)
                case "6":
                    client_id = input("Enter client ID to update")
                    new_name = input("Enter new client name")
                    self.service.update_client(id,new_name)
                case "7":
                    client_id = input("Enter the client ID to remove")
                    self.service.remove_client(client_id)
                case "8":
                    self.service.list_clients()
                case "9":
                   movie_id=input("Enter the id of the movie to rent")

                case "10":
                    pass
                case "11":
                    pass
                case "12":
                    pass
                case "13":
                    pass
                case "14":
                    pass
                case "15":
                    pass
                case "0":
                    quit()
                case default:
                    raise ValueError
        except ValueError:
            print("Invalid Command!")

    def start_app(self):
        while True:
            self.print_menu()
            command = self.user_input()
            self.exec_command(command)





