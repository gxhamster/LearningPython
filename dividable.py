# Two numbers
# See which number they are divisble from


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

# Return the number which both nums can be divided from

def divide(num1, num2):
    for div in range(2, num1):
        if num1 % div or num2 % div:
            continue
        else:
            return div
    
print(divide(num1, num2))