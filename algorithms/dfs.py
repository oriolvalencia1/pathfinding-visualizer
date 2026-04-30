def dfs(grid, start, end):
    stack = [start]
    visited = {start}
    came_from = {}

    while stack:
        current = stack.pop()

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
                stack.append(neighbor)
                neighbor.make_frontier()

        if current.color != start.color:
            current.make_visited()

        yield False

    yield None
