def contrarPares( list):
    if list == []:
        return 0
    else:
        if(list[0]%2==0):
            return 1+contrarPares(list[1:])
        else:
            return 0+contrarPares(list[1:])

if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9]
    print contrarPares(l)