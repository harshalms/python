# Given n names and phone numbers, assemble a phone book that maps friends' names to their 
# respective phone numbers. You will then be given an unknown number of names to query your 
# phone book for. For each name queried, print the associated entry from your phone book on 
# a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.
if __name__=='__main__':
    n = int(input())
    s={}
    for i in range(n):
        name, number = input().split()
        phone = int(number)
        s[name]=phone 
    while True:
        try:  # any number of input can be taken
            query = input()
            if query in s:
                print(f"{query}={s[query]}")
            else:
                print("Not found")
        except EOFError:
            break