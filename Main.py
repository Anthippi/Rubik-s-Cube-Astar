import random
import copy
from Cube import RubiksCube
from CubeState import CubeState
from Astar import AStarSolver

def scramble_cube(cube, num_moves=5):
    """
    Μπερδεύει τον κύβο εφαρμόζοντας έναν αριθμό από τυχαίες κινήσεις.
    - `num_moves`: Πόσες κινήσεις θα εφαρμοστούν για το μπέρδεμα.
    - Αποφεύγεται η εφαρμογή διαδοχικών αντίστροφων κινήσεων (π.χ. "U" -> "U'").
    Επιστρέφει τον μπερδεμένο κύβο και τη λίστα των κινήσεων που έγιναν.
    """
    moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
    opposite_moves = {
        'U': "U'", "U'": 'U',
        'D': "D'", "D'": 'D',
        'L': "L'", "L'": 'L',
        'R': "R'", "R'": 'R',
        'F': "F'", "F'": 'F',
        'B': "B'", "B'": 'B'
    }

    scramble_moves = []
    for _ in range(num_moves):
        if scramble_moves:
            # Εξασφαλίζουμε ότι δεν επιλέγουμε την αντίστροφη κίνηση της προηγούμενης
            last_move = scramble_moves[-1]
            available_moves = [m for m in moves if m != opposite_moves[last_move]]
        else:
            available_moves = moves

        move = random.choice(available_moves)  # Επιλογή τυχαίας κίνησης
        cube.apply_move(move)  # Εφαρμογή της κίνησης στον κύβο
        scramble_moves.append(move)  # Αποθήκευση της κίνησης

    return cube, scramble_moves  # Επιστροφή του μπερδεμένου κύβου και των κινήσεων

def main():

    # 1. Δημιουργία αρχικού λυμένου κύβου
    original_cube = RubiksCube()
    print("=== Αρχική Κατάσταση Κύβου ===")
    original_cube.display()  # Εμφάνιση αρχικού κύβου

    # 2. Μπέρδεμα του κύβου
    scrambled_cube, scramble_moves = scramble_cube(original_cube, num_moves=10)
    print("\n=== Μπερδεμένος Κύβος ===")
    print(f"Κινήσεις για το μπέρδεμα: {' -> '.join(scramble_moves)}")  # Εμφάνιση κινήσεων που εφαρμόστηκαν
    scrambled_cube.display()  # Εμφάνιση του μπερδεμένου κύβου

    # 3. Επίλυση του κύβου με τον αλγόριθμο A*
    print("\n=== Αρχή Επίλυσης με A* ===")
    initial_state = CubeState(scrambled_cube)  # Δημιουργία αρχικής κατάστασης για το A*
    solver = AStarSolver(initial_state)  # Δημιουργία του αντικειμένου επίλυσης
    solution = solver.solve()  # Εκτέλεση του A*

    # 4. Εμφάνιση αποτελεσμάτων
    if solution:
        print(f"\nΒρέθηκε λύση σε {len(solution)} βήματα:")
        print(" -> ".join(solution))  # Εκτύπωση των κινήσεων που λύνουν τον κύβο

        # 5. Επαλήθευση της λύσης εφαρμόζοντας τις κινήσεις στην αρχική κατάσταση
        solved_cube = copy.deepcopy(scrambled_cube)  # Δημιουργία αντιγράφου του μπερδεμένου κύβου
        for move in solution:
            solved_cube.apply_move(move)  # Εφαρμογή κάθε κίνησης της λύσης
            solved_cube.display()  # Εμφάνιση της κατάστασης μετά από κάθε κίνηση

        print("\n=== Επιλυμένος Κύβος ===")
        solved_cube.display()  # Τελική εμφάνιση του λυμένου κύβου
    else:
        print("\nΔεν βρέθηκε λύση!")  # Αν δεν βρεθεί λύση, εκτυπώνεται μήνυμα αποτυχίας

if __name__ == "__main__":
    main()  # Εκκίνηση του προγράμματος
