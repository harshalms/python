string,sub_string=input("Enter string and sub string\n").split(',')
# string='abcdcdc'
# sub_string='cdc'
count=0
# print(len(string))
# z=len(sub_string)
for k in range(0,len(string)):
    if string[k : k+len(sub_string)] == sub_string:
        # print(string[k:k+z])
        count=count+1
print(count)