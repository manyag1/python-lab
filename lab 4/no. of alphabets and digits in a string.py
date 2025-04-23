def sm():
    c=0
    s=0
    n=input("enter a string")
    for i in n:
        if i.isalpha():
            c+=1
        elif i.isdigit():
            s+=1
    print("no. of alphabets=", c)
    print("no. of digits=", s)
      
sm()    













