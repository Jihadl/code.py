# the use of user defined function 
def sum(a,b):
    x = a+b
    return x
print(sum(12,34))    

'''
def add(*numbers):    # xarguments 
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum

print(add(10,20))
'''

# the use of lambda function 
x = (lambda a,b:a*a + 2*a*b + b*b) (2,4) # single line code 
print(x)


# Map and Filter function
def square(a):
    return a*a

num = [1,2,3,4,5]

result = list(map(square,num))
print(result)

#filtering 
def num3(d):
    return d%2==0

num2 = [1,2,3,4,5]
print(list(filter(num3,num2)))

#result = list(filter(lambda x: x%2==0 ,num2))
#print(result)