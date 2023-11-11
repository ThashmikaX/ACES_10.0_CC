def create_pattern(n):
    j = 1
    k = n*2-2
    for i in range(n):
        print(" "*(n+1) + " "*(n-i-1)+ "*"*j + " "*(n*2) + " "*(k*2) + "*"*j)
        j+=3
        k-=2
    upperrows, lowerrows = 0,0
    if n%2 == 0:
        upperrows = n//2 #2
        lowerrows = n//2 #3
    else:
        upperrows = n//2
        lowerrows = n-upperrows

    for i in range(upperrows):
        b = (j-3)*2 + n*2
        print(" "*(n+1) + "*"*(b))

    for i in range(lowerrows):
        print(" " * (n + 1) + "*" * n +" " * n + "*"*(b-4*n) + " " * n + "*" * n)
    upnose = (b-4*n)
    nose = n*2
    z=0
    nosehair = lowerrows//2 #1
    downnose = lowerrows - nosehair


    #nose hair
    B = (upnose-nose)
    for i in range(nosehair):

        print(" "*z +"*"*n + " " + "*"*(n*2+(B//2)) + " "*nose + "*"*(n*2+(B//2)) + " " +"*"*n)
        nose-=2
        print(" "*(z+n+2) + "*"*(n*2+(B//2)) + " "*(nose) + "*"*(n*2+(B//2)) )
        nose-=2
        z += 2
    dowsnosestar = ((nose+2) - 1)//2
    #down nose
    C = (dowsnosestar+(n*2+(B//2))-1)
    for i in range(downnose):
        print(" " * z + "*" * n + " " + "*" * C + " "*2 + "*" * C + " " + "*" * n)
        z += 2
        C-=1

        if (downnose - i) != 1:
            print(" " * (z + n) + "*" * C + " " * 2 + "*" * C)
            C -= 1
        else:
            if n%2 == 0:
                print(" " * (z + n) + "*" * C + " " * 2 + "*" * C)
                C -= 1

    downStart = (z + n -1)
    q=0
    g = C * 2 + 4
    for i in range(n):
        if n%2==0:
            print(" " * (downStart+1 + q) + "*" * (g))
            q -= 1
            g += 2

        else:
            print(" " * (downStart+q) + "*" * (g))
            q-=1
            g+=2


if __name__ == "__main__":
    n = int(input())
    create_pattern(n)

