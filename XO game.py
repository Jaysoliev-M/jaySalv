#!/usr/bin/env python
# coding: utf-8

# In[109]:


def choose_marker():
    """Выбор игровой роли: крестик или нолик"""

    player_mark = ''
    while player_mark not in ('X','O'):
        player_mark = str(input('Выберите, за кого хотите сыграть "Х" или "O": ').upper())
        
        if player_mark == 'X':
            player = 'X'
            robot = 'O'
        else:
            player = 'O'
            robot = 'X'
            
    return (player, robot)


def who_starts_first(marks):
    """Определение случайным образом игрока, который будет ходить первым"""
    import random
    return marks[random.choice((0, 1))]


def the_first_move(board, tuple_marks):
    #global CURRENT_PLAYER_MARK
    global CURRENT_PLAYER_MARK
    first_one = who_starts_first(tuple_marks)
    
    #позиции игороков
    player_mark = tuple_marks[0]
    robot_mark = tuple_marks[1]
    
    if first_one is player_mark:
        print('Игру начинаете Вы!')
        CURRENT_PLAYER_MARK = player_mark
        move = choose_position(board, player_mark)
        
    elif first_one is robot_mark:
        print('Игру начинает Робот!')
        CURRENT_PLAYER_MARK = robot_mark
        move = robot_position(board, robot_mark)
    return move

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
            
#     board[position] = '\033[91m'+'\033[1m'+'\033[4m'+mark+'\033[0m'
    board[position] = mark
    display_board(board)

    
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
            
#     board[position] = '\033[94m'+'\033[1m'+'\033[4m'+mark+'\033[0m'
    board[position] = mark
    display_board(board)
    

#проверяем на выигрыш игру
def check_if_game_over(board, mark, markers):

    # устанавливаем глобалку winner
    win_boolean_cases = []
    
    #ищем выигрыш по строкам
    for j in range (10):
        for i in range(6):
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+1] == board[j*10+i+2] == board[j*10+i+3] == board[j*10+i+4] == mark)
    
    #ищем выигрыш по столбцам                     
    for j in range (6):
        for i in range(10):
            win_boolean_cases.append(board[j*10+i] == board[j*10+i+10] == board[j*10+i+20] == board[j*10+i+30] == board[j*10+i+40] == mark)                           
    
    #ищем выигрыш по диогонали
    for j in range (6):
        for i in range(6):
            win_boolean_cases.append(board[i*10+j] == board[i*10+j+11] == board[i*10+j+22] == board[i*10+j+33] == board[i*10+j+44] == mark)  
    
    #ищем выигрыш по обратной диогонали
    for j in range (9,3,-1):
        for i in range(9,3,-1):
            win_boolean_cases.append(board[i*10+j] == board[i*10+j-11] == board[i*10+j-22] == board[i*10+j-33] == board[i*10+j-44] == mark)  
    
    if True in win_boolean_cases and markers[0] == mark:
        print(f'Вы проиграли! У вас был "{mark}"')
        return False
    
    elif True in win_boolean_cases and markers[1] == mark:
        print(f'Вы выиграли! У вас был "{mark}"')
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
    
    #данные для доски
    PLAY_BOARD = [str(num) for num in range(0, 101)]
    
    #пустой список для записи всех выигрышей (по вертикали, горизонтали, диогонали)
    win_boolean_cases = []
    
    print('Игра в "Крестики-нолики"')
    
    #отоброжаем доску для игры
    display_board(PLAY_BOARD)

    #выбираем каким игрок хочет начать игру
    CHOOSE_MARKERS = choose_marker()
    
    #рандомно кто-то начинает первым
    the_first_move(PLAY_BOARD, CHOOSE_MARKERS)
    
    game_still_is_going = True
         
    #если игру начал ИГРОК
    if CURRENT_PLAYER_MARK == CHOOSE_MARKERS[0]:
            
        #играем до тех пор, пока кто-то не выиграет либо ничья
        while game_still_is_going:
            robot_position(PLAY_BOARD, flip_player(CURRENT_PLAYER_MARK))
            game_still_is_going = check_if_game_over(PLAY_BOARD, CURRENT_PLAYER_MARK, CHOOSE_MARKERS)
            #игра закочилась
            if game_still_is_going is False:
                break
            
            choose_position(PLAY_BOARD, CURRENT_PLAYER_MARK)

    #если игру начал РОБОТ
    elif CURRENT_PLAYER_MARK == CHOOSE_MARKERS[1]:
        
        #играем до тех пор, пока кто-то не выиграет либо ничья
        while game_still_is_going:
            choose_position(PLAY_BOARD, flip_player(CURRENT_PLAYER_MARK))
            game_still_is_going = check_if_game_over(PLAY_BOARD, flip_player(CURRENT_PLAYER_MARK), CHOOSE_MARKERS)
            #игра закочилась
            if game_still_is_going is False:
                break
            
            robot_position(PLAY_BOARD, CURRENT_PLAYER_MARK)
            




        
    

play_game()


# In[ ]:





# In[ ]:




