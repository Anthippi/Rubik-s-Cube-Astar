import numpy as np

class RubiksCube:
    def __init__(self):
        """
        Αρχικοποιεί τον κύβο του Rubik με κάθε πλευρά να έχει ένα μοναδικό χρώμα.
        Οι πλευρές αναπαριστώνται ως πίνακες NumPy 3x3.
        """
        self.faces = {
            'U': np.full((3, 3), 'W'),  # Άσπρο (White - Up)
            'D': np.full((3, 3), 'Y'),  # Κίτρινο (Yellow - Down)
            'F': np.full((3, 3), 'G'),  # Πράσινο (Green - Front)
            'B': np.full((3, 3), 'B'),  # Μπλε (Blue - Back)
            'L': np.full((3, 3), 'O'),  # Πορτοκαλί (Orange - Left)
            'R': np.full((3, 3), 'R')   # Κόκκινο (Red - Right)
        }

    def display(self):
        """Εμφανίζει τον κύβο σε ένα δισδιάστατο διάγραμμα που δείχνει τη διάταξη των χρωμάτων."""
        cross = np.full((9, 12), ' ')

        cross[0:3, 3:6] = self.faces['U']
        cross[3:6, 0:3] = self.faces['L']
        cross[3:6, 3:6] = self.faces['F']
        cross[3:6, 6:9] = self.faces['R']
        cross[6:9, 3:6] = self.faces['D']
        cross[3:6, 9:12] = self.faces['B']

        for row in cross:
            print(' '.join(row))
        print()

    def rotate_face(self, face, clockwise=True):
        """
        Περιστρέφει μία μεμονωμένη πλευρά του κύβου δεξιόστροφα ή αριστερόστροφα.
        """
        self.faces[face] = np.rot90(self.faces[face], -1 if clockwise else 1)

# ======== Περιστροφές Άνω (U) και Κάτω (D) πλευράς ========

    def rotate_U(self):
        """Περιστροφή της πάνω πλευράς (U) δεξιόστροφα."""
        self.rotate_face('U', clockwise=True)
        temp = self.faces['F'][0, :].copy()
        self.faces['F'][0, :] = self.faces['R'][0, :]
        self.faces['R'][0, :] = self.faces['B'][0, :]
        self.faces['B'][0, :] = self.faces['L'][0, :]
        self.faces['L'][0, :] = temp

    def rotate_U_prime(self):
        """Περιστροφή της πάνω πλευράς (U) αριστερόστροφα."""
        self.rotate_face('U', clockwise=False)
        temp = self.faces['F'][0, :].copy()
        self.faces['F'][0, :] = self.faces['L'][0, :]
        self.faces['L'][0, :] = self.faces['B'][0, :]
        self.faces['B'][0, :] = self.faces['R'][0, :]
        self.faces['R'][0, :] = temp

    def rotate_D(self):
        """Περιστροφή της κάτω πλευράς (D) δεξιόστροφα."""
        self.rotate_face('D', clockwise=True)
        temp = self.faces['F'][2, :].copy()
        self.faces['F'][2, :] = self.faces['L'][2, :]
        self.faces['L'][2, :] = self.faces['B'][2, :]
        self.faces['B'][2, :] = self.faces['R'][2, :]
        self.faces['R'][2, :] = temp

    def rotate_D_prime(self):
        """Περιστροφή της κάτω πλευράς (D) αριστερόστροφα."""
        self.rotate_face('D', clockwise=False)
        temp = self.faces['F'][2, :].copy()
        self.faces['F'][2, :] = self.faces['R'][2, :]
        self.faces['R'][2, :] = self.faces['B'][2, :]
        self.faces['B'][2, :] = self.faces['L'][2, :]
        self.faces['L'][2, :] = temp

