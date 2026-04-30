import heapq


def dijkstra(grid, start, end):
    count = 0
    open_set = []
    start.distance = 0
    heapq.heappush(open_set, (start.distance, count, start))
    came_from = {}
    open_set_hash = {start}

    while open_set:
        _, _, current = heapq.heappop(open_set)
        if current is end:
            # reconstruct
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
            temp_d = current.distance + 1
            if temp_d < neighbor.distance:
                came_from[neighbor] = current
                neighbor.distance = temp_d
                count += 1
                heapq.heappush(open_set, (neighbor.distance, count, neighbor))
                open_set_hash.add(neighbor)
                neighbor.make_frontier()

        if current.color != start.color:
            current.make_visited()

        yield False

    yield None
