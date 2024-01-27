# 다항식 계산 7x^3 -4x^2 +0x^1 +5x^0 
def printPoly(p_x) :
    term = len(p_x) - 1
    polyStr = "P(x) = "

    for i in range(len(p_x)) :
        coef = p_x[i]

        if coef >= 0 and i > 0 : 
            polyStr += "+"
        polyStr += str(coef) + "x^" +str(term) + " "
        term -= 1
    
    return polyStr

def calcPoly(xVal, p_x) :
    retValue = 0
    term = len(p_x) - 1

    for i in range(len(p_x)) :
        coef = p_x[i]
        retValue += coef * xVal ** term
        term -= 1

    return retValue

px = [7,-4,0,5]

print(printPoly(px))
print(f'값 : {calcPoly(2,px)}')