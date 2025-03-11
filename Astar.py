from queue import PriorityQueue
from collections import defaultdict

class AStarSolver:
    def __init__(self, initial_state):
        self.open = PriorityQueue()
        self.closed = defaultdict(bool)
        self.open.put((initial_state.f, initial_state))
        self.came_from = {}  # Για να παρακολουθείτε το μονοπάτι

    def solve(self):
        while not self.open.empty():
            current = self.open.get()[1]
            if current.is_final():
                return self.reconstruct_path(current)
            if self.closed[hash(current)]:
                continue
            self.closed[hash(current)] = True
            for child in current.get_children():
                if not self.closed.get(hash(child), False):
                    self.open.put((child.f, child))
                    self.came_from[child] = current
        return None

    def reconstruct_path(self, current):
        path = []
        while current in self.came_from:
            path.append(current.move)
            current = self.came_from[current]
        return path[::-1]
