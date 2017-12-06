# -*- coding: utf-8 -*-
# working with python 2.7

import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board):
    j = 8
    m = 9
    for i in range(1,4):
        number = [ 1,2,3,4,5,6,7,8,9]
        print('+---------------------------+')
        print('|'+str(number[j-2])+'        |'+str(number[j-1])+'       |'+str(number[j])+'       |')
	print('|    '+str(board[m-2])+'    '+'|    '+str(board[m-1])+'   '+'|   '+str(board[m])+'    |' )
	print('|         |        |        |')
        j -=3
        m -=3
    print('+---------------------------+\n')
    
def choose_first():
    
    x = random.randint(0,1)
    if x is 0:
        string = "Παίκτης 1"
    elif x is 1:
        string = "Παίκτης 2"
    return string

def display_score(score):
    for i in score:
        
        print i, score[i]

def place_marker(board, marker, position):
    

    board[position] = str(marker)
      
def win_check(board,mark):
    check = False
    
    
    
    
    test1 = board[1]+board[2]+board[3]
    test2 = board[4]+board[5]+board[6]
    test3 = board[7]+board[8]+board[9]
    if test1 == mark+mark+mark:
        check = True
    elif test2 == mark+mark+mark:
        check = True
    elif test3 == mark+mark+mark:
        check = True
    #Ελεγχος για καθετες τριλιζες
    test4 = board[1]+board[4]+board[7]
    test5 = board[2]+board[5]+board[8]
    test6 = board[3]+board[6]+board[9]
    if test4 == mark+mark+mark:
        check = True
    elif test5 == mark+mark+mark:
        check = True
    elif test6 == mark+mark+mark:
        check = True
    #Ελεγχος για διαγωνιες τριλιζες
    test7 = board[1]+board[5]+board[9]
    test8 = board[7]+board[5]+board[3]

    if test7 == mark+mark+mark:
        check = True
    elif test8 == mark+mark+mark:
        check = True

    #Επιστροφη ελεγχου
    return check

def board_check(board):
    check = True
    for i in range(1,10):
        if board[i] is ' ':
            check = False
            break
    return check
 
def player_choice(board, turn):
        
    while True:
        #πρεπει να μπει input αν ο compiler einai python 3
        choice = raw_input("Διάλεξε απο τη θέση 1 έως 9 για να παίξεις: ")
        if choice.isalpha() is True:
            print("Αυτο που εισήγαγες δεν είναι σωστό…Προσπαθησε να εισάγεις εναν αριθμο \nαπο το 1 εως το 9 για να επιλέξεις θέση!!!!")
        #na alaksw ligo ta inputs apo katw tou xrhsth
        elif choice.isdigit() is True:
            c = int(choice)
            if c in range(1,10) and board[c] == ' ':
                break
            else:
                print("Αυτή η θέση είναι ήδη καλυμμένη…Παρακαλώ διαλέξτε μία άλλη θέση!!\n")
        
        else:
            continue
    return c

def replay():
    decision = False
    choice = raw_input('Αν θες να παίξεις ξανά γράψε “play” ,αλλιώς πάτα “enter” για να τερματιστεί το παιχνίδι:')
    if ( choice == 'play'):
        decision = True
    return decision
        

def next_player(turn):
    if turn == 'Παίκτης 1':
        turn = 'Παίκτης 2'
    elif turn == 'Παίκτης 2':
        turn = 'Παίκτης 1'
    return turn

def main():
    score = {} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ')
    for t in range(10):
        flush = 'True'
        print(".", flush)
        time.sleep(0.2)
    print()
    # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    turn = choose_first() 
    print("\nΟ " + turn + ' παίζει πρώτος.')
    # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    first = turn
    print(turn)
    game_round = 1 # γύρος παιχνιδιού
    while True:
        # Καινούργιο παιχνίδι
        # Δημιουργία λίστας 10 στοιχείων βλέπε μάθημα 2 σελ.7 σημειώσεων
        theBoard = [' '] * 10 
        # Αφήστε το πρώτο στοιχείο δηλαδή το theBoard[0] κενό έτσι ώστε 
        # το index να αντιστοιχεί στην ονοματοδότηση των τετραγώνων 
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            # ο παίκτης turn επιλέγει θέση
            position = player_choice(theBoard, turn) 
            # τοποθετείται η επιλογή του
            place_marker(theBoard, marker[turn], position) 
            if win_check(theBoard, marker[turn]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
            elif board_check(theBoard): 
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            turn = next_player(first) 
            first = turn
main()
