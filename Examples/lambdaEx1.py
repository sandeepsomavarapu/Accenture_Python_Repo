# Python Lambda Example
 
num = lambda: True
 
print(num())

#lambda sum with argument
print('--lambda with argumnet--')
num = lambda x: x + 5
 
#calling lambda function
print(num(10))

#lambda expression with two arguments:
print('--x,y--')
add = lambda x, y : x + y
 
print(add(10, 20))

# Python Lambda Example
print('--default values output--') 
add = lambda x = 10, y = 20, z = 30 : x + y + z
print(add()) # 10 + 20 + 30
 
multi = lambda x = 10, y = 20, z = 30 : x * y * z
print(multi()) # 10 * 20 * 30
 
sub = lambda x = 10, y = 45: y - x
print(sub()) # 45 - 10