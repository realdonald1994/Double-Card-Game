def play(m=None,n=None):
    if n  or m is None:
        while True:
            try:
                uinput = input('Input the grid size: ')
                suinput= uinput.split(' ')
                n = int(suinput[0])
                m = int(suinput[1])
            except ValueError:
                print('Invalid input')
                continue
            if n <= 0:
                print('Invalid input')
                continue
            elif m<=0:
                print('Invalid input')
                continue
            break

    grids = [[0 for _ in range(m)] for _ in range(n)]


    user = 1
    print('Current board:')
    print(*grids, sep='\n')

    while True:
        user_input = get_input(user, grids, n, m)
        place_piece(user_input[0], user_input[1],user, grids)
        print('Current board:')
        print(*grids, sep='\n')

        if (check_won(grids, user) or
                check_won(zip(*grids), user) or
                diagcheck_won(grids, user, n) or
                diagcheck_won(grids[::-1], user, n)):
            print('Player', user, 'has won')
            return

        if not any(0 in grid for grid in grids):
            return

        user = 2 if user == 1 else 1


def get_input(user, grids, n, m):
    instr = 'Input a slot player {0} in {1}*{2}: '.format(user, n, m)
    while True:
        try:
            uinput= input(instr)
            suinput = uinput.split(' ')
            user_inputx = int(suinput[0])
            user_inputy = int(suinput[1])
        except ValueError:
            print('invalid input:', user_inputx,user_inputy)
            continue
        if 0 > user_inputx or user_inputx > m+1:
            print('invalid input:', user_inputx)
        elif 0 > user_inputy or user_inputy > n+1:
            print('invalid input:', user_inputy)
        elif grids[user_inputx-1][user_inputy-1] != 0:
            print('slot', user_inputy, 'is full try again')
        else:
            return user_inputx-1,user_inputy-1



def place_piece(user_input0,user_input1, user, grids):
        if not grids[user_input0][user_input1]:
            grids[user_input0][user_input1] = user
            return

def check_won(grids, user):
    sum =0
    for grid in grids:
        for cell in grid:
            if cell==user:
                sum =sum+1
        if sum>=4:
            return True
        else:
            return False


    #return any(all(cell == user for cell in grid) for grid in grids)


def diagcheck_won(grids, user, n):
    sum=0
    for x in range(n):
        if grids[x][x] == user:
            sum= sum+1
    if sum>=4:
        return True
    else:
        return False
    #return all(grids[x][x] == user for x in range(n))


if __name__ == '__main__':
    play()