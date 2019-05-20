def Comparar( FList, SList):
    if(FList==SList):
        return True
    else:
        return False

if __name__=="__main__":
    
    L1=[1,2,3,4]
    L2=[1,2,3,4]
    L3=[1,2,4,3]

    print Comparar(L1,L2)
    print Comparar(L1,L3)