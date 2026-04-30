![Demo](demo.gif)

# Interactive visualizer for classical pathfinding algorithms

Interactive visualizer for classical pathfinding algorithms (A*, Dijkstra, BFS) built from scratch in Python with Pygame. Demonstrates real-time algorithm animation, grid interaction, and maze generation via recursive division.

## Controls
- Left click: place start (first), end (second), then walls
- Right click: erase cell
- Click and drag: draw/erase walls
- Spacebar: run selected algorithm
- R: clear path
- C: clear all
- ESC: quit

## Setup
1. Create a virtual environment (recommended)
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run:

```bash
python main.py
```

## Algorithms
- A*: Heuristic (Manhattan) driven shortest path; fast with good heuristics.
- Dijkstra: Guarantees shortest path without heuristics; explores uniformly by distance.
- BFS: Unweighted shortest path on grids; good for small distances or unweighted graphs.
- DFS: Similar to BFS.
