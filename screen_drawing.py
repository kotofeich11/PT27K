import pygame
from pygame import Surface
import screen_drawing as SC

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 128, 0)



def draw_splash_screen(screen: Surface):
    
    line_width = 60

# Used to manage how fast the screen updates
#clock = pygame.time.Clock()

    screen.fill(white)

    pygame.draw.circle(screen, red, (250, 250), 165, 30)

    top_left = (100, 100)
    bottom_right = (400, 400)
    top_right = (400, 100)
    bottom_left = (100, 400)

# Draw the first diagonal line (from top-left to bottom-right)
    pygame.draw.line(screen, green, top_left, bottom_right, line_width)

# Draw the second diagonal line (from top-right to bottom-left)
    pygame.draw.line(screen, green, top_right, bottom_left, line_width)

    font_size = 66
    font = pygame.font.Font(None, font_size)  # None means using the default font

    # Text to display
    text = "Tic Tac Toe"

    # Render the text
    text_surface = font.render(text, True, black)  # True for anti-aliasing

    # Calculate position (centered)
    text_rect = text_surface.get_rect(center=(250, 437))

    # Blit the text onto the screen at the specified position
    screen.blit(text_surface, text_rect)

    return screen

def draw_start_screen(screen: Surface):
    
    line_width = 30

# # Used to manage how fast the screen updates
# #clock = pygame.time.Clock()

    screen.fill(white)

    pygame.draw.circle(screen, red, (100, 200), 85, 30)

    top_left = (315, 115)
    bottom_right = (485, 285)
    top_right = (485, 115)
    bottom_left = (315, 285)

# Draw the first diagonal line (from top-left to bottom-right)
    pygame.draw.line(screen, green, top_left, bottom_right, line_width)

# Draw the second diagonal line (from top-right to bottom-left)
    pygame.draw.line(screen, green, top_right, bottom_left, line_width)

    font_size = 66
    font = pygame.font.Font(None, font_size)  # None means using the default font

    # Text to display
    text = "Choose your destiny"

    # Render the text
    text_surface = font.render(text, True, black)  # True for anti-aliasing

    # Calculate position (centered)
    text_rect = text_surface.get_rect(center=(250, 437))

    # Blit the text onto the screen at the specified position
    screen.blit(text_surface, text_rect)

    return screen

def draw_game_screen(screen: Surface, grid, field_width, field_height, field_margin):
    
    line_width = 30

# # Used to manage how fast the screen updates
# #clock = pygame.time.Clock()

    screen.fill(black)

    for row in range(3):
        for column in range(3):
            if grid[row][column] == 0:
                color = white
            else:
                color = green
            pygame.draw.rect(screen,
                             color,
                             [field_margin + (field_width + field_margin) * column,
                              field_margin + (field_height + field_margin) * row,
                              field_width,
                              field_height])

    return screen

def update_grid(field_width, field_margin, screen, grid):
    for row in range(3):
        for column in range(3):
            if grid[row][column] == 1:
                            pygame.draw.circle(screen, SC.red, 
                                            (int(column * (field_width  + field_margin) + field_margin + field_width//2), int(row * (field_width  + field_margin) + field_margin + field_width//2)), 
                                            50, 10)
            elif grid[row][column] == 2:
                pygame.draw.line(screen, SC.green, 
                                                (column * (field_width + field_margin) + field_margin, row * (field_width + field_margin) + field_width + field_margin), 
                                                (column * (field_width + field_margin) + field_width + field_margin, row * (field_width + field_margin) + field_margin), 15)
                pygame.draw.line(screen, SC.green, 
                                                 (column * (field_width + field_margin) + field_margin, row * (field_width + field_margin) + field_margin), 
                                                 (column * (field_width + field_margin) + field_width + field_margin, row * (field_width + field_margin) + field_width + field_margin), 15)

def draw_end_screen(screen: Surface, text:str):
    
    screen.fill(white)
    
    font_size = 60
    font = pygame.font.Font(None, font_size)  # None means using the default font

    # Render the text
    text_surface = font.render(text, True, black)  # True for anti-aliasing

    # Calculate position (centered)
    text_rect = text_surface.get_rect(center=(250, 150))

    # Blit the text onto the screen at the specified position
    screen.blit(text_surface, text_rect)

    # Render the text
    text_restart = font.render('Do you want to restart?', True, black)  # True for anti-aliasing

    # Calculate position (centered)
    text_rect2 = text_restart.get_rect(center=(250, 300))

    # Blit the text onto the screen at the specified position
    screen.blit(text_restart, text_rect2)

    # Render the text
    text_yes = font.render('Yes', True, black)  # True for anti-aliasing

    # Calculate position (centered)
    text_rect3 = text_yes.get_rect(center=(100, 450))

    # Blit the text onto the screen at the specified position
    screen.blit(text_yes, text_rect3)

    # Render the text
    text_no = font.render('No', True, black)  # True for anti-aliasing

    # Calculate position (centered)
    text_rect4 = text_no.get_rect(center=(400, 450))

    # Blit the text onto the screen at the specified position
    screen.blit(text_no, text_rect4)

    return screen