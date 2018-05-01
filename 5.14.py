a= input()
b= input()
c= input()
n= input()

def check_fermat (a,b,c,n):
    if a**n+b**n==c**n:
        print("fermat was wrong")
    elif n<2:
        print ("fermat was wrong")
    else:
        print ("no that doesnt work")


check_fermat(a,b,c,n)


#5.3
s1=input()
s2=input()
s3=input()


def is_triangle(s1,s2,s3):
    if s1+s2<s3:
        print ("no triangle")
    elif s2+s3<s1:
        print ("no triangle")
    elif s3+s1<s2:
        print ("no triangle")
    else:
        print ("triangle possible")


is_triangle(s1,s2,s3)

#5.4
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

    recurse(3, 0)
    return (x2-x1)**2