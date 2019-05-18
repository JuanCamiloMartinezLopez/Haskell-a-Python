def comprobarListOrd(list):
    if list==[] or len(list)==1:
        return True
    else:
        if(list[0]<=list[1] and comprobarListOrd(list[2:])):
            return True
        else:
            return False

if __name__=="__main__":
    l=[1,2,5,4]
    print comprobarListOrd(l)    