from cmath import cos
import math,random,copy

def cost(sudoku):
    res = 0
    for row in sudoku:
        for i in range(9):
            for j in range(i+1,9):
                if row[i]==row[j]:
                    res += 1
    
    for col in range(9):
        for i in range(9):
            for j in range(i+1,9):
                if sudoku[i][col]==sudoku[j][col]:
                    res += 1

    return res

def generate_next_states(sudoku):
    next_states = []

    for i in range(9):
        for j in range(9):
            if (j+1)//3==j//3:
                state = copy.deepcopy(sudoku)
                state[i][j],state[i][j+1] = state[i][j+1],state[i][j]
                next_states.append(state)
            if j-1>=0 and (j-1)//3==j//3:
                state = copy.deepcopy(sudoku)
                state[i][j],state[i][j-1] = state[i][j-1],state[i][j]
                next_states.append(state)
            if (i+1)//3==i//3:
                state = copy.deepcopy(sudoku)
                state[i+1][j],state[i][j] = state[i][j],state[i+1][j]
                next_states.append(state)
            if i-1>=0 and (i-1)//3==j//3:
                state = copy.deepcopy(sudoku)
                state[i][j],state[i-1][j] = state[i-1][j],state[i][j]
                next_states.append(state)

    return next_states

def print_sudoku(sudoku):
    print()
    for row in sudoku:
        for i in row:
            print(i,end=' ')
        print()
    print()

def is_this_state_good(delta,temperature):
    eps = 1e-9
    if temperature<eps:
        return False

    p = math.exp(delta/temperature)

    random_p = random.random()

    if random_p <= p:
        return True
    else:
        return False

def solve_soduko(sudoku):
    temperature = 10000
    reducing_factor = 0.999

    current_state = sudoku
    while True:
        if cost(current_state)==0:
            return current_state

        next_states = generate_next_states(current_state)
        
        good_state_found = False
        
        mn = cost(current_state)

        for state in next_states:
            mn = min(mn,cost(state))

        if mn < cost(current_state):
            good_state_found = True

            for state in next_states:
                if cost(state)==mn:
                    current_state = state
                    break
        
        if good_state_found==False:
            for state in next_states:
                if is_this_state_good(cost(current_state)-cost(state),temperature):
                    temperature*=reducing_factor
                    current_state = state
                    break

        if good_state_found==False:
            return current_state



def fill_sudoku(sudoku):
    for i in range(3):
        for j in range(3):
            for num in range(9):
                ok = False
                for x in range(3):
                    for y in range(3):
                        if sudoku[3*i+x][3*j+y]==num+1:
                            ok = True
                
                if ok == False:
                    for x in range(3):
                        for y in  range(3):
                            if sudoku[3*i+x][3*j+y]==0 and ok==False:
                                sudoku[3*i+x][3*j+y] = num+1
                                ok = True
    return sudoku


def main():
    sudoku = []
    for i in range(9):
        row = [int(item) for item in input().split()]  
        sudoku.append(row)
    
    sudoku = fill_sudoku(sudoku)
    sudoku = solve_soduko(sudoku)
    print_sudoku(sudoku)

main()