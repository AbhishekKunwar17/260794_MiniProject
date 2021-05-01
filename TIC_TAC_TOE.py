import random
board=[i for i in range(0,9)]
user, comp = '',''

moves=((1,7,3,9),(5,),(2,4,6,8))

win=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))

tab=range(1,10)
def board_create():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
def sel_ch():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars
def can_turn(brd, user, turn):
    if turn in tab and brd[turn-1] == turn-1:
        return True
    return False
def can_win(brd, user, turn):
    places=[]
    x=0
    for i in brd:
        if i == user: places.append(x);
        x+=1
    win=True
    for tup in win:
        win=True
        for ix in tup:
            if brd[ix] != user:
                win=False
                break
        if win == True:
            break
    return win
def make_turn(brd, user, turn, undo=False):
    if can_turn(brd, user, turn):
        brd[turn-1] = user
        win=can_win(brd, user, turn)
        if undo:
            brd[turn-1] = turn-1
        return (True, win)
    return (False, False)

def comp_turn():
    turn=-1

    for i in range(1,10):
        if make_turn(board, comp, i, True)[1]:
            turn=i
            break
    if turn == -1:

        for i in range(1,10):
            if make_turn(board, user, i, True)[1]:
                turn=i
                break
    if turn == -1:

        for tup in moves:
            for mv in tup:
                if turn == -1 and can_turn(board, comp, mv):
                    turn=mv
                    break
    return make_turn(board, comp, turn)
def exist():
    return board.count('X') + board.count('O') != 9
user, comp = sel_ch()
print('user is [%s] and comp is [%s]' % (user, comp))
result='%%% Deuce ! %%%'
while exist():
    board_create()
    print('#Make your turn ! [1-9] : ', end='')
    turn = int(input())
    turnd, won = make_turn(board, user, turn)
    if not turnd:
        print(' >> Invalid number ! Try again !')
        continue

    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif comp_turn()[1]:
        result='=== You lose ! =='
        break;
board_create()
print(result)
