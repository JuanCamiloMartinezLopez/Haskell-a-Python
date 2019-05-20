def invertirlista(List):
    if List==[]:
        return []
    else:
        return  invertirlista(List[1:])+ [List[0]]

if __name__ =="__main__":
    print invertirlista([1,2,3,4,5])