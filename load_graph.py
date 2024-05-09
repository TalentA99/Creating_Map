#Author: Talent Koronya
#Purpose: Asssignment 20 Map part 3
#Date: 15/11/2023
from vertex import Vertex
def create_vertex_dictionary(file):
    f1 = open(file, "r")
    vertex_dictionary = {}


    for line in f1:
        # Remove leading/trailing whitespaces and split the line by semicolon
        s = line.strip()
        p = s.split(";")

        # Extract vertex name
        name = p[0].strip()

        # Extract x and y coordinates, converting them to integers
        x, y = p[2].split(",")

        place = Vertex(name, x, y)

        vertex_dictionary[name] = place

    f1.close()
    # Open the file again for the second pass
    f1 = open(file, "r")

    # Second pass: Establish adjacency lists
    for line in f1:
        # Remove leading/trailing whitespaces and split the line by semicolon
        s = line.strip()
        p = s.split(";")
        name = p[0].strip()
        adj = p[1].split(",")

        # Establish adjacency list for the current vertex
        for i in adj:
            vertex_dictionary[name].adj_list.append(vertex_dictionary[i.strip()])

    # Return the populated vertex dictionary
    return vertex_dictionary


dict1 = create_vertex_dictionary("dartmouth_graph.txt")
