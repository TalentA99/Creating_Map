#Author: Talent Koronya
#Purpose: Asssignment 20 Map part 3
#Date: 16/11/2023


from cs1lib import *

# I used a .join function in order to join the adjacent names with commas

# Here is the link:
#https://www.w3schools.com/python/ref_string_join.asp

VERTEX_RADIUS = 6
EDGE_LINE_WIDTH = 4
class Vertex:
    def __init__(self, name, x, y):

        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj_list = []

    def __str__(self):
        # Convert adjacent vertices to names for string representation
        for i in range(len(self.adj_list)):
            self.adj_list[i] = self.adj_list[i].name

        # Join adjacent names with commas
        adj_names = ", ".join(self.adj_list)

        # Create string representation
        return str(self.name) + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + \
            "Adjacent vertices: " + str(adj_names)

    def draw_vertex(self, r, g, b):
        # Draw a filled circle representing the vertex
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, VERTEX_RADIUS)

    def is_clicked(self, mouse_x, mouse_y):
        if self.x - 5 <= mouse_x <= self.x + 5 and self.y - 5 <= mouse_y <= self.y + 5:
            return True
        else:
            return False
    def draw_edge(self, vertex, r, g, b):
        # Draw a line representing an edge between self and another vertex
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_LINE_WIDTH)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    def draw_all_edges(self, r, g, b):
        # Draw edges between self and all adjacent vertices
        set_stroke_color(r, g, b)
        set_stroke_width(EDGE_LINE_WIDTH)
        for i in self.adj_list:
            self.draw_edge(i, r, g, b)