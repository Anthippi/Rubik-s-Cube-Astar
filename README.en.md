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
  - Heuristic calculation
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
The heuristic function estimates the approximation cost from the current cube state to the solved state. It combines:
  - Mismatched Tiles: Counts tiles that do not match the center color of each face (excluding fixed centers).
  - Edge/Corner Penalties: Applies higher penalties for incorrect corners (+1.5 per tile) and edges (+1.2 per tile), as they require more moves to fix.

The total cost is normalized by dividing by 8 to align better with the actual move count.
- `g`: Path cost from initial state (number of moves)
- `f = g + h`: Total score for state prioritization

## Key Parameters
Modify scramble intensity in Main.py:
```python
scrambled_cube, scramble_moves = scramble_cube(original_cube, num_moves=5)  # Default: 5 moves
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
