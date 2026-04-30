import pytest
from grid import Grid
from algorithms import astar, dijkstra, bfs, dfs


def make_empty_grid(rows=5, cols=5):
    g = Grid(cols=cols, rows=rows, width=500, height=500)
    return g


def test_astar_simple_path():
    g = make_empty_grid(5, 5)
    start = g.get_cell(0, 0)
    end = g.get_cell(0, 2)
    start.make_start()
    end.make_end()
    g.update_all_neighbors()
    gen = astar.astar(g, start, end)
    found = None
    for res in gen:
        found = res
    assert found is True


def test_dijkstra_simple_path():
    g = make_empty_grid(5, 5)
    start = g.get_cell(1, 0)
    end = g.get_cell(1, 3)
    start.make_start()
    end.make_end()
    g.update_all_neighbors()
    gen = dijkstra.dijkstra(g, start, end)
    found = None
    for res in gen:
        found = res
    assert found is True


def test_bfs_simple_path():
    g = make_empty_grid(5, 5)
    start = g.get_cell(2, 0)
    end = g.get_cell(2, 1)
    start.make_start()
    end.make_end()
    g.update_all_neighbors()
    gen = bfs.bfs(g, start, end)
    found = None
    for res in gen:
        found = res
    assert found is True


def test_dfs_simple_path():
    g = make_empty_grid(5, 5)
    start = g.get_cell(3, 0)
    end = g.get_cell(3, 4)
    start.make_start()
    end.make_end()
    g.update_all_neighbors()
    gen = dfs.dfs(g, start, end)
    found = None
    for res in gen:
        found = res
    assert found is True
