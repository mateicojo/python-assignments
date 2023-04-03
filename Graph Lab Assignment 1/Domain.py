from copy import deepcopy
class Graph:
    def __init__(self, n:int):
        self.__vertex=n
        self.__vertexes_in={}
        for i in range(n):
            self.__vertexes_in[i]=[]
        self.__vertexes_out={}
        for i in range(n):
            self.__vertexes_out[i]=[]
        self.__edges={}

    def get_n(self):
        return self.__vertex

    def get_m(self):
        return len(self.__edges)

    def get_edges(self):
        return self.__edges

    def print_vertexes(self):
        print(self.__vertexes_in)
        print(self.__vertexes_out)
        print(self.__edges)

    def count_vertex(self):
        return self.__vertex

    def add_vertex(self,x):
        if x in self.__vertexes_in.keys():
            print("Vertex already exists!")
        self.__vertexes_in[x]=[]
        self.__vertexes_out[x]=[]
        self.__vertex+=1

    def remove_vertex(self, x):
        if x in self.__vertexes_in.keys():
            for i in self.__vertexes_in[x]:
                del self.__edges[(i,x)]
            for i in self.__vertexes_out[x]:
                del self.__edges[(x,i)]
            del self.__vertexes_in[x]
            del self.__vertexes_out[x]
            self.__vertex-=1
        else:
            print("Inexistent vertex!")

    def is_vertex(self,x):
        if x in self.__vertexes_in.keys():
            return True
        else:
            return False

    def add_edge(self, a,b,cost):
        if a in self.__vertexes_in.keys() and b in self.__vertexes_in.keys():
            if (a,b) in self.__edges.keys():
                print("Edge already exists!")
            self.__edges[(a,b)]=cost
            self.__vertexes_in[b].append(a)
            self.__vertexes_out[a].append(b)
        else:
            print("Inexistent vertex!")

    def remove_edge(self,a,b):
        if(a,b) in self.__edges.keys():
            del self.__edges[(a,b)]
            self.__vertexes_in[b].remove(a)
            self.__vertexes_out[a].remove(b)
        else:
            print("ABC")

    def is_edge(self, a, b):
        if (a, b) in self.__edges:
            return True
        else:
            return False

    def set_edge(self, a, b, cost):
        if (a, b) in self.__edges.keys():
            self.__edges[(a, b)] = cost
        else:
            print("Edge does not exist")

    def edge(self, a, b):
        if (a, b) in self.__edges.keys():
            return self.__edges[(a, b)]
        else:
            print("Edge does not exist")

    def copy_graph(self):
        return deepcopy(self)

    def degrees(self, x):
        if x not in self.__vertexes_in.keys():
            raise ValueError("Vertex does not exist")
        return ("Ins: " + str(len(self.__vertexes_in[x])) + " Outs:" + str(len(self.__vertexes_out[x])))

    def parse_vertices(self):
        for x in self.__vertexes_in.keys():
            yield x

    def edge_iterator(l):
        return edgeIterator(l)

    def parse_out_edges(self, x):
        if x not in self.__vertexes_in.keys():
            print("Vertex does not exist")
        outIterator = edgeIterator(self.__vertexes_out[x])
        while True:
            try:
                yield next(outIterator)
            except:
                break

    def parse_in_edges(self, x):
        inIterator = edgeIterator(self.__vertexes_in[x])
        while True:
            try:
                yield next(inIterator)
            except :
                break


class edgeIterator:
    def __init__(self, l):
        self.__vertex_list = l
        self.__i = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i < len(self.__vertex_list) - 1:
            self.__i += 1
            return self.__vertex_list[self.__i]
        else:
            raise ValueError()