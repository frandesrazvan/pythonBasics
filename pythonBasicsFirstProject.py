def display_board(board):
    # clear board
    print('\n' * 100)
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('- - -')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('- - -')
    print(board[1] + '|' + board[2] + '|' + board[3])
        
def choose_team():
    marker = ''
    
    # KEEP ASKING PLAYER 1 to choose X or 0
    while marker != 'x' and marker != '0':
        marker = input('You are player 1, choose X or 0: ')
        
    player1 = marker
    
    if player1 == 'x':
        player2 = '0'
    else: player2 = 'x'
    
    return [('Player 1', player1), ('Player 2', player2)]
        
def game(board, p1, p2):
    display_board(board)
    game_status = 'ONGOING'
    current_player = p1
    p1_winnings = 0
    p2_winnings = 0
    
    while game_status != 'OVER':
        print(f'{current_player[0]} turn')
        position = int(input('Choose a position (1-9): '))
    
        if board[position] == ' ':
            board[position] = current_player[1][0]
        else:
            display_board(board)
            print('Position already in use, try another one')
            continue
        
        display_board(board)

        # check if there is a winner
        if board[7] == board[8] == board[9] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[4] == board[5] == board[6] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[1] == board[2]== board[3] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[1] == board[4] == board[7] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[2] == board[5] == board[8] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[3] == board[6] == board[9] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[1] == board[5] == board[9] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
        elif board[3] == board[5] == board[7] == current_player[1][0]:
            game_status = 'OVER'
            print(f'And the winner is {current_player[0]}')
            
        # check if there is a tie
        if (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ') and game_status == 'ONGOING':
            game_status = 'OVER'
            display_board(board)
            print('There is a tie')

        # if the game is over, ask if they want to play again
        if game_status == 'OVER':
            if current_player[0] == 'Player 1':
                p1_winnings += 1
            else:
                p2_winnings += 1
                
            print('\n\n### Current score ###')
            print(f'{p1[0]} [{p1_winnings}] - [{p2_winnings}] {p2[0]}\n\n')
            
            play_again = ''
            while play_again != 'y' and play_again != 'n':
                play_again = input('Do you want to play again?(y/n): ')
                
            if play_again == 'y':
                game_status = 'ONGOING'
                board = [' '] * 10
                display_board(board)
        
        # if game is not over, change player turn
        if current_player[0] == 'Player 1':
            current_player = p2
        else:
            current_player = p1    
    
test_board = [' '] * 10
player1_marker, player2_marker = choose_team()
print(player1_marker[0])
print(player2_marker[0])
game(test_board, player1_marker, player2_marker)