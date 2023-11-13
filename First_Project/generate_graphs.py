import random
import math
import json

random.seed(98359)

def generate_vertices(n_vertices):
    
    vertices = []

    min_distance_between_vertices = 7                                       #This value was defined as an educated guess for 2 points not to be "too close"
    
    while len(vertices) < n_vertices:
        vertex = (random.randint(1, 100),random.randint(1, 100))           #graph vertices are 2D points on the XOY plane, with integer valued coordinates between 1 and 100

        can_add_vertex = True

        if vertex not in vertices:                                         #Vertices cannot coincide with each other
            for v in vertices:
                if math.dist(v,vertex) < min_distance_between_vertices:    #Distance from each vertice has to be bigger than the minimum value (For example points (10,10) and (15,15))
                    can_add_vertex = False
                    break
            if can_add_vertex:
                vertices.append(vertex)

    return {i:vertices[i] for i in range(len(vertices))}                    #Return dictionary where keys are vertice IDs and values are vertice coordinates

 
def generate_graph(n_vertices,edge_percentage):

    vertices = generate_vertices(n_vertices)

    print(f"{vertices=}")

    max_n_edges = (n_vertices * (n_vertices - 1)) / 2                       #Max number of edges

    print(f"{max_n_edges=}")

    n_edges = int(max_n_edges * edge_percentage)                            #Usable number of edges using the percentage of the maximum number of edges

    print(f"{n_edges=}")

    edges = []
    counter = 0

    while counter < n_edges:
        u = random.randint(0, n_vertices-1)
        v = random.randint(0, n_vertices-1)
        if u != v and (u,v) not in edges and (v,u) not in edges:            #If the vertices are not the same and the edge does not exist
            edges.append((u,v))
            counter += 1

    return vertices, edges

if __name__ == '__main__':

    edge_percentage_list = [0.125, 0.25, 0.5, 0.75]
    n_vertices_list = range(4,151)

    for n_vertices in n_vertices_list:
        for edge_percentage in edge_percentage_list:
            vertices, edges = generate_graph(n_vertices, edge_percentage)
            graph = {"vertices": vertices, "edges":edges}
            with open("graphs/{}_vertices_{}_edge_percentage.json".format(n_vertices,edge_percentage), "w") as f:
                f.write(json.dumps(graph))