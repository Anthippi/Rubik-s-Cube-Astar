# Rubik's Cube Solver Using A* Algorithm

## File Structure

### `Astar.py`
- Implements the A* search algorithm with:
  - Priority queue for open states (frontier)
  - Closed set for explored states
  - Path reconstruction functionality

### `Cube.py`
- Creates Rubik's Cube structure
- Defines all possible moves (U, F, R, etc.)
- Contains methods for:
  - Visualizing cube state
  - Applying moves
  - Scrambling the cube

### `CubeState.py`
- Represents a cube state with:
  - Heuristic calculation: 
    ```python
    sum(np.sum(face != face[1,1]) for face in self.cube.faces.values()
    ```
  - Child state generation (all possible moves)
  - State comparison methods (`__hash__` and `__eq__`)

### `Main.py`
- Main execution script:
  - Scrambles cube with random moves
  - Calls A* solver
  - Displays solution path
---

## Heuristic & Scoring
- **Heuristic (h)**: 
  Counts mismatched colors per face relative to center
```python
  return sum(np.sum(face != face[1,1]) for face in self.cube.faces.values()
```
- `g`: Path cost from initial state (number of moves)
- `f = g + h`: Total score for state prioritization

## Key Parameters
Modify scramble intensity in Main.py:
```python
scrambled_cube, scramble_moves = scramble_cube(original_cube, num_moves=10)  # Default: 10 moves
```
---
## Execution
```bash
python Main.py
```
## OUTPUT
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

## Dependencies
Install required library:
```bash
pip install numpy
```
