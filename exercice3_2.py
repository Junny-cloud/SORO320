
r = 1
avant = (0.9**r)-(1/r)
suivant= (0.9**(r+1))-(1/(r+1))

while  suivant > avant:
    r+=1
    avant = (0.9**r)-(1/r)
    suivant= (0.9**(r+1))-(1/(r+1))
print("La valeur de r ou f(x) est maximal est r =", r) 
