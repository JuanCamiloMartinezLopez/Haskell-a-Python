def MayorList(list):
    if len(list)==1:
        return list[0]
    else:
        if(list[0]>MayorList(list[1:])):
            return list[0]
        else:
            return MayorList(list[1:])

if __name__=="__main__":

    list=[1,3,100,2,4,8]
    print MayorList(list)