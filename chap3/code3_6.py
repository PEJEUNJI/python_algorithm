# 특수 다항식의 계산

def printPoly(t_x, p_x) :
    polyStr = "P(x) = "

    for i in range(len(p_x)) :
        term = t_x[i]
        coef = p_x[i]

        if coef >= 0 :
            polyStr += "+"
        
        polyStr += str(coef) + "x^" + str(term) + " "

    return polyStr

def calcPoly(xVal, t_x, p_x) :
    retValue = 0

    for i in range(len(p_x)) :
        term = t_x[i]
        coef = p_x[i]
        retValue += coef * xVal ** term

    return retValue

tx = [300, 20, 0]
px = [7, -4, 5]

print(f'printPoly : {printPoly(tx,px)}')
print(f'calcPoly : {calcPoly(1,tx,px)}')