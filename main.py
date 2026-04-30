import pygame
import time
from config import WINDOW_WIDTH, WINDOW_HEIGHT, SIDEBAR_WIDTH, FPS, ANIMATION_DELAY, WHITE
from grid import Grid
from ui import Button, draw_sidebar
from config import ORANGE, TURQUOISE, BLACK, RED, GREEN, PURPLE
from algorithms import astar, dijkstra, bfs, dfs


def get_clicked_cell(pos, grid):
    x, y = pos
    if x >= grid.width:
        return None
    col = x // grid.cell_width
    row = y // grid.cell_height
    return grid.get_cell(row, col)


def run_app():
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    clock = pygame.time.Clock()

    grid = Grid()

    font_small = pygame.font.SysFont(None, 20)
    font_title = pygame.font.SysFont(None, 28)

    # Buttons
    bx = WINDOW_WIDTH - SIDEBAR_WIDTH + 12
    buttons = {}
    buttons['astar'] = Button((bx, 120, 170, 32), "A*", font_small)
    buttons['dijkstra'] = Button((bx, 160, 170, 32), "Dijkstra", font_small)
    buttons['bfs'] = Button((bx, 200, 170, 32), "BFS", font_small)
    buttons['dfs'] = Button((bx, 240, 170, 32), "DFS", font_small)
    buttons['run'] = Button((bx, 290, 170, 32), "Run", font_small, base=(50,160,50), hover=(80,190,80))
    buttons['clear_path'] = Button((bx, 330, 170, 32), "Clear Path", font_small)
    buttons['clear_all'] = Button((bx, 370, 170, 32), "Clear All", font_small)
    buttons['maze'] = Button((bx, 410, 170, 32), "Maze", font_small)

    selected_algo = 'A*'
    start = None
    end = None
    running_algo = False
    algo_gen = None
    status_text = "Idle"
    last_step_time = 0

    dragging = False
    erasing = False

    legend_items = [
        ("Unvisited", WHITE),
        ("Wall", BLACK),
        ("Start", ORANGE),
        ("End", TURQUOISE),
        ("Visited", RED),
        ("Frontier", PURPLE),
        ("Path", GREEN),
    ]

    def start_algorithm():
        nonlocal running_algo, algo_gen, status_text
        if not start or not end:
            status_text = "Select start and end"
            return
        grid.update_all_neighbors()
        if selected_algo == 'A*':
            algo_gen = astar.astar(grid, start, end)
        elif selected_algo == 'Dijkstra':
            algo_gen = dijkstra.dijkstra(grid, start, end)
        elif selected_algo == 'DFS':
            algo_gen = dfs.dfs(grid, start, end)
        else:
            algo_gen = bfs.bfs(grid, start, end)
        running_algo = True
        status_text = "Running..."

    def clear_path():
        nonlocal running_algo, algo_gen, status_text
        nonlocal start, end
        running_algo = False
        algo_gen = None
        grid.reset_visited()
        if start:
            start.make_start()
        if end:
            end.make_end()
        status_text = "Idle"

    def clear_all():
        nonlocal start, end, running_algo, algo_gen, status_text
        start = None
        end = None
        running_algo = False
        algo_gen = None
        grid.reset_all()
        status_text = "Idle"

    def generate_maze():
        # simple random walls peppered then carve with recursive divisions
        for r in range(grid.rows):
            for c in range(grid.cols):
                grid.get_cell(r, c).reset()
        # recursive division implementation
        def divide(r1, c1, r2, c2):
            width = c2 - c1
            height = r2 - r1
            if width < 2 or height < 2:
                return
            import random
            horizontal = width < height
            if horizontal:
                # choose a horizontal wall row
                wr = random.randrange(r1+1, r2, 2)
                gap = random.randrange(c1, c2, 2)
                for c in range(c1, c2):
                    if c == gap:
                        continue
                    grid.get_cell(wr, c).make_wall()
                divide(r1, c1, wr, c2)
                divide(wr+1, c1, r2, c2)
            else:
                wc = random.randrange(c1+1, c2, 2)
                gap = random.randrange(r1, r2, 2)
                for r in range(r1, r2):
                    if r == gap:
                        continue
                    grid.get_cell(r, wc).make_wall()
                divide(r1, c1, r2, wc)
                divide(r1, wc+1, r2, c2)

        # make outer borders
        for r in range(grid.rows):
            grid.get_cell(r, 0).make_wall()
            grid.get_cell(r, grid.cols - 1).make_wall()
        for c in range(grid.cols):
            grid.get_cell(0, c).make_wall()
            grid.get_cell(grid.rows - 1, c).make_wall()

        divide(1, 1, grid.rows - 1, grid.cols - 1)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_SPACE:
                    start_algorithm()
                if event.key == pygame.K_r:
                    clear_path()
                if event.key == pygame.K_c:
                    clear_all()

            if not running_algo:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        cell = get_clicked_cell(event.pos, grid)
                        if cell:
                            if not start:
                                start = cell
                                start.make_start()
                            elif not end and cell is not start:
                                end = cell
                                end.make_end()
                            elif cell is not start and cell is not end:
                                cell.make_wall()
                            dragging = True
                    elif event.button == 3:
                        cell = get_clicked_cell(event.pos, grid)
                        if cell:
                            if cell is start:
                                start = None
                            if cell is end:
                                end = None
                            cell.reset()
                            erasing = True
                if event.type == pygame.MOUSEBUTTONUP:
                    dragging = False
                    erasing = False
                if event.type == pygame.MOUSEMOTION and (pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]):
                    cell = get_clicked_cell(event.pos, grid)
                    if cell:
                        if pygame.mouse.get_pressed()[0]:
                            if not start:
                                start = cell
                                start.make_start()
                            elif not end and cell is not start:
                                end = cell
                                end.make_end()
                            elif cell is not start and cell is not end:
                                cell.make_wall()
                        elif pygame.mouse.get_pressed()[2]:
                            if cell is start:
                                start = None
                            if cell is end:
                                end = None
                            cell.reset()

            # button clicks always allowed
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                bx = WINDOW_WIDTH - SIDEBAR_WIDTH + 12
                # check buttons
                for key, btn in buttons.items():
                    if btn.is_hover(event.pos):
                        if key in ('astar', 'dijkstra', 'bfs', 'dfs'):
                            selected_algo = (
                                'A*' if key == 'astar'
                                else 'Dijkstra' if key == 'dijkstra'
                                else 'BFS' if key == 'bfs'
                                else 'DFS'
                            )
                        elif key == 'run':
                            clear_path()
                            start_algorithm()
                        elif key == 'clear_path':
                            clear_path()
                        elif key == 'clear_all':
                            clear_all()
                        elif key == 'maze':
                            generate_maze()

        # update algorithm step
        if running_algo and algo_gen is not None:
            now = pygame.time.get_ticks()
            if now - last_step_time >= ANIMATION_DELAY:
                try:
                    res = next(algo_gen)
                    if res is True:
                        status_text = "Done!"
                        running_algo = False
                        algo_gen = None
                    elif res is None:
                        status_text = "No path found"
                        running_algo = False
                        algo_gen = None
                except StopIteration:
                    running_algo = False
                    algo_gen = None
                last_step_time = now

        win.fill((0, 0, 0))
        grid.draw(win)

        # Draw sidebar first, then buttons on top of it
        draw_sidebar(win, selected_algo, status_text, font_small, font_title, buttons, legend_items)

        for key, btn in buttons.items():
            btn.draw(win, mouse_pos)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    run_app()
