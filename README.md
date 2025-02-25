# Επίλυση κύβου Rubik χρησιμοποιώντας τον αλγόριθμο **A\***.  [![Static Badge](https://img.shields.io/badge/English-orange)](README.en.md)

---

## Αρχεία
1. **`Astar.py`**  
   - Υλοποιεί τον αλγόριθμο **A\***.  
   - Χρησιμοποιεί **σωρό** για διαχείριση ανοιχτών καταστάσεων και **σύνολο** για κλειστές.  

2. **`Cube.py`**  
   - Δημιουργεί τον **κύβο Rubik** και ορίζει όλες τις **περιστροφές** (U, F, R, κλπ).  
   - Περιλαμβάνει μεθόδους για εμφάνιση του κύβου και εφαρμογή κινήσεων.  

3. **`CubeState.py`**  
   - Αναπαριστά μια **κατάσταση του κύβου**.  
   - Υπολογίζει την **ευρετική (heuristic)** ως το άθροισμα των λανθασμένων χρωμάτων ανά πλευρά.  
   - Δημιουργεί **παιδικές καταστάσεις** με όλες τις πιθανές κινήσεις.  
   - Υλοποιεί συγκρίσεις καταστάσεων με `__hash__` και `__eq__`.  

4. **`Main.py`**  
   - **Μπερδεύει** τον κύβο με τυχαίες κινήσεις.  
   - Καλεί τον **A\*** για επίλυση και εμφανίζει τη διαδρομή.  

---

## Ευρετική (Heuristic) και Σκορ  
- **`heuristic()`**  
  Μετράει πόσα κομμάτια **δεν** ταιριάζουν με το κεντρικό χρώμα κάθε πλευράς:  
  ```python
  return sum(np.sum(face != face[1,1]) for face in self.cube.faces.values())
  ```
- `g`: Κόστος από την αρχική κατάσταση (αριθμός βημάτων).
- `f = g + h`: Συνολικό σκορ για την επιλογή της επόμενης κατάστασης στον A*.
  
---
## Παράμετροι για Τροποποίηση

Αριθμός Κινήσεων Μπερδέματος
Αλλάξτε το `num_moves=5` στο `Main.py`:

```python
scrambled_cube, scramble_moves = scramble_cube(original_cube, num_moves=10) # Παράδειγμα: 10 κινήσεις
```
---

## Παράδειγμα Εκτέλεσης

```bash
=== Αρχική Κατάσταση Κύβου ===
      W W W            
      W W W            
      W W W            
O O O G G G R R R B B B
O O O G G G R R R B B B
O O O G G G R R R B B B
      Y Y Y            
      Y Y Y            
      Y Y Y            


=== Μπερδεμένος Κύβος ===
Κινήσεις για το μπέρδεμα: R -> R' -> B -> F' -> D
      R R R            
      W W W            
      R R R            
W O W G G G Y R Y B B B
W O W G G G Y R Y B B B
B B B W O W G G G Y R Y
      O Y O            
      O Y O            
      O Y O            


=== Αρχή Επίλυσης με A* ===

Βρέθηκε λύση σε 3 βήματα:
D' -> F -> B'
      R R R            
      W W W            
      R R R            
W O W G G G Y R Y B B B
W O W G G G Y R Y B B B
B B B W O W G G G Y R Y
      O Y O            
      O Y O            
      O Y O            

      R R R            
      W W W            
      R R R            
W O W G G G Y R Y B B B
W O W G G G Y R Y B B B
W O W G G G Y R Y B B B
      O O O            
      Y Y Y            
      O O O            

      R R R            
      W W W            
      W W W            
W O O G G G R R Y B B B
W O O G G G R R Y B B B
W O O G G G R R Y B B B
      Y Y Y            
      Y Y Y            
      O O O            


=== Επιλυμένος Κύβος ===
      W W W            
      W W W            
      W W W            
O O O G G G R R R B B B
O O O G G G R R R B B B
O O O G G G R R R B B B
      Y Y Y            
      Y Y Y            
      Y Y Y            
```
---
## Σημειώσεις
Απαιτούμενες Βιβλιοθήκες:
Εγκαταστήστε το `numpy` με την εντολή:
```bash
pip install numpy
```