# ======== Περιστροφές Αριστερής (L) και Δεξιάς (R) πλευράς ========

    def rotate_L(self):
        """Περιστροφή της αριστερής πλευράς (L) δεξιόστροφα."""
        self.rotate_face('L', clockwise=True)
        temp = self.faces['U'][:, 0].copy()
        self.faces['U'][:, 0] = self.faces['B'][:, 2]
        self.faces['B'][:, 2] = np.flipud(self.faces['D'][:, 0])
        self.faces['D'][:, 0] = np.flipud(self.faces['F'][:, 0])
        self.faces['F'][:, 0] = temp

    def rotate_L_prime(self):
        """Περιστροφή της αριστερής πλευράς (L) αριστερόστροφα."""
        self.rotate_face('L', clockwise=False)
        temp = self.faces['U'][:, 0].copy()
        self.faces['U'][:, 0] = self.faces['F'][:, 0]
        self.faces['F'][:, 0] = np.flipud(self.faces['D'][:, 0])
        self.faces['D'][:, 0] = np.flipud(self.faces['B'][:, 2])
        self.faces['B'][:, 2] = temp

    def rotate_R(self):
        """Περιστροφή της δεξιάς πλευράς (R) δεξιόστροφα."""
        self.rotate_face('R', clockwise=True)
        temp = self.faces['U'][:, 2].copy()
        self.faces['U'][:, 2] = self.faces['F'][:, 2]
        self.faces['F'][:, 2] = self.faces['D'][:, 2]
        self.faces['D'][:, 2] = np.flipud(self.faces['B'][:, 0])
        self.faces['B'][:, 0] = np.flipud(temp)

    def rotate_R_prime(self):
        """Περιστροφή της δεξιάς πλευράς (R) αριστερόστροφα."""
        self.rotate_face('R', clockwise=False)
        temp = self.faces['U'][:, 2].copy()
        self.faces['U'][:, 2] = np.flipud(self.faces['B'][:, 0])
        self.faces['B'][:, 0] = np.flipud(self.faces['D'][:, 2])
        self.faces['D'][:, 2] = self.faces['F'][:, 2]
        self.faces['F'][:, 2] = temp

# ======== Περιστροφές Μπροστινής (F) και Πίσω (B) πλευράς ========

    def rotate_F(self):
        """Περιστροφή της μπροστινής πλευράς (F) δεξιόστροφα."""
        self.rotate_face('F', clockwise=True)
        temp = self.faces['U'][2, :].copy()
        self.faces['U'][2, :] = np.flipud(self.faces['L'][:, 2])
        self.faces['L'][:, 2] = self.faces['D'][0, :]
        self.faces['D'][0, :] = np.flipud(self.faces['R'][:, 0])
        self.faces['R'][:, 0] = temp

    def rotate_F_prime(self):
        """Περιστροφή της μπροστινής πλευράς (F) αριστερόστροφα."""
        self.rotate_face('F', clockwise=False)
        temp = self.faces['U'][2, :].copy()
        self.faces['U'][2, :] = self.faces['R'][:, 0]
        self.faces['R'][:, 0] = np.flipud(self.faces['D'][0, :])
        self.faces['D'][0, :] = self.faces['L'][:, 2]
        self.faces['L'][:, 2] = np.flipud(temp)

    def rotate_B(self):
        """Περιστροφή της πίσω πλευράς (B) δεξιόστροφα."""
        self.rotate_face('B', clockwise=True)
        temp = self.faces['U'][0, :].copy()
        self.faces['U'][0, :] = self.faces['R'][:, 2]
        self.faces['R'][:, 2] = np.flipud(self.faces['D'][2, :])
        self.faces['D'][2, :] = self.faces['L'][:, 0]
        self.faces['L'][:, 0] = np.flipud(temp)

    def rotate_B_prime(self):
        """Περιστροφή της πίσω πλευράς (B) αριστερόστροφα."""
        self.rotate_face('B', clockwise=False)
        temp = self.faces['U'][0, :].copy()
        self.faces['U'][0, :] = np.flipud(self.faces['L'][:, 0])
        self.faces['L'][:, 0] = self.faces['D'][2, :]
        self.faces['D'][2, :] = np.flipud(self.faces['R'][:, 2])
        self.faces['R'][:, 2] = temp

    def apply_move(self, move):
        """Εφαρμόζει μία συγκεκριμένη κίνηση στον κύβο."""
        if move == 'U': self.rotate_U()
        elif move == "U'": self.rotate_U_prime()
        elif move == 'D': self.rotate_D()
        elif move == "D'": self.rotate_D_prime()
        elif move == 'L': self.rotate_L()
        elif move == "L'": self.rotate_L_prime()
        elif move == 'R': self.rotate_R()
        elif move == "R'": self.rotate_R_prime()
        elif move == 'F': self.rotate_F()
        elif move == "F'": self.rotate_F_prime()
        elif move == 'B': self.rotate_B()
        elif move == "B'": self.rotate_B_prime()

    def fast_copy(self):
        """Δημιουργεί ένα γρήγορο αντίγραφο του κύβου."""
        new_cube = RubiksCube()
        for face in self.faces:
            new_cube.faces[face] = np.copy(self.faces[face])
        return new_cube
