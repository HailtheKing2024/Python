def countdown(num):

    while num >=0:
        yield num
        num -=1

user = input('Enter number to start countdown:')

numbers = countdown(int(user))

for i in numbers:
    print(i) # Prints numbers withhin the range of the user input and 0.
