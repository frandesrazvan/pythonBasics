def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

example_row1 = [' ', ' ', ' ']
example_row2 = [' ', ' ', ' ']
example_row3 = [' ', ' ', ' ']

example_row3.index

def user_choice():
    acceptable_range = range(0, 3)
    within_range = False
    row_column = []

    for i in range(0, 2):
        if i == 0:
            line = 'row'
        else:
            line = 'column'

        choice = 'WRONG'
        while choice.isdigit() == False or within_range == False:
            choice = input(f'Please choose a {line} (0, 1, 2): ')

            # Check if digit
            if choice.isdigit() == False:
                print('Sorry that is not a digit!')

            # Check if within range
            if choice.isdigit():
                if int(choice) in acceptable_range:
                    within_range = True
                else:
                    print('Sorry, you are out of acceptable range (0, 1, 2)')
                    within_range = False

        row_column.append(int(choice))
        i += 1
    
    return row_column

def tic_tac_toe():
    game_on = True

    while game_on:
        display(example_row1, example_row2, example_row3)
        row_column = user_choice()
        
        for row in range(0, 3):



tic_tac_toe()