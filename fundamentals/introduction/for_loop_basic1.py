#Basic Loop
for i in range(151):
    print(i)

#Multiples of 5
for i in range(151):
    if not i%5:
        print(i)

#Counting, the Dojo Way
for i in range(1, 101):
    if not i%10:
        print("Coding Dojo")
    elif not i%5:
        print("Coding")
    else:
        print(i)

#Whoa, that suckers huge
sum = 0
for i in range(500001):
    sum += i
print(sum)

#Countdown by fours
for i in range(2018, 0, -4):
    print(i)

#flexible counter
def counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum):
        if not i%mult:
            print(i)
counter(1, 105, 7)