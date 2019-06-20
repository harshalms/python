name, age, complexion= input('Enter your name, age and complexion\n').split(',') #separate by commas and separate by space if only .split() is used
print(name)
print(age)
print(complexion)
print('your name is',name,'\nyour age is ',age, '\nyour complexion is',complexion)
print(f'Your Name is {name}, your age is {age} and your complexion is {complexion}')
print(r'put always r to print escape sequence like \n \t')