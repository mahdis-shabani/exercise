import random

def is_started(dice_of_first_player,dice_of_second_player,first_player_move,second_player_move):
    if first_player_move>1 or second_player_move>1:
          return True
    if dice_of_first_player==6 or dice_of_second_player==6:
            return True
    return False
    
def is_finished(first_player_move,second_player_move):
    if first_player_move<100 and second_player_move<100:
          return False
    return True
    
def create_board():
      return [ ["$","O","O","O","O","O","O","#","O","O"],
            ["O","O","O","O","#","O","O","O","O","O"],
            ["$","O","O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O","O","O"],
            ["O","O","O","O","#","O","O","O","O","O"],
            ["O","O","O","O","O","O","O","O","O","O"],
            ["$","O","O","O","O","O","O","O","O","#"],
            ["O","O","O","O","O","O","O","O","$","H"]]

def get_next_movement():
    return random.randint(1,6)

def is_snake_bite(player_move):
    if player_move==99:
        return True
    if player_move==81:
          return True
    return False
    
def is_ladder(player_move):
    if player_move==15:
        return True
    if player_move==3:
        return True
    return False

def location(player_move):
    line=int(player_move/10)
    coulmn=player_move%10
    return line,coulmn

def one_house(first_player_move,second_player_move):
    if first_player_move==second_player_move:
            return True 
    return False
        
        
def main():
    first_player_move=1
    second_player_move=1
    check_1=True
    check_2=True
    number_of_board_displays=0
    dice_of_second_player=get_next_movement()
    dice_of_first_player=get_next_movement()
    print(f"dice of player_1:{dice_of_first_player}")
    print(f"dice of player_2:{dice_of_second_player}")

    if is_started(dice_of_first_player,dice_of_second_player,first_player_move,second_player_move)==True:
        
        if is_finished(first_player_move,second_player_move)==False:
            while True:
                list=create_board()
                len_2=len(list)-1
                counter=0

                if first_player_move==1 and check_1==True and number_of_board_displays>0:
                    dice_of_first_player=get_next_movement()
                    print(f"dice_of_first_playet:{dice_of_first_player}")
                if second_player_move==1 and check_2==True and number_of_board_displays>0:
                    dice_of_second_player=get_next_movement()
                    print(f"dice_of_second_player:{dice_of_second_player}")
                
                if (dice_of_first_player==6 or first_player_move>1) and check_1==True:
                    player_1="*"
                    dice_of_first_player=get_next_movement()
                    if dice_of_first_player==6:
                        check_2=False
                    else:
                        check_2=True
                    print(f"dice of first player:{dice_of_first_player}")
                    first_player_move+=dice_of_first_player

                    if first_player_move==3:
                        first_player_move=65
                    if first_player_move==15:
                          first_player_move=90
                    if first_player_move==99:
                          first_player_move=10
                    if first_player_move==81:
                          first_player_move=21
                          
                    print(f"first_player_move:{first_player_move}")
                    if first_player_move>100:
                        first_player_move-=dice_of_first_player
                        print(f"first_player_move:{first_player_move}")
                    if one_house(first_player_move,second_player_move):
                        player_1="@"
                        player_2="@"  
                                        
                    line,coulmn=location(first_player_move)
                    if coulmn==0:
                        if line==10:
                            list[line-1][coulmn-1]=player_1
                        elif first_player_move==10:
                            list[line-1][coulmn]=player_1
                        elif coulmn==0:
                            list[line-1][coulmn-1]=player_1
                    elif coulmn!=0:

                            if is_ladder(first_player_move)==True:
                                        list[6][4]=player_1
                                        print(f"first_player_move:{first_player_move}")

                            elif is_snake_bite(first_player_move)==True:
                                        list[0][0]=player_1
                                        print(f"first_player_move:{first_player_move}")
                            elif is_ladder(first_player_move)==True:
                                list[8][9]=player_1
                                print(f"first_player_move:{first_player_move}")

                            elif is_snake_bite(first_player_move)==True:
                                        list[2][0]=player_1
                                        print(f"first_player_move:{first_player_move}")

                            elif is_snake_bite(first_player_move)==False and is_ladder(first_player_move)==False:
                                        if line==0:
                                            list[line][coulmn*-1]=player_1
                                        else:
                                            list[line][coulmn-1]=player_1
                                        
                if (dice_of_second_player==6 or second_player_move>1) and check_2==True:
                    player_2="+"
                    dice_of_second_player=get_next_movement()
                    if dice_of_second_player==6:
                        check_1=False
                    else:
                        check_1=True
                    
                    print(f"dice of second player:{dice_of_second_player}")
                    second_player_move+=dice_of_second_player
                          
                    if second_player_move==3:
                        second_player_move=65
                    if second_player_move==15:
                        second_player_move=90
                    if second_player_move==99:
                        second_player_move=10
                    if second_player_move==81:
                        second_player_move=21

                    print(f"second_player_move:{second_player_move}")
                    if one_house(first_player_move,second_player_move)==True:
                        player_1="@"
                        player_2="@"  
        
                    if second_player_move>100:
                        second_player_move-=dice_of_second_player
                        print(f"second_player_move:{second_player_move}")

                    line,coulmn=location(second_player_move)

                    if coulmn==0:
                        if line==10:
                            list[line-1][coulmn-1]=player_2
                        elif second_player_move==10:
                            list[line-1][coulmn]=player_2
                        elif coulmn==0:
                            list[line-1][coulmn-1]=player_2
                    elif coulmn!=0:
                        if is_ladder(second_player_move)==True:
                                        list[6][4]=player_2
                                        print(f"second_player_move:{second_player_move}")

                        elif is_snake_bite(second_player_move)==True:
                                        list[0][0]=player_2
                                        print(f"second_player_move:{second_player_move}")

                        elif is_snake_bite(second_player_move)==True:
                                        list[2][0]=player_2
                                        print(f"second_player_move:{second_player_move}")

                        elif is_ladder(second_player_move)==True:
                                    list[8][9]=player_2
                                    print(f"second_player_move:{second_player_move}")

                        elif is_ladder(second_player_move)==False and is_snake_bite(first_player_move)==False:
                                        if line==0:
                                            list[line][coulmn*-1]=player_2
                                        else:
                                            list[line][coulmn-1]=player_2
                                        
                while counter<len(list):
                    len_1=len(list)-1
                    for item in list:
                            print(list[len_2][len_1],end='  ')
                            len_1-=1

                    counter+=1
                    len_2-=1
                    print("\n")

                if first_player_move==100:
                        print("\n")
                        print("player_1 won this game")
                        exit()
                if second_player_move==100:
                    print("\n")
                    print("player_2 won this game")
                    exit()

                new_set=input("enter 'c' for continue:")
                number_of_board_displays+=1

                if new_set=='c':
                    continue
                else:
                    exit()


main()
    




            
            



                    

         
         
             

              
            

    

        






