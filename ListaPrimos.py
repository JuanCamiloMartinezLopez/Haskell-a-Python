def EsDivisible(divisor, dividendo):
    return divisor%dividendo==0

def Divisores(l):
    return [x for x in range(1,l+1) if EsDivisible(l,x) ]

def EsPrimo(n):
    return len(Divisores(n))<=2

def listaPrimos(a):
    return [x for x in range(1,a+1)if EsPrimo(x)]

if __name__=="__main__":
    
    print "ingrese el numero de limite:\n"
    print listaPrimos(n)