f = open(".//day2.txt", "r")

res = 0
for line in f:
    line = line.split()
    opponent = line[0]
    you = line[1]
    score = 0

    # A Rock, B Paper, C Scissors
    # X Rock, Y Paper, Z Scissors

    '''
    if you == "X":
        score += 1
        if opponent == "A":
            score += 3
        elif opponent == "B":
            score += 0
        else: 
            score += 6
    elif you == "Y":
        score += 2
        if opponent == "A":
            score += 6
        elif opponent == "B":
            score += 3
        else: 
            score += 0  
    else:
        score += 3
        if opponent == "A":
            score += 0
        elif opponent == "B":
            score += 6
        else: 
            score += 3
    '''

    # X Lose, Y Draw, Z Win
    if you == "X":
        if opponent == "A":
            score += 3
        elif opponent == "B":
            score += 1
        else: 
            score += 2
    elif you == "Y":
        score += 3
        if opponent == "A":
            score += 1
        elif opponent == "B":
            score += 2
        else: 
            score += 3  
    else:
        score += 6
        if opponent == "A":
            score += 2
        elif opponent == "B":
            score += 3
        else: 
            score += 1
    
    res += score

print(res)