import heapq
from collections import defaultdict
from config import PURPLE, RED, GREEN


def heuristic(a, b):
    # Manhattan distance
    return abs(a.row - b.row) + abs(a.col - b.col)


def reconstruct_path(came_from, current, start, end):
    path = []
    while current in came_from:
        current = came_from[current]
        if current is start:
            break
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, end):
    count = 0
    open_set = []
    start.g_score = 0
    start.f_score = heuristic(start, end)
    heapq.heappush(open_set, (start.f_score, count, start))
    came_from = {}

    open_set_hash = {start}

    while open_set:
        _, _, current = heapq.heappop(open_set)
        open_set_hash.remove(current)

        if current is end:
            # reconstruct
            path = []
            node = end
            while node in came_from:
                node = came_from[node]
                if node is start:
                    break
                path.append(node)
            for cell in path:
                cell.make_path()
            yield True
            return

        for neighbor in current.neighbors:
            temp_g = current.g_score + 1
            if temp_g < neighbor.g_score:
                came_from[neighbor] = current
                neighbor.g_score = temp_g
                neighbor.f_score = temp_g + heuristic(neighbor, end)
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (neighbor.f_score, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_frontier()
        if current is not start:
            current.make_visited()

        yield False

    # no path
    yield None
