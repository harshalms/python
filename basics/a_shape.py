NAME = "HARSHAL SHEDOLKAR"

for i in range(7):
    for j in range(5):
        # if (j==0 and i>0) or (j==4 and i>0) or (j%4!=0 and i==0) or (j%4!=0 and i==3):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and j%4!=0):
            print('*', end="")
        else:
            print(end=" ")
    print()



def foo(name):
    print("My name is ", name)

def bar(fun, name):
    fun(name)


def foobar():
    foo("Harshal")
    fun = foo
    bar(fun, "Rajesh")


foobar()