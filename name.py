# name = int(input())

# # print the name along with Hello
# print('Hello {0}'.format(name))

numArray = map(int, input().split()) # Get the input

# print(numArray)
sum_integer = 0
# write your logic to add these 4 numbers here
for i in numArray:
    sum_integer+=i



print(sum_integer) # Print the sum