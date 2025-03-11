import numpy as np

class CubeState:
    def __init__(self, cube, parent=None, g=0, move=None):
        self.cube = cube.fast_copy()  # Δημιουργεί ένα αντίγραφο του κύβου
        self.parent = parent  # Γονική κατάσταση στην αναζήτηση
        self.move = move  # Αποθηκεύει την κίνηση που δημιούργησε αυτήν την κατάσταση
        self.g = g  # Κόστος από την αρχική κατάσταση (αριθμός κινήσεων)
        self.h = self.heuristic()  # Ευρετικό κόστος (λανθασμένα πλακίδια)
        self.f = self.g + self.h  # Συνολικό κόστος (g + h)

    def heuristic(self):
        # Υπολογίζει τον αριθμό των λανθασμένων πλακιδίων σε κάθε έδρα
        distance = 0
        for face in self.cube.faces.values():
            target_color = face[1, 1]  # Χρώμα του κέντρου της έδρας
            mismatches = np.sum(face != target_color)
            distance += mismatches
        return distance // 8  # Κανονικοποίηση με βάση τα 8 μη κεντρικά πλακίδια

    def is_final(self):
        # Ελέγχει αν όλες οι έδρες έχουν το ίδιο χρώμα με το κέντρο τους
        return all(np.all(face == face[1, 1]) for face in self.cube.faces.values())

    def get_children(self):
        moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
        opposite_moves = {"U": "U'", "U'": "U", "D": "D'", "D'": "D",
                          "L": "L'", "L'": "L", "R": "R'", "R'": "R",
                          "F": "F'", "F'": "F", "B": "B'", "B'": "B"}

        children = []
        for move in moves:
            if self.parent and self.parent.move == opposite_moves.get(move):
                continue  # Αγνόησε αντίστροφες κινήσεις
            new_cube = self.cube.fast_copy()
            new_cube.apply_move(move)
            children.append(CubeState(new_cube, self, self.g + 1, move))
        return children

    def __hash__(self):
        # Υπολογίζει το hash βάσει των εδρών του κύβου
        return hash(tuple(self.cube.faces[f].tobytes() for f in ['U', 'D', 'F', 'B', 'L', 'R']))

    def __eq__(self, other):
        # Ελέγχει αν δύο καταστάσεις είναι ίδιες συγκρίνοντας τις έδρες τους
        return all(np.array_equal(self.cube.faces[f], other.cube.faces[f]) for f in ['U', 'D', 'F', 'B', 'L', 'R'])

    def __lt__(self, other):
        # Χρησιμοποιείται για τη σύγκριση στην ουρά προτεραιότητας (min-heap)
        return self.f < other.f

    def get_path(self):
        path = []
        current = self
        while current.parent:
            path.append(current.move)
            current = current.parent
        return path[::-1]
