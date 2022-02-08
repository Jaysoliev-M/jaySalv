#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def choose_marker():
    """Выбор игровой роли: крестик или нолик"""

    player_mark = ''
    
    while player_mark not in ('X','O'):
        
        player_mark = str(input('Выберите, за кого хотите сыграть "Х" или "O": ').upper()) 
            
        if player_mark == 'X':
            robot = 'O'
        else:
            robot = 'X'
            
    return (player_mark, robot)


def who_starts_first(markers):
    """Определение случайным образом игрока, который будет ходить первым"""
    import random
    return markers[random.choice((0, 1))]


def the_first_move(markers):
    
    first_one = who_starts_first(markers)
    
    #позиции игороков
    player_mark = markers[0]
    robot_mark = markers[1]
    
    if first_one is player_mark:
        print('Игру начинаете Вы!')
        mark = player_mark
        
    elif first_one is robot_mark:
        print('Игру начинает Робот!')
        mark = robot_mark
        
    return mark


def display_board(board):
    """Генерация игрового поля"""
    list_1 = list(range(0,101))
    print('-'*51)
    for i in range(10):
        if i == 0:
            print('|  {0} |  {1} |  {2} |  {3} |  {4} |  {5} |  {6} |  {7} |  {8} |  {9} |'.format(board[0+i*10], board[1+i*10], board[2+i*10], 
                                                                                                   board[3+i*10],board[4+i*10], board[5+i*10],
                                                                                                   board[6+i*10], board[7+i*10], board[8+i*10], board[9+i*10]))
            print('-'*51)


        else:
            print('| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} |'.format(board[0+i*10], board[1+i*10], board[2+i*10], 
                                                                                         board[3+i*10],board[4+i*10], board[5+i*10],
                                                                                         board[6+i*10], board[7+i*10], board[8+i*10], board[9+i*10]))
            print('-'*51)                 
            
            
#человек выбирает позицию    
def choose_position(board, mark):
    
    position = int(input("Введите число от 0 до 99: "))
    position_occupied = True
    while position_occupied:
        if board[position] == 'X':
            position = int(input("Там уже стоит 'X'. Введите еще раз: "))
        elif board[position] == 'O':
            position = int(input("Там уже стоит 'O'. Введите еще раз: "))
        else:
            position_occupied = False
            
    mark = '\033[91m'+'\033[1m'+'\033[4m'+mark+'\033[0m'
    board[position] = mark
    
    
#робот выбирает позицию через рандом
def robot_position(board, mark):
    import random
    position = random.randint(0,99)
    position_occupied = True
    
    while position_occupied:
        if board[position] == 'X':
            position = random.randint(0,99)
        elif board[position] == 'O':
            position = random.randint(0,99)
        else:
            position_occupied = False 
            
    mark = '\033[94m'+'\033[1m'+'\033[4m'+mark+'\033[0m'
    
    board[position] = mark
    print(f'Робот решил поставить на {position}!')

    
def positions(board, mark, markers):
    
    #игра начинается с Робота
    if mark == markers[1]:
        robot_position(board, mark)

    #игра начинается с Игрока
    elif mark == markers[0]:
        choose_position(board, mark)
    
    
#проверяем на выигрыш игру
def check_if_game_over(board, mark, markers):

    win_boolean_cases = []
    mark1 = '\033[91m'+'\033[1m'+'\033[4m'+mark+'\033[0m'
    mark2 = '\033[94m'+'\033[1m'+'\033[4m'+mark+'\033[0m'
    
    #ищем выигрыш по строкам
    for j in range (10):
        for i in range(6):
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+1] == board[j*10+i+2] == board[j*10+i+3] == board[j*10+i+4] == mark1)
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+1] == board[j*10+i+2] == board[j*10+i+3] == board[j*10+i+4] == flip_player(mark1))
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+1] == board[j*10+i+2] == board[j*10+i+3] == board[j*10+i+4] == mark2)
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+1] == board[j*10+i+2] == board[j*10+i+3] == board[j*10+i+4] == flip_player(mark2))   
    
    #ищем выигрыш по столбцам                     
    for j in range (6):
        for i in range(10):
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+10] == board[j*10+i+20] == board[j*10+i+30] == board[j*10+i+40] == mark1)                           
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+10] == board[j*10+i+20] == board[j*10+i+30] == board[j*10+i+40] == flip_player(mark1))                       
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+10] == board[j*10+i+20] == board[j*10+i+30] == board[j*10+i+40] == mark2)                           
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+10] == board[j*10+i+20] == board[j*10+i+30] == board[j*10+i+40] == flip_player(mark2))
    
    #ищем выигрыш по диогонали
    for j in range (6):
        for i in range(6):
            win_boolean_cases.append(board[i*10+j] == board[i*10+j+11] == board[i*10+j+22] == board[i*10+j+33] == board[i*10+j+44] == mark1) 
            win_boolean_cases.append(board[i*10+j] == board[i*10+j+11] == board[i*10+j+22] == board[i*10+j+33] == board[i*10+j+44] == flip_player(mark1))
            win_boolean_cases.append(board[i*10+j] == board[i*10+j+11] == board[i*10+j+22] == board[i*10+j+33] == board[i*10+j+44] == mark2) 
            win_boolean_cases.append(board[i*10+j] == board[i*10+j+11] == board[i*10+j+22] == board[i*10+j+33] == board[i*10+j+44] == flip_player(mark2))
    
    #ищем выигрыш по обратной диогонали
    for j in range (9,3,-1):
        for i in range(9,3,-1):
            win_boolean_cases.append(board[i*10+j] == board[i*10+j-11] == board[i*10+j-22] == board[i*10+j-33] == board[i*10+j-44] == mark1)  
            win_boolean_cases.append(board[i*10+j] == board[i*10+j-11] == board[i*10+j-22] == board[i*10+j-33] == board[i*10+j-44] == flip_player(mark1))
            win_boolean_cases.append(board[i*10+j] == board[i*10+j-11] == board[i*10+j-22] == board[i*10+j-33] == board[i*10+j-44] == mark2)  
            win_boolean_cases.append(board[i*10+j] == board[i*10+j-11] == board[i*10+j-22] == board[i*10+j-33] == board[i*10+j-44] == flip_player(mark2))
    
    if True in win_boolean_cases:
        print(f'Вы проиграли Роботу!')
        return False
    
    elif len(set(board)) == 2:
        print('Кажется ничья!')
        return False
    
    else:
        return True
                              

def flip_player(mark):
    """Переключение роли игрока для смены очереди для хода"""
    return 'O' if mark == 'X' else 'X'

    
def play_game():
    
    print('Игра в "Крестики-нолики"')

    playing = True
        
    #данные для доски
    PLAY_BOARD = [str(num) for num in range(0, 101)]

    #пустой список для записи всех выигрышей (по вертикали, горизонтали, диогонали)
    win_boolean_cases = []
        
    #выбираем каким маркером игрок хочет начать игру
    CHOOSE_MARKERS = choose_marker()
    
    #рандомно выбирается, какой маркер начнет
    CURRENT_PLAYER_MARK = the_first_move(CHOOSE_MARKERS)

    while playing:
                
        display_board(PLAY_BOARD)
        #проверяем на выигрыш или ничью
        playing = check_if_game_over(PLAY_BOARD, flip_player(CURRENT_PLAYER_MARK), CHOOSE_MARKERS)
        if playing is False:
                    break
        
        positions(PLAY_BOARD, CURRENT_PLAYER_MARK, CHOOSE_MARKERS)
        CURRENT_PLAYER_MARK = flip_player(CURRENT_PLAYER_MARK)

        

play_game()

