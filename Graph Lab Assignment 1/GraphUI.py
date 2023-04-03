from Domain import Graph
import random

def read_graph(filename):
    file = open(filename, "r")
    sizes = file.readline().split(" ")
    n = int(sizes[0])
    m = int(sizes[1])
    g = Graph(n)
    for i in range(m):
        line = file.readline().split(" ")
        x = int(line[0])
        y = int(line[1])
        e = int(line[2].split("\\")[0])
        g.add_edge(x, y, e)
    file.close()
    return g

def copy_graph(g):
    write_graph(g,"GraphCopy.txt")

def write_graph(g, filename):
    file = open(filename, "w")
    file.write(str(g.get_n()) + " " + str(g.get_m()) + "\n")
    edges = g.get_edges()
    for edge in edges.keys():
        file.write(str(edge[0]) + " " + str(edge[1]) + " " + str(edges[edge]) + "\n")
    file.close()

def generate_graph(n, m):
    g = Graph(n)
    while m > 0:
        x = random.randint(0, n - 1)
        y = random.randint(0, n - 1)
        e = random.randint(0, 100)
        if not g.is_edge(x, y):
            g.add_edge(x, y, e)
            m -= 1
    return g

def menu():
    print("1. Get number of vertices")
    print("2. Parse vertices")
    print("3. Check if edge exists")
    print("4. Get vertex degrees")
    print("5. Parse out edges")
    print("6. Parse in edges")
    print("7. Get edge info")
    print("8. Change edge info")
    print("9. Add edge")
    print("10. Remove edge")
    print("11. Add vertex")
    print("12. Remove vertex")
    print("13. Copy the graph")
    print("14. Read a graph from a file")
    print("15. Write a graph to a file")
    print("16. Generate a random graph")
    print("18. Print graph")
    print("0. Exit")


g = read_graph("MyGraph.txt")
copy = g.copy_graph()
print(g.print_vertexes())
while True:
    menu()
    command = -1
    try:
        command = int(input(">: "))
    except:
        pass
    match command:
        case 1:
            print(g.count_vertex())
        case 2:
            for v in g.parse_vertices():
                print(v, end=" ")
            print()
        case 3:
            try:
                x = int(input("Enter 1st end: "))
                y = int(input("Enter 2nd end: "))
                print(g.is_edge(x,y))
            except:
                print("Invalid input")
        case 4:
            try:
                x = int(input("Enter vertex: "))
                print(g.degrees(x))
            except:
                print("Invalid vertex")
        case 5:
            try:
                x = int(input("Enter vertex: "))
                for e in g.parse_out_edges(x):
                    print(e, end=" ")
                print()
            except:
                print("Invalid vertex")
        case 6:
            try:
                x = int(input("Enter vertex: "))
                for e in g.parse_in_edges(x):
                    print(e, end=" ")
                print()
            except:
                pass
        case 7:
            try:
                x = int(input("Enter 1st end: "))
                y = int(input("Enter 2nd end: "))
                print("The edge has cost: " + str(g.edge(x, y)))
            except:
                pass
        case 8:
            try:
                x = int(input("Enter 1st end: "))
                y = int(input("Enter 2nd end: "))
                e = int(input("Enter cost: "))
                g.set_edge(x, y, e)
            except:
                print("Invalid edge")
        case 9:
            try:
                x = int(input("Enter 1st end: "))
                y = int(input("Enter 2nd end: "))
                e = int(input("Enter cost: "))
                g.add_edge(x, y, e)
            except:
                print("Invalid edge")
        case 10:
            try:
                x = int(input("Enter 1st end: "))
                y = int(input("Enter 2nd end: "))
                g.remove_edge(x, y)
            except:
                print("Invalid edge")
        case 11:
            try:
                x = int(input("Enter vertex: "))
                g.add_vertex(x)
            except:
                print("Invalid vertex")
        case 12:
            try:
                x = int(input("Enter vertex: "))
                g.remove_vertex(x)
            except:
                print("Invalid vertex")
        case 13:
            copy=copy_graph(g)
            write_graph(copy,"GraphCopy.txt")
        case 14:
            filename = input("Enter filename: ")
            try:
                g = read_graph(filename)
            except:
                print("Invalid filename")
        case 15:
            filename = input("Enter filename: ")
            write_graph(g, filename)
        case 16:
            try:
                n = int(input("Enter n: "))
                m = int(input("Enter m: "))
                g = generate_graph(n, m)
            except:
                print("Invalid input")
        case 17:
            copy=g
            g=read_graph("GraphCopy.txt")
        case 18:
            g.print_vertexes()
        case 0:
            break
