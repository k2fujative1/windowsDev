##Author: Daniel Brown
##Purpose: Shows the traditional fizzBuzz as a python program

count = 1
while count <101:
    if count % 15 == 0:
        print ('FizzBuzz')
    elif count % 3 == 0:
        print ('Fizz')
    elif count % 5 == 0:
        print ('Buzz')
    else:
        print (count)
    count += 1
