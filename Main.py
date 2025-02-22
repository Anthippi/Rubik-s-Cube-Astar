import random
import copy
from Cube import RubiksCube
from CubeState import CubeState
from Astar import AStarSolver


def scramble_cube(cube, num_moves=5):
    """Εφαρμόζει τυχαίες κινήσεις στον κύβο και επιστρέφει τις κινήσεις"""
    moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
    scramble_moves = []  # Λίστα για την καταγραφή των κινήσεων
    for _ in range(num_moves):
        move = random.choice(moves)
        cube.apply_move(move)
        scramble_moves.append(move)  # Προσθήκη της κίνησης στη λίστα
    return cube, scramble_moves  # Επιστρέφουμε και τις κινήσεις


def main():
    # 1. Δημιουργία αρχικού κύβου
    original_cube = RubiksCube()
    print("=== Αρχική Κατάσταση Κύβου ===")
    original_cube.display()

    # 2. Μπέρδεμα του κύβου
    scrambled_cube, scramble_moves = scramble_cube(original_cube, num_moves=5)
    print("\n=== Μπερδεμένος Κύβος ===")
    print(f"Κινήσεις για το μπέρδεμα: {' -> '.join(scramble_moves)}")  # Εμφάνιση κινήσεων
    scrambled_cube.display()


    # 3. Επίλυση με A*
    print("\n=== Αρχή Επίλυσης με A* ===")
    initial_state = CubeState(scrambled_cube)
    solver = AStarSolver(initial_state)
    solution = solver.solve()

    # 4. Εμφάνιση αποτελεσμάτων
    if solution:
        print(f"\nΒρέθηκε λύση σε {len(solution)} βήματα:")
        print(" -> ".join(solution))

        # Επαλήθευση
        solved_cube = copy.deepcopy(scrambled_cube)
        for move in solution:
            solved_cube.display()
            solved_cube.apply_move(move)
        print("\n=== Επιλυμένος Κύβος ===")
        solved_cube.display()
    else:
        print("\nΔεν βρέθηκε λύση!")


if __name__ == "__main__":
    main()