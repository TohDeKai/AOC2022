f = open(".//day4.txt", "r")

res1 = 0

res2 = 0

for line in f:
    line = line.split(',')

    first = line[0]
    first = first.split('-')
    first_start = int(first[0])
    first_end = int(first[1])

    second = line[1]
    second = second.split('-')
    second_start = int(second[0])
    second_end = int(second[1])


    if first_start >= second_start and first_end <= second_end or second_start >= first_start and second_end <= first_end:
        res1 += 1

    if second_start <= first_end and second_end >= first_start or first_start <= second_end and first_end >= second_start:
        res2 += 1

print(res1)
print(res2)