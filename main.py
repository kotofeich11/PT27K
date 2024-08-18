from queue import Full
import pygame
import screen_drawing as SC
import logics as Logics
from typing import List

pygame.init()

width, height = 500, 500
field_width, field_height, field_margin  = 144, 144, 17

screen = pygame.display.set_mode((width, height))

done = False

player_side = ''

current_screen = 0 #0 = splash screen, 1 - start screen, 2 - game screen, 3 - end screen, 4 -restart screen

current_turn = 0 #0 - not set, 1 = pc, 2 = user

result_text = ''

def create_grid():
    grid = []

    for row in range(3):
        grid.append([])

        for column in range(3):
            grid[row].append(0)
    return grid

grid = create_grid()

screen = SC.draw_splash_screen(screen)

def make_turn(grid: List, row: int, column: int, item_id: int) -> bool:  
    if grid[row][column] == 0:
        grid[row][column] = item_id
        return True
    else:
        return False
   
while not done:

    if current_screen == 2:
        user_id = 2 if player_side == 'X' else 1
        computer_id = 1 if player_side == 'X' else 2
        if Logics.win_check(grid, computer_id):
            result_text = 'Computer wins'
            print (result_text)
            current_screen = 3
        elif Logics.win_check(grid, user_id):
            result_text = 'You win'
            print (result_text)
            current_screen = 3
        elif Logics.grid_full(grid):
            result_text = 'Draw'
            print (result_text)
            current_screen = 3
        else:
            if current_turn == 1:
                item_id = 1 if player_side == 'X' else 2
                best_turn = Logics.get_best_turn(grid, item_id)        
                if len(best_turn) == 0:               
                    if make_turn(grid, 1, 1, item_id) == True: 
                        current_turn = 2                 
                else:
                    if best_turn['type'] == 'row':
                        for counter in range(3):
                            field = grid[best_turn['number']][counter]
                            if field == 0:
                                if make_turn(grid, best_turn['number'], counter, item_id) == True: 
                                    current_turn = 2   
                                    break         
                    elif best_turn['type'] == 'column':
                        for counter in range(3):
                            field = grid[counter][best_turn['number']]
                            if field == 0:
                                if make_turn(grid, counter, best_turn['number'], item_id) == True: 
                                    current_turn = 2   
                                    break
                    elif best_turn['type'] == 'diagonal':
                        if best_turn['number'] == 1:
                            if grid[2][0] == 0:
                                if make_turn(grid, 2, 0, item_id) == True: 
                                    current_turn = 2   
                            elif grid[1][1] ==0:
                                if make_turn(grid, 1, 1, item_id) == True: 
                                    current_turn = 2   
                            elif grid[0][2] ==0:
                                if make_turn(grid, 0, 2, item_id) == True: 
                                    current_turn = 2   
                        elif best_turn['number'] == 2:
                            if grid[0][0]== 0:
                                if make_turn(grid, 0, 0, item_id) == True: 
                                    current_turn = 2   
                            elif grid[1][1] == 0:
                                if make_turn(grid, 1, 1, item_id) == True: 
                                    current_turn = 2   
                            elif grid[2][2] == 0:
                                if make_turn(grid, 2, 2, item_id) == True: 
                                    current_turn = 2   

            SC.update_grid(field_width, field_margin, screen, grid)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

            if current_screen == 0:      
                SC.draw_start_screen(screen)
                current_screen = 1
            elif current_screen == 1:           
                if pos[0] <= 250:
                    player_side = 'O'
                    current_turn = 1
                else:
                    player_side = 'X'
                    current_turn = 2
                print(player_side)
                SC.draw_game_screen(screen, grid, field_width, field_height, field_margin)
                current_screen = 2
            elif current_screen == 2:
                column_clicked = pos[0] // (field_width + field_margin) 
                row_clicked = pos[1] // (field_height + field_margin)
                print("Row:", row_clicked, "Column:", column_clicked)

                item_id = 2 if player_side == 'X' else 1

                if make_turn(grid, row_clicked, column_clicked, item_id) == True: 

                    SC.update_grid(field_width, field_margin, screen, grid)

                    current_turn = 1
            elif current_screen == 3:
                SC.draw_end_screen(screen, result_text)
                current_screen = 4
            elif current_screen == 4:    
                if pos[0] <= 250:
                    SC.draw_start_screen(screen)
                    current_screen = 1
                    grid = create_grid()
                else:
                    done = True

    pygame.display.flip()

pygame.quit()


     
