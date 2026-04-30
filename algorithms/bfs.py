from collections import deque


def bfs(grid, start, end):
    queue = deque()
    queue.append(start)
    visited = {start}
    came_from = {}

    while queue:
        current = queue.popleft()

        if current is end:
            node = end
            path = []
            while node in came_from:
                node = came_from[node]
                if node is start:
                    break
                path.append(node)
            path.reverse()
            for cell in path:
                cell.make_path()
            yield True
            return

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                neighbor.make_frontier()

        if current.color != start.color:
            current.make_visited()

        yield False

    yield None
