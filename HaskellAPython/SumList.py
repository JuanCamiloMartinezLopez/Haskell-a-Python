def SumaLista(List):
    if(len(List)==1):
        return List[0]
    else:
        return List[0]+ SumaLista(List[1:])

if __name__=="__main__":
    Lista=[0,1,2,3,4,5,6,7,8,9]
    print " lista:\n"
    print Lista 
    print SumaLista(Lista)