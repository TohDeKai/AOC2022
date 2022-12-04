f = open(".//day1.txt", "r")

count = 0
biggest = 0
biggest2 = 0
biggest3 = 0

# O(n) solution
for line in f:
    if line == "\n":
        if count > biggest:
            biggest3 = biggest2
            biggest2 = biggest
            biggest = count      
        else:
            if count > biggest2:
                biggest3 = biggest2
                biggest2 = count            
            else:
                if count > biggest3:
                    biggest3 = count
        count = 0
    else:
        count += int(line)

print(biggest + biggest2 + biggest3)

#O(nlogn) solution - might look cleaner, just sort and select first 3 elements