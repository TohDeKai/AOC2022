f = open(".//day3.txt", "r")

res = 0
# Part 1
'''
for line in f:
    line = line.strip()
    n = len(line)
    n = int(n/2)
    first = line[:n]
    last = line[n:]
    letters = {}

    pointer = 0
    
    shared = []

    while pointer < n:
        if first[pointer] not in letters:
            letters[first[pointer]] = 1
        pointer += 1

    pointer = 0

    while pointer < n:
        if last[pointer] in letters and letters[last[pointer]] > 0:
            letters[last[pointer]] -= 1
            shared.append(last[pointer])
        pointer += 1
    
    for item in shared:
        if item.isupper():
            priority = ord(item) - ord('A') + 27
        else:
            priority = ord(item) - ord('a') + 1
        res += priority
    
    print(priority)
'''
counter = 0
letters = {}
for line in f:
    letters_line = {}
    counter += 1
    line = line.strip()
    pointer = 0
    while pointer < len(line):
        if line[pointer] not in letters and line[pointer] not in letters_line:
            letters[line[pointer]] = 1
            letters_line[line[pointer]] = 1
        elif line[pointer] in letters and line[pointer] not in letters_line:
            letters[line[pointer]] += 1
            letters_line[line[pointer]] = 1
        pointer += 1

    if counter == 3:
        print(letters)
        for k,v in letters.items():
            if v == 3:
                if k.isupper():
                    priority = ord(k) - ord('A')+ 27
                else:
                    priority = ord(k) - ord('a') + 1
        res += priority
        counter = 0
        letters = {}
    
    


# Part 2
print(res)