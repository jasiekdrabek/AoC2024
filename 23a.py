import networkx as nx
from itertools import combinations

def find_largest_clique_with_t(file_path):
    # Wczytanie danych z pliku
    with open(file_path, 'r') as file:
        connections = [line.strip().split('-') for line in file.readlines()]
    
    # Tworzenie grafu
    graph = nx.Graph()
    graph.add_edges_from(connections)

    # Znalezienie wszystkich klik
    cliques = nx.algorithms.clique.find_cliques(graph)
    cliques = [clique for clique in cliques if len(clique) >= 3]
    clique_3 = set()
    for c in cliques:
        for (x,y,z) in combinations(c,3):
            if any(node.startswith('t') for node in [x,y,z]):
                clique_3.add((x,y,z))
    
    return clique_3
# Ścieżka do pliku
file_path = '23.txt'

# Znalezienie największego zbioru połączonych komputerów (klika z "t")
clique_3 = find_largest_clique_with_t(file_path)

# Wyświetlenie wyniku
if clique_3:
    print(len(clique_3))
else:
    print("Nie znaleziono kliki z komputerem zaczynającym się od 't'.")
