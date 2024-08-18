from typing import Dict, List

def win_check(grid: List, player_id: int) -> bool:
    for column in range(3):    
        if grid[0][column] == player_id and grid[1][column] == player_id and grid[2][column] == player_id:
             return True
        
    for row in range(3):
        if grid[row][0] == player_id and grid[row][1] == player_id and grid[row][2] == player_id:
            return True
        
    if grid[2][0] == player_id and grid[1][1] == player_id and grid[0][2] == player_id:
        return True

    if grid[0][0] == player_id and grid[1][1] == player_id and grid[2][2] == player_id:
        return True

    return False      
        
def get_best_turn(grid: List, player_id: int) -> Dict:

    answer_list = {}

    max_points = 0

    for column in range(3):
        if (grid[0][column] == player_id or grid[0][column] == 0) and (grid[1][column] == player_id or grid[1][column] == 0) and (grid[2][column] == player_id or grid[2][column] == 0):
            if grid[0][column] + grid[1][column] + grid[2][column] > max_points:
                temp_dict = {'type': 'column', 'number': column, 'sum': grid[0][column] + grid[1][column] + grid[2][column]}
                max_points  = temp_dict['sum']
                answer_list.update(temp_dict)

    for row in range(3):
        if (grid[row][0] == player_id or grid[row][0] == 0) and (grid[row][1] == player_id or grid[row][1] == 0) and (grid[row][2]  == player_id or grid[row][2]== 0):
            if grid[row][0] + grid[row][1] + grid[row][2] > max_points:
                temp_dict = {'type': 'row', 'number': row, 'sum': grid[row][0] + grid[row][1] + grid[row][2]}
                max_points  = temp_dict['sum']
                answer_list.update(temp_dict)
        
    if (grid[2][0] == player_id or grid[2][0] == 0) and (grid[1][1] == player_id or grid[1][1] == 0) and (grid[0][2] == player_id or grid[0][2] == 0):
        if grid[2][0] + grid[1][1] + grid[0][2] > max_points:
            temp_dict = {'type': 'diagonal', 'number': 1, 'sum': grid[2][0] + grid[1][1] + grid[0][2]}
            max_points  = temp_dict['sum']
            answer_list.update(temp_dict)

    if (grid[0][0] == player_id or grid[0][0] == 0) and (grid[1][1] == player_id or grid[1][1] == 0) and (grid[2][2] == player_id or grid[2][2] == 0):
        if grid[0][0] + grid[1][1] + grid[2][2] > max_points:
            temp_dict = {'type': 'diagonal', 'number': 2, 'sum': grid[0][0] + grid[1][1] + grid[2][2]}
            max_points  = temp_dict['sum']
            answer_list.update(temp_dict)

    if not len(answer_list) == 0:
        return answer_list
    elif grid[1][1] == 0:
         return answer_list  
    else:       
        #no win combinations, just to fill field
        for column in range(3):
            if (grid[0][column] == 0) or grid[1][column] == 0 or grid[2][column] == 0:
                temp_dict = {'type': 'column', 'number': column, 'sum': grid[0][column] + grid[1][column] + grid[2][column]}
                max_points  = temp_dict['sum']
                answer_list.update(temp_dict)

        return answer_list  
    
def grid_full(grid: List) -> bool:
    for row in range(3):
        for column in range(3):
            if grid[row][column] == 0:
                return False
    return True


    