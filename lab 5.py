#1
age = int(input('Input your age:'))
if age<20:
    print('You are too young... for now...');
elif age<50:
    print('You are just the right age...')
elif age<100:
    print('You are too old!')
else:
    print('You lie... you will suffer the consequences. It is inevitable.')
#2
x=10
if 15>x>5:
    print('inside!')
elif x>15:
    print('outside')
else:
    print('outside')
#3-FizzBuzz challenge
for a in range(1,101):
    b = 0
    if a%3 == 0 and a%5==0:
        print('Fizz', end='')
        b+=1
    elif a%3==0:
        print('Fizz')
    if a%5 == 0:
        print('Buzz')
        b+=1
    if b==0 and (b+2%5==0 or b+2%3==0) and (a%3!=0 and a%5!=0):
        print('\n'+str(a),end = '')
    elif(a%3!=0 and a%5!=0):
        print(a)
#4
listOfLists = [['a','b','c',],['d','e','f'],['g','h','i']]
print('  0 1 2')
print(' +-+-+-+')
x = 0
for a in listOfLists:
    print(str(x)+'|', end = '')
    for b in a:
        print(b,end = '|')
    print('\n +-+-+-+')
    x+=1
#5-misunderstood and accidentally created bingo game
listOfLists = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
while True:
    print('  0 1 2')
    print(' +-+-+-+')
    x = 0
    thing=0
    for a in listOfLists:
        print(str(x)+'|', end = '')
        for b in a:
            print(b,end = '|')
        print('\n +-+-+-+')
        x+=1
    while True:
        userInputX = input('Enter x coordinate:')
        userInputY = input('Enter a y coordinate:')
        if listOfLists[int(userInputY)][int(userInputX)]==' ':
            listOfLists[int(userInputY)][int(userInputX)]='X'
            break
    for t in listOfLists:
        if t[0]==t[1]==t[2]!=' ':
            thing+=1
    for t in range(0,3):
        if listOfLists[0][t]==listOfLists[1][t]==listOfLists[2][t]!=' ':
            thing+=1
    if thing!=0:
        break
print('  0 1 2')
print(' +-+-+-+')
x = 0
thing=0
for a in listOfLists:
    print(str(x)+'|', end = '')
    for b in a:
        print(b,end = '|')
    print('\n +-+-+-+')
    x+=1
print('BINGO!')
#here begins the real #5
listOfLists = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
print('  0 1 2')
print(' +-+-+-+')
x = 0
thing=0
for a in listOfLists:
    print(str(x)+'|', end = '')
    for b in a:
        print(b,end = '|')
    print('\n +-+-+-+')
    x+=1
userInputX1, userInputY1 = [int(x) for x in input("Enter first coordinate as 'x,y' ").split(',')]
userInputX2, userInputY2 = [int(x) for x in input("Enter second coordinate as 'x,y' ").split(',')]
if userInputX2 == userInputX1:
    for a in range(userInputY1,userInputY2+1):
        listOfLists[int(a)][int(userInputX1)] = 'X'
else:
    for a in range(userInputX1,userInputX2+1):
        listOfLists[int(userInputY1)][int(a)] = 'X'
print('  0 1 2')
print(' +-+-+-+')
x = 0
thing=0
for a in listOfLists:
    print(str(x)+'|', end = '')
    for b in a:
        print(b,end = '|')
    print('\n +-+-+-+')
    x+=1
