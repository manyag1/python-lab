a=int(input("enter no.1"))
b=int(input("enter no.2"))
c=int(input("enter no.3"))
def ls(a,b,c):
    
    if a>b and a>c:
        if b>c:
            print(a, " is the largest and", c, " is the smallest")

    elif a<b and b>c:
        if a<c:
            print(b, " is the largest and", a, " is the smallest")

    elif c>a and c>b:
        if b<a:
            print(c, " is the largest and", b, " is the smallest")

ls(a,b,c)
    

