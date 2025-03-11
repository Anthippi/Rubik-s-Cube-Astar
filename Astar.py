import heapq


class AStarSolver:
    def __init__(self, initial_state):
        self.open = []
        self.closed = set()
        heapq.heappush(self.open, (initial_state.f, id(initial_state), initial_state))

    def solve(self):
        while self.open:
            current = heapq.heappop(self.open)[2]
            if current.is_final():
                return current.get_path()
            if current in self.closed:
                continue
            self.closed.add(current)
            for child in current.get_children():
                if child not in self.closed:
                    heapq.heappush(self.open, (child.f, id(child), child))
        return None
