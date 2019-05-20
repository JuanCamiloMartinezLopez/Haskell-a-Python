def Cuadrados(list):
    if list==[ ]:
        return []
    else:
        return [list[0]*list[0]]+Cuadrados(list[1:])

if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9]
    print Cuadrados(l)