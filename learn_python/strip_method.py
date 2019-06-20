#strip method is used to remove gaps in the string
# name.lstrip() to remove left space
# name.rstrip() to remove right spaces.
# name.strip() to remove both left and right spaces.
# we can use replace, name.replace(" ","") this replaces space" " with no space"" 
# using replace we can find something and can replace with anything.
string='He is is is a legend'
print(string.replace('is','was',1)) # Here only one 'is' is being replaced by 'was'.
print(string.find('legend')) # finds the starting position of legend
print(string.index('d'))