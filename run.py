#!/usr/bin/env python3.9

from player import Player

player_obj=Player()
input_list=[" "," "," "," "," "," "," "," "," "]

def show_grid():
    print("\n")
    print(f'  {input_list[0]}  |  {input_list[1]}  |  {input_list[2]}  ')
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(f'  {input_list[3]}  |  {input_list[4]}  |  {input_list[5]}  ')
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(f'  {input_list[6]}  |  {input_list[7]}  |  {input_list[8]}  ')

def check_winner():
    if input_list[0]==input_list[1] and input_list[1]==input_list[2]:
        if input_list[0] != " ":
            return True
    elif input_list[0]==input_list[3] and input_list[3]==input_list[6]:
        if input_list[0] != " ":
            return True
    elif input_list[0]==input_list[4] and input_list[4]==input_list[8]:
        if input_list[0] != " ":
            return True
    elif input_list[1]==input_list[4] and input_list[4]==input_list[7]:
        if input_list[1] != " ":
            return True
    elif input_list[2]==input_list[5] and input_list[5]==input_list[8]:
        if input_list[2] != " ":
            return True
    elif input_list[2]==input_list[4] and input_list[4]==input_list[6]:
        if input_list[2] != " ":
            return True
    elif input_list[3]==input_list[4] and input_list[4]==input_list[5]:
        if input_list[3] != " ":
            return True
    elif input_list[6]==input_list[7] and input_list[7]==input_list[8]:
        if input_list[6] != " ":
            return True
    else:
        return False


def main():

    which_player=True
    is_stalemate=True
    # value_error=False
        
    print("     TIC-TAC_TOE")
    print("This is how the grid looks like")
    print("\n")

    print(" 1   | 2   | 3   ")
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(" 4   | 5   | 6   ")
    print("-"*5+"|"+"-"*5+"|"+"-"*5)
    print(" 7   | 8   | 9   ")   
    print("\n")

    print("     START")
    while len(player_obj.moves_av_list)>0:
        value_error=False
        
        if which_player==True:
            print("\n")
            print("Player 1:")
            print("Available moves:")
            player_obj.show_av_moves()
            show_grid()
            print("Your move:")
            try:
                x=int(input())
            except ValueError:
                value_error=True
                print("******Fatal Mistake: Use numbers 1-9******")
            
            if value_error==False:
                if player_obj.validate_move(x):
                    input_list[x-1]="X"
                    player_obj.move_made(x)
                    which_player=False
                    if check_winner():
                        show_grid()
                        print("\n")
                        print("-----(( PLAYER ONE WINS ))-----")                    
                        print("              END")
                        is_stalemate=False
                        break
                else:
                    print("******Invalid move, try again******")
                    which_player=True
                        
            
        else:
            print("\n")
            print("Player 2:")
            print("Available moves:")
            player_obj.show_av_moves()
            show_grid()
            print("Your move:")
            try:
                x=int(input())
            except ValueError:
                value_error=True
                print("******Fatal Mistake: Use numbers 1-9******")
            
            if value_error==False:
                if player_obj.validate_move(x):
                    input_list[x-1]="O"
                    player_obj.move_made(x)
                    which_player=True
                    if check_winner():
                        show_grid()
                        print("\n")
                        print("-----(( PLAYER TWO WINS ))-----")                    
                        print("              END")
                        is_stalemate=False
                        break
                else:
                    print("******Invalid move, try again******")
                    which_player=False

    if is_stalemate:
        show_grid()
        print("\n")
        print("Stalemate: Cat Game")
        print("     END")
    

if __name__ == "__main__":
    main ()