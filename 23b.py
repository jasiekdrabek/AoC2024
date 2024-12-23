import networkx as nx

def find_largest_clique_with_t(file_path):
    # Wczytanie danych z pliku
    with open(file_path, 'r') as file:
        connections = [line.strip().split('-') for line in file.readlines()]
    
    # Tworzenie grafu
    graph = nx.Graph()
    graph.add_edges_from(connections)

    # Znalezienie wszystkich klik
    cliques = nx.algorithms.clique.find_cliques(graph)
    
    # Filtrowanie klik, które zawierają komputer zaczynający się od "t"
    cliques_with_t = [clique for clique in cliques if any(node.startswith('t') for node in clique)]
    
    if not cliques_with_t:
        return None  # Brak klik spełniających warunek
    
    # Znalezienie największej kliki spośród tych z "t"
    largest_clique = max(cliques_with_t, key=len)

    return largest_clique

# Ścieżka do pliku
file_path = '23.txt'

# Znalezienie największego zbioru połączonych komputerów (klika z "t")
largest_clique_with_t = find_largest_clique_with_t(file_path)

# Wyświetlenie wyniku
if largest_clique_with_t:
    print("Największy zbiór połączonych komputerów (klika z komputerem na 't'):")
    print(sorted(largest_clique_with_t))
else:
    print("Nie znaleziono kliki z komputerem zaczynającym się od 't'.")
