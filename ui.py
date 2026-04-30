import pygame
from config import SIDEBAR_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT, SIDEBAR_BG, BUTTON_COLOR, BUTTON_HOVER, TEXT_COLOR, FPS


class Button:
    def __init__(self, rect, text, font, base=BUTTON_COLOR, hover=BUTTON_HOVER, text_color=TEXT_COLOR):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.base = base
        self.hover = hover
        self.text_color = text_color

    def draw(self, win, mouse_pos):
        color = self.hover if self.rect.collidepoint(mouse_pos) else self.base
        pygame.draw.rect(win, color, self.rect, border_radius=6)
        txt = self.font.render(self.text, True, self.text_color)
        txt_rect = txt.get_rect(center=self.rect.center)
        win.blit(txt, txt_rect)

    def is_hover(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


def draw_sidebar(win, selected_algo, status_text, font_small, font_title, buttons, legend_items):
    sidebar_rect = pygame.Rect(WINDOW_WIDTH - SIDEBAR_WIDTH, 0, SIDEBAR_WIDTH, WINDOW_HEIGHT)
    pygame.draw.rect(win, SIDEBAR_BG, sidebar_rect)

    # Title
    title = font_title.render("Pathfinding Visualizer", True, TEXT_COLOR)
    win.blit(title, (WINDOW_WIDTH - SIDEBAR_WIDTH + 12, 12))

    # Algorithm label
    algo_label = font_small.render(f"Algorithm: {selected_algo}", True, TEXT_COLOR)
    win.blit(algo_label, (WINDOW_WIDTH - SIDEBAR_WIDTH + 12, 60))

    # Status
    status = font_small.render(status_text, True, TEXT_COLOR)
    win.blit(status, (WINDOW_WIDTH - SIDEBAR_WIDTH + 12, 86))

    # Buttons drawn separately by caller

    # Legend
    y = WINDOW_HEIGHT - 150
    legend_title = font_small.render("Legend:", True, TEXT_COLOR)
    win.blit(legend_title, (WINDOW_WIDTH - SIDEBAR_WIDTH + 12, y))
    y += 20
    for name, color in legend_items:
        pygame.draw.rect(win, color, (WINDOW_WIDTH - SIDEBAR_WIDTH + 12, y, 20, 20))
        txt = font_small.render(name, True, TEXT_COLOR)
        win.blit(txt, (WINDOW_WIDTH - SIDEBAR_WIDTH + 40, y))
        y += 28
