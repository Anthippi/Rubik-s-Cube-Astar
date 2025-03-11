import numpy as np

class CubeState:
    def __init__(self, cube, parent=None, g=0, move=None):
        self.cube = cube.fast_copy()  # Δημιουργεί ένα αντίγραφο του κύβου για να διατηρηθεί η αρχική κατάσταση
        self.parent = parent  # Αποθηκεύει τον γονέα (την προηγούμενη κατάσταση) για ανίχνευση της διαδρομής
        self.move = move  # Κίνηση που οδήγησε σε αυτή την κατάσταση
        self.g = g  # Κόστος της διαδρομής από την αρχική κατάσταση (αριθμός κινήσεων)
        self.h = self.heuristic()  # Υπολογισμός ευρετικής συνάρτησης (πόσα πλακίδια είναι σε λάθος θέση)
        self.f = self.g + self.h  # Συνολικό κόστος f(n) = g(n) + h(n)

    def heuristic(self):
        # Υπολογίζει τον αριθμό των λανθασμένων πλακιδίων σε σχέση με το κεντρικό χρώμα κάθε έδρας
        distance = 0
        for face in self.cube.faces.values():
            target_color = face[1, 1]  # Το κεντρικό χρώμα της έδρας (στόχος)
            mismatches = np.sum(face != target_color)  # Μετράει πόσα πλακίδια δεν ταιριάζουν
            distance += mismatches
        return distance // 8  # Κανονικοποίηση με βάση τα 8 μη κεντρικά πλακίδια κάθε έδρας

    def is_final(self):
        # Ελέγχει αν όλες οι έδρες του κύβου έχουν ομοιόμορφο χρώμα (αν έχει λυθεί)
        return all(np.all(face == face[1, 1]) for face in self.cube.faces.values())

    def get_children(self):
        # Δημιουργεί νέες καταστάσεις (παιδιά) εφαρμόζοντας όλες τις δυνατές κινήσεις στον κύβο
        moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
        opposite_moves = {"U": "U'", "U'": "U", "D": "D'", "D'": "D",
                          "L": "L'", "L'": "L", "R": "R'", "R'": "R",
                          "F": "F'", "F'": "F", "B": "B'", "B'": "B"}

        children = []
        for move in moves:
            # Αγνοούμε την αντίστροφη κίνηση από την τελευταία που έγινε για αποφυγή άσκοπης επαναφοράς
            if self.parent and self.parent.move == opposite_moves.get(move):
                continue  
            new_cube = self.cube.fast_copy()  # Αντιγράφει τον κύβο για να μην αλλοιωθεί η τρέχουσα κατάσταση
            new_cube.apply_move(move)  # Εφαρμόζει την κίνηση
            children.append(CubeState(new_cube, self, self.g + 1, move))  # Δημιουργεί νέα κατάσταση και την προσθέτει στη λίστα
        return children

    def __hash__(self):
        # Υπολογίζει ένα μοναδικό hash βασισμένο στις έδρες του κύβου, ώστε να μπορούμε να αποθηκεύουμε καταστάσεις σε σύνολα (sets)
        return hash(tuple(self.cube.faces[f].tobytes() for f in ['U', 'D', 'F', 'B', 'L', 'R']))

    def __eq__(self, other):
        # Δύο καταστάσεις θεωρούνται ίδιες αν όλες οι έδρες του κύβου είναι ίδιες
        return all(np.array_equal(self.cube.faces[f], other.cube.faces[f]) for f in ['U', 'D', 'F', 'B', 'L', 'R'])

    def __lt__(self, other):
        # Ορίζει τη σχέση μικρότερου για τη χρήση της κατάστασης σε ουρές προτεραιότητας (π.χ. στο A*)
        return self.f < other.f
