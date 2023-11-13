import networkx as nx
import matplotlib.pyplot as plt
import json

def draw_graph(vertices, edges, n_vertices, edge_percentage):

    G = create_graph(vertices, edges)

    pos = nx.get_node_attributes(G, 'pos')

    fig, ax = plt.subplots()

    ax.set_xlim(0,100)
    ax.set_ylim(0,100)

    ax.axvline(x=0, color='black', linestyle='--')
    ax.axhline(y=0, color='black', linestyle='--')

    nx.draw(G, pos, with_labels=True,ax=ax, node_size=300)

    plt.title(f"Graph with {n_vertices} vertices and {edge_percentage} edge percentage")

    plt.show()

def draw_graph(G):
    
    pos = nx.get_node_attributes(G, 'pos')

    fig, ax = plt.subplots()

    ax.set_xlim(0,100)
    ax.set_ylim(0,100)

    ax.axvline(x=0, color='black', linestyle='--')
    ax.axhline(y=0, color='black', linestyle='--')

    nx.draw(G, pos, with_labels=True,ax=ax, node_size=300)

    plt.show()

def get_adjacency_matrix(G):
    nx_matrix = nx.adjacency_data(G)
    
    adjancency_matrix = []
    
    for vertex in range(len(nx_matrix['nodes'])):
        adjancency_matrix_row = []
        for vertex2 in range(len(nx_matrix['nodes'])):
            if {'id':str(vertex2)} in nx_matrix['adjacency'][vertex]:
                adjancency_matrix_row.append(1)
            else:
                adjancency_matrix_row.append(0)
        adjancency_matrix.append(adjancency_matrix_row)
    
    return adjancency_matrix

def draw_all_graphs():
    edge_percentage_list = [0.125, 0.25, 0.5, 0.75]
    n_vertices_list = range(4,21)

    for n_vertices in n_vertices_list:
        for edge_percentage in edge_percentage_list:
            with open("graphs/{}_vertices_{}_edge_percentage.json".format(n_vertices,edge_percentage)) as json_file:
                data = json.load(json_file)
                vertices = data["vertices"]
                edges = data["edges"]
                print(f"{n_vertices=}")
                print(f"{edge_percentage=}")
                print(f"{vertices=}")
                print(f"{edges=}")
                draw_graph(vertices, edges, n_vertices, edge_percentage)

def create_graph(vertices, edges):
    
    G = nx.Graph()

    for vertex in vertices.keys():
        G.add_node(vertex, pos = vertices[vertex])

    for edge in edges:
        G.add_edge(str(edge[0]),str(edge[1]))

    return G

def load_single_graph(edge_percentage, n_vertices):
    with open("graphs/{}_vertices_{}_edge_percentage.json".format(n_vertices,edge_percentage)) as json_file:
                data = json.load(json_file)
                vertices = data["vertices"]
                edges = data["edges"]
    return create_graph(vertices, edges)

def load_graphs(max_vertices):
    edge_percentage_list = [0.125, 0.25, 0.5, 0.75]
    n_vertices_list = range(4,max_vertices+1)

    graphs = []

    for n_vertices in n_vertices_list:
        for edge_percentage in edge_percentage_list:
            with open("graphs/{}_vertices_{}_edge_percentage.json".format(n_vertices,edge_percentage)) as json_file:
                data = json.load(json_file)
                vertices = data["vertices"]
                edges = data["edges"]
                graphs.append(create_graph(vertices, edges))

    return graphs

def remove_isolated_vertices(G):
    return G.subgraph([v for v in G if G.degree(v) > 0])

def is_clique(adjacency_matrix, vertices):
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if adjacency_matrix[int(vertices[i])][int(vertices[j])] == 0:
                return False
    return True

def neighbors(adjancency_matrix, vertex):
    return {v for v in range(len(adjancency_matrix)) if adjancency_matrix[vertex][v]}