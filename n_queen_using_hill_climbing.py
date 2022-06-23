import random

def Cost(state,n):
    value = 0
    for i in range(n):
        for j in range(i+1,n):
            if state[i]==state[j] or state[i]-state[j]==j-i or state[i]-state[j]==i-j:
                value += 1
    return value

def generate_next_states(state,n):
    next_states = []
    for i in range(n):
        for j in range(n):
            tmp = state[i]
            state[i] = j
            next_states.append(list(state))
            state[i] = tmp
    
    return next_states

def next_better_state(state,n):
    next_states = generate_next_states(state,n)
    heuristic_values_for_next_states = []
    heuristic_value_of_parent_state = Cost(state,n)
    for next_state in next_states:
        heuristic_values_for_next_states.append(Cost(next_state,n))

    minimum_value = heuristic_value_of_parent_state
    next_opt_state = []
    for i in range(len(heuristic_values_for_next_states)):
        if minimum_value > heuristic_values_for_next_states[i]:
            minimum_value = heuristic_values_for_next_states[i]
            next_opt_state = next_states[i]
    
    return next_opt_state

def print_n_queens(state,n):
    for i in range(n):
        for j in range(n):
            if j==state[i]:
                print('1',end=' ')
            else:
                print('0',end=' ')
        print() 
    print()

def generate_random_state(n):
    state = []
    for i in range(n):
        state.append(random.randint(0,n-1))

    return state

def arrange_n_queens(n):
    state = generate_random_state(n)
    
    while(True):
        next_opt_state = next_better_state(state,n)
        if len(next_opt_state)==0:
            if Cost(state,n):
                state = generate_random_state(n)
            else:
                break
        else:
            state = next_opt_state

    return state

def main():
    n = int(input("Enter size of board to place queens : "))
    state = arrange_n_queens(n)
    print_n_queens(state,n)
    #So, Here 1 represents that at this position queen
    #is placed and 0 represents that at this position is empty

main()