import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
G = nx.Graph()

# Nodes and edges for the Red Line
red_line = [
    ("Akademmistechko", (0, 7)),
    ("Zhytomyrska", (1, 6)),
    ("Sviatoshyn", (2, 5)),
    ("Nyvky", (3, 4)),
    ("Beresteiska", (4, 3)),
    ("Shuliavska", (5, 2)),
    ("Politekhnichnyi Instytut", (6, 1)),
    ("Vokzalna", (7, 0)),
    ("Universytet", (8, 0)),
    ("Teatralna", (9, 0)),
    ("Khreshchatyk", (10, 0)),
    ("Arsenalna", (11, -1)),
    ("Dnipro", (12, -2)),
    ("Hidropark", (12, -3)),
    ("Livoberezhna", (14, -2)),
    ("Darnytsia", (15, -1)),
    ("Chernihivska", (16, 0)),
    ("Lisova", (17, 1)),
]
G.add_nodes_from([(station, {"pos": pos, "color": "red"}) for station, pos in red_line])
G.add_edges_from(
    [
        (red_line[i][0], red_line[i + 1][0], {"weight": 1, "color": "red"})
        for i in range(len(red_line) - 1)
    ]
)

# Nodes and edges for the Blue Line
blue_line = [
    ("Heroiv Dnipra", (10, 6)),
    ("Minska", (10, 5)),
    ("Obolon", (10, 4)),
    ("Pochaina", (10, 3)),
    ("Tarasa Shevchenka", (10, 2)),
    ("Kontraktova Ploshcha", (10, 1)),
    ("Poshtova Ploshcha", (8, -1)),
    ("Maidan Nezalezhnosti", (9, -2)),
    ("Ploshcha Lva Tolstoho", (8, -3)),
    ("Olimpiiska", (8, -4)),
    ("Palats Ukraina", (8, -5)),
    ("Lybidska", (8, -6)),
    ("Demiivska", (7, -7)),
    ("Holosiivska", (6, -8)),
    ("Vasylkivska", (5, -9)),
    ("Vystavkovyi Tsentr", (4, -10)),
    ("Ipodrom", (3, -10.5)),
    ("Teremky", (2, -10.5)),
]
G.add_nodes_from(
    [(station, {"pos": pos, "color": "blue"}) for station, pos in blue_line]
)
G.add_edges_from(
    [
        (blue_line[i][0], blue_line[i + 1][0], {"weight": 1, "color": "blue"})
        for i in range(len(blue_line) - 1)
    ]
)


# Nodes and edges for the Green Line
green_line = [
    ("Syrets", (3, 7)),
    ("Dorohozhychi", (4, 6)),
    ("Lukianivska", (5, 5)),
    ("Zoloti Vorota", (8, 1)),
    ("Palats Sportu", (6, -2.5)),
    ("Klovska", (10, -1)),
    ("Pecherska", (10, -1)),
    ("Druzhby Narodiv", (12, -2)),
    ("Vydubychi", (10.5, -3)),
    ("Slavutych", (13, -3)),
    ("Osokorky", (14, -5)),
    ("Pozniaky", (15, -5.5)),
    ("Kharkivska", (16, -5.5)),
    ("Vyrlytsia", (17, -5)),
    ("Boryspilska", (18, -4.5)),
    ("Chervony Khutir", (19, -4)),
]
G.add_nodes_from(
    [(station, {"pos": pos, "color": "green"}) for station, pos in green_line]
)
G.add_edges_from(
    [
        (green_line[i][0], green_line[i + 1][0], {"weight": 1, "color": "green"})
        for i in range(len(green_line) - 1)
    ]
)

electrichka = [
    ("Petrivka", (5, 7)),
    ("Troyeschina", (7, 7)),
    ("Darnycia", (9, 7)),
    ("Zoloti Vorota", (8, 1)),
    ("Livyi bereh", (9, 5)),
    ("Vydubychi", (10.5, -3)),
    ("Vokzalna", (7, 0)),
    ("Shuliavska", (12, 5)),
    ("Beresteiska", (4, 3)),
    ("Syrets", (3, 7)),
]
G.add_nodes_from(
    [(station, {"pos": pos, "color": "grey"}) for station, pos in electrichka]
)
G.add_edges_from(
    [
        (electrichka[i][0], electrichka[i + 1][0], {"weight": 2, "color": "grey"})
        for i in range(len(electrichka) - 1)
    ]
)

# Adding transfer nodes real and not real for presentation purpouse
transfers = [
    ("Zoloti Vorota", "Teatralna"),
    ("Darnycia", "Livoberezhna"),
    ("Maidan Nezalezhnosti", "Khreshchatyk"),
    ("Palats Sportu", "Ploshcha Lva Tolstoho"),
    ("Politekhnichnyi Instytut", "Lybidska"),
    ("Petrivka", "Hidropark"),
]
G.add_edges_from([(u, v, {"weight": 3, "color": "yellow"}) for u, v in transfers])

node_colors = [data["color"] for _, data in G.nodes(data=True)]
edge_colors = [data["color"] for _, _, data in G.edges(data=True)]

pos = nx.get_node_attributes(G, "pos")

# Visualization of the graph
plt.figure(figsize=(14, 10))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=700,
    node_color=node_colors,
    font_size=10,
    font_weight="bold",
    edge_color=edge_colors,
    width=3,
)

plt.show()

# Analysis of the graph
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
print("Degree of each node:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

degree_histogram = nx.degree_histogram(G)
plt.figure(figsize=(10, 6))
plt.bar(range(len(degree_histogram)), degree_histogram, color="skyblue")
plt.title("Degree Histogram")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")
plt.show()
