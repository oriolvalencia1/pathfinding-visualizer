# Prompt — Build My Pathfinding Visualizer

Copy and paste everything below this line into another AI.

---

Build me an interactive pathfinding visualizer in Python using Pygame. The user draws walls
on a grid, places start and end points, and watches algorithms explore the grid in real time.
Here is the full spec:

## Stack
- Language: Python 3.11+
- Graphics/UI: Pygame
- Algorithms: A*, Dijkstra, BFS — all implemented manually, no external algorithm libraries

## Project Structure
```
pathfinding-visualizer/
├── main.py              # Entry point, main loop
├── grid.py              # Grid and Cell classes
├── algorithms/
│   ├── astar.py
│   ├── dijkstra.py
│   └── bfs.py
├── ui.py                # Button rendering, sidebar, legend
├── config.py            # Constants
├── requirements.txt
└── README.md
```

## Detailed Requirements

### config.py
- WINDOW_WIDTH = 900
- WINDOW_HEIGHT = 700
- GRID_COLS = 50
- GRID_ROWS = 50
- SIDEBAR_WIDTH = 200
- FPS = 60
- ANIMATION_DELAY = 15 (milliseconds between each step of the visualisation)
- Colors:
  - WHITE = (255, 255, 255)       # unvisited cell
  - BLACK = (30, 30, 30)          # wall
  - GREY = (200, 200, 200)        # grid lines
  - ORANGE = (255, 165, 0)        # start node
  - TURQUOISE = (64, 224, 208)    # end node
  - RED = (220, 50, 50)           # visited/explored cell
  - GREEN = (50, 200, 100)        # final path cell
  - PURPLE = (150, 100, 220)      # frontier/open set cell
  - SIDEBAR_BG = (40, 40, 40)
  - BUTTON_COLOR = (70, 130, 180)
  - BUTTON_HOVER = (100, 160, 210)
  - TEXT_COLOR = (240, 240, 240)

### grid.py
Cell class with attributes:
- row, col, x, y, width, height
- color (determines state)
- neighbors (list, populated by update_neighbors)
- g_score, f_score (for A*)
- distance (for Dijkstra)
- Methods: draw(win), reset(), make_start(), make_end(), make_wall(),
  make_visited(), make_frontier(), make_path(), is_wall(), is_start(), is_end()

Grid class:
- 2D list of Cell objects
- Methods: draw(win), get_cell(row, col), update_all_neighbors(),
  reset_visited() (resets visited/path/frontier cells but keeps walls, start, end)
- Neighbors: 4-directional only (no diagonals)

### algorithms/astar.py
- Implement A* using a min-heap (Python heapq)
- Heuristic: Manhattan distance
- At each step, yield the current state so the visualizer can animate it
- Use a generator function so main.py can call next() each frame
- Color frontier cells PURPLE, visited cells RED
- When path is found, reconstruct and color it GREEN (excluding start/end)
- If no path exists, display a message in the sidebar

### algorithms/dijkstra.py
- Implement Dijkstra using a min-heap
- Same generator pattern as A*
- All edge weights = 1
- Same coloring convention

### algorithms/bfs.py
- Implement BFS using a queue (collections.deque)
- Same generator pattern
- Same coloring convention

### ui.py
Sidebar (right side, SIDEBAR_WIDTH px wide):
- Title: "Pathfinding Visualizer"
- Three algorithm buttons: "A*", "Dijkstra", "BFS"
  - Highlight the currently selected algorithm
  - Hover effect on buttons
- "Run" button (green) — starts the selected algorithm
- "Clear Path" button — resets visited/path cells, keeps walls
- "Clear All" button — resets entire grid
- "Maze" button — generates a random maze using recursive division
- Legend section at the bottom showing what each color means

### main.py
Main loop behavior:
- Left click on grid:
  - First click sets start (orange)
  - Second click sets end (turquoise)
  - Further clicks draw walls (black)
- Right click: removes any cell (resets to white)
- Click and drag supported for drawing/erasing walls
- Spacebar: run the currently selected algorithm (same as Run button)
- R key: clear path
- C key: clear all
- ESC: quit
- While algorithm is running:
  - Call next() on the generator each frame with ANIMATION_DELAY
  - Disable grid editing and buttons except "Clear All"
  - Show current algorithm name and status ("Running..." / "Done!" / "No path found") in sidebar

### Maze Generation
Implement recursive division maze generation:
- Start with an empty grid
- Recursively divide the space with walls, leaving one gap per wall
- This creates a proper maze with a guaranteed solution
- Run it without animation (instant generation)

### requirements.txt
Include all necessary packages with pinned versions (really just pygame).

### README.md
Include:
- Description framed as: "Interactive visualizer for classical pathfinding algorithms
  (A*, Dijkstra, BFS) built from scratch in Python with Pygame. Demonstrates real-time
  algorithm animation, grid interaction, and maze generation via recursive division."
- A placeholder line: "![Demo](demo.gif)" at the top
- Controls reference (click, drag, keyboard shortcuts)
- Brief explanation of the difference between the three algorithms and when each is optimal
- Setup: pip install -r requirements.txt, python main.py

## Additional Notes
- All three algorithms must be implemented manually — no networkx or similar libraries
- The generator/yield pattern is required so animation is frame-by-frame, not instant
- Code must be clean and commented — this is a portfolio project
- Performance: the grid can be up to 50x50 (2500 cells) — make sure drawing is efficient
  (only redraw changed cells where possible)
- Make sure the visualizer looks polished: clean fonts (pygame.font), smooth hover effects
  on buttons, clear visual hierarchy between grid and sidebar

Generate all files in full, ready to run.