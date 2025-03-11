import numpy as np
import copy

class CubeState:
    def __init__(self, cube, parent=None, g=0):
        self.cube = copy.deepcopy(cube)
        self.parent = parent
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h

    def heuristic(self):
        distance = 0
        for face_name, face in self.cube.faces.items():
            target_color = face[1, 1]
            for i in range(3):
                for j in range(3):
                    if face[i, j] != target_color:
                        distance += 1
        # Προσθήκη επιπλέον ποινών για edge/corner pieces εκτός θέσης
        return distance // 8  # Κανονικοποίηση (εξαρτάται από το cube) 3x3x3

    #def heuristic(self):
    #    return sum(np.sum(face != face[1,1]) for face in self.cube.faces.values())

    def is_final(self):
        return all(np.all(face == face[1,1]) for face in self.cube.faces.values())

    def get_children(self):
        moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
        children = []
        for move in moves:
            new_cube = self.cube.fast_copy()
            new_cube.apply_move(move)
            children.append(CubeState(new_cube, self, self.g + 1))
        return children

    def __hash__(self):
        return hash(tuple(self.cube.faces[f].tobytes() for f in ['U', 'D', 'F', 'B', 'L', 'R']))

    def __eq__(self, other):
        return all(np.array_equal(self.cube.faces[f], other.cube.faces[f]) for f in ['U', 'D', 'F', 'B', 'L', 'R'])

    def __lt__(self, other):
        return self.f < other.f

    def get_path(self):
        path = []
        current = self
        while current.parent:
            for move in ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]:
                temp = copy.deepcopy(current.parent.cube)
                temp.apply_move(move)

                # Συγκρίνουμε τα faces ως dicts
                faces_equal = True
                for face_name in temp.faces:
                    if not np.array_equal(temp.faces[face_name], current.cube.faces[face_name]):
                        faces_equal = False
                        break

                if faces_equal:
                    path.append(move)
                    break
            current = current.parent
        return path[::-1]
