x=5

match x:

    case 0:
        print("x is zero")
    case 4 if x%2==0:
        print("x is even")

    case _ if x%2!=0:
        print("x is odd")