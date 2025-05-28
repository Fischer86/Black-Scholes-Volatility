from BlackScholes import BlackScholes

def ImpliedVolatility(S, K, T, r, Cm, option='C', tol=1e-6):
    sMin = 1e-5
    sMax = 5.0
    max_iter = 100

    for i in range(max_iter):
        sMid = (sMin + sMax) / 2
        price = BlackScholes(S, K, T, r, sMid, option)

        if abs(price - Cm) < tol:
            return sMid

        if price > Cm:
            sMax = sMid
        else:
            sMin = sMid

    return sMid
