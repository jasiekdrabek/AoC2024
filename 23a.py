from itertools import combinations

def find_connected_triples(file_path):
    # Wczytanie danych z pliku
    with open(file_path, 'r') as file:
        connections = [line.strip().split('-') for line in file.readlines()]
    
    # Tworzenie zbioru połączeń dla szybkiego sprawdzania
    connection_set = set(tuple(sorted(conn)) for conn in connections)

    # Tworzymy listę unikalnych komputerów
    computers = set(comp for conn in connections for comp in conn)

    # Sprawdzanie każdej kombinacji trzech komputerów
    triples = []
    for triple in combinations(computers, 3):
        # Jeśli każdy komputer z trójki jest połączony ze sobą
        if (
            tuple(sorted([triple[0], triple[1]])) in connection_set and
            tuple(sorted([triple[0], triple[2]])) in connection_set and
            tuple(sorted([triple[1], triple[2]])) in connection_set
        ) and (triple[0].startswith('t') or triple[1].startswith('t') or triple[2].startswith('t')):
            triples.append(triple)

    return triples

# Ścieżka do pliku
file_path = '23.txt'

# Znalezienie wszystkich połączonych trójek
connected_triples = find_connected_triples(file_path)

# Wyświetlenie wyniku
print(len(connected_triples))
