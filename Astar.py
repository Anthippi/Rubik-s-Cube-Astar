from queue import PriorityQueue
from collections import defaultdict

class AStarSolver:
    def __init__(self, initial_state):
        """
        Αρχικοποιεί τον αλγόριθμο A*.
        - `open`: Μια ουρά προτεραιότητας (PriorityQueue) που περιέχει τις προς εξέταση καταστάσεις.
        - `closed`: Ένα λεξικό (`defaultdict(bool)`) που κρατάει ποιες καταστάσεις έχουν ήδη εξεταστεί.
        - `came_from`: Ένα λεξικό που διατηρεί το μονοπάτι (γονείς των καταστάσεων).
        """
        self.open = PriorityQueue()  # Δημιουργία της ουράς προτεραιότητας
        self.closed = defaultdict(bool)  # Λεξικό για τις εξετασμένες καταστάσεις (false = δεν έχει εξεταστεί)
        self.open.put((initial_state.f, initial_state))  # Προσθήκη της αρχικής κατάστασης στην ουρά
        self.came_from = {}  # Λεξικό που παρακολουθεί το μονοπάτι προς τη λύση

    def solve(self):
        """
        Εκτελεί τον αλγόριθμο A* για την εύρεση της βέλτιστης λύσης.
        Επιστρέφει τη λίστα με τις κινήσεις που λύνουν τον κύβο ή None αν δεν βρεθεί λύση.
        """
        while not self.open.empty():  # Όσο υπάρχουν καταστάσεις προς εξέταση
            current = self.open.get()[1]  # Παίρνουμε την κατάσταση με το μικρότερο κόστος f
            
            if current.is_final():  # Αν η κατάσταση είναι η τελική (λυμένος κύβος)
                return self.reconstruct_path(current)  # Ανακατασκευή και επιστροφή του μονοπατιού

            if self.closed[hash(current)]:  # Αν η κατάσταση έχει ήδη εξεταστεί, την αγνοούμε
                continue

            self.closed[hash(current)] = True  # Προσθέτουμε την τρέχουσα κατάσταση στο `closed`

            for child in current.get_children():  # Δημιουργούμε τα παιδιά της τρέχουσας κατάστασης
                if not self.closed.get(hash(child), False):  # Εξετάζουμε αν το παιδί έχει ήδη ελεγχθεί
                    self.open.put((child.f, child))  # Προσθήκη στην ουρά με την προτεραιότητα f
                    self.came_from[child] = current  # Καταγράφουμε τον "γονέα" του για την ανακατασκευή της λύσης

        return None  # Επιστρέφει None αν δεν βρεθεί λύση

    def reconstruct_path(self, current):
        """
        Ανακατασκευάζει το μονοπάτι από την τελική κατάσταση στην αρχική.
        - Ξεκινά από την τελική κατάσταση και ακολουθεί τους "γονείς" προς τα πίσω.
        - Επιστρέφει τη λίστα των κινήσεων που πρέπει να γίνουν για τη λύση.
        """
        path = []
        while current in self.came_from:  # Όσο υπάρχει "γονέας" για την τρέχουσα κατάσταση
            path.append(current.move)  # Προσθέτουμε την κίνηση που οδήγησε σε αυτή την κατάσταση
            current = self.came_from[current]  # Προχωράμε προς τα πίσω στον γονέα

        return path[::-1]  # Επιστρέφουμε το μονοπάτι αντιστραμμένο (από αρχή σε τέλος)
