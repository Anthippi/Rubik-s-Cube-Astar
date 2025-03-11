import numpy as np

class CubeState:
    def __init__(self, cube, parent=None, g=0):
        self.cube = cube.fast_copy()  # Use the fast_copy method to make a shallow copy of the cube
        self.parent = parent
        self.g = g  # Path cost from the start node (number of moves)
        self.h = self.heuristic()  # Heuristic cost (misplaced tiles)
        self.f = self.g + self.h  # Total cost (g + h)

    def heuristic(self):
        distance = 0
        for face in self.cube.faces.values():
            target_color = face[1, 1]  # Center color
            mismatches = np.sum(face != target_color)
            distance += mismatches
        return distance // 8  # Normalized based on 3x3 face size (8 non-center pieces)

    def is_final(self):
        # Check if all faces are solved (i.e., all squares have the same color as the center)
        return all(np.all(face == face[1, 1]) for face in self.cube.faces.values())

    def get_children(self):
        # Generate all valid child states by applying all possible moves
        moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
        children = []
        for move in moves:
            new_cube = self.cube.fast_copy()  # Create a copy of the current cube state
            new_cube.apply_move(move)  # Apply the move to the new cube
            children.append(CubeState(new_cube, self, self.g + 1))  # Create a child state
        return children

    def __hash__(self):
        # Hashing based on the string representation of the cube's faces
        return hash(tuple(self.cube.faces[f].tobytes() for f in ['U', 'D', 'F', 'B', 'L', 'R']))

    def __eq__(self, other):
        # Comparing cube states by checking if all faces match
        return all(np.array_equal(self.cube.faces[f], other.cube.faces[f]) for f in ['U', 'D', 'F', 'B', 'L', 'R'])

    def __lt__(self, other):
        # For priority queue (min-heap) comparison
        return self.f < other.f

    def get_path(self):
        # Construct the solution path (sequence of moves)
        path = []
        current = self
        while current.parent:
            move = self.get_move_from_parent(current)
            path.append(move)
            current = current.parent
        return path[::-1]  # Return the path in reverse (from start to goal)

    def get_move_from_parent(self, current):
        """Optimized function to find the move from the parent state to current state."""
        for move in ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]:
            temp_cube = current.parent.cube.fast_copy()  # Use fast_copy instead of deepcopy
            temp_cube.apply_move(move)

            # Check if applying the move results in the current cube state
            if np.array_equal(temp_cube.faces['U'], current.cube.faces['U']) and \
                    np.array_equal(temp_cube.faces['D'], current.cube.faces['D']) and \
                    np.array_equal(temp_cube.faces['F'], current.cube.faces['F']) and \
                    np.array_equal(temp_cube.faces['B'], current.cube.faces['B']) and \
                    np.array_equal(temp_cube.faces['L'], current.cube.faces['L']) and \
                    np.array_equal(temp_cube.faces['R'], current.cube.faces['R']):
                return move
        return None  # If no move is found, return None
