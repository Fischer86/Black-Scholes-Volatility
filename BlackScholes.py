import math
from scipy.stats import norm

def BlackScholes(S, K, T, r, sigma, option = 'C'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option == 'C':
        call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
        return call_price
    elif option == 'P':
        put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return put_price
    else:
        raise ValueError("The option must be 'C' for call or 'P' for put.")

import math
from scipy.stats import norm

def ComputeGreeks(S, K, T, r, sigma, option='C'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    gamma = norm.pdf(d1) / (S * sigma * math.sqrt(T))
    vega = S * norm.pdf(d1) * math.sqrt(T)

    if option == 'C':
        delta = norm.cdf(d1)
        theta = (- (S * sigma * norm.pdf(d1)) / (2 * math.sqrt(T))
                 - r * K * math.exp(-r * T) * norm.cdf(d2))
        rho = K * T * math.exp(-r * T) * norm.cdf(d2)

    elif option == 'P':
        delta = norm.cdf(d1) - 1
        theta = (- (S * sigma * norm.pdf(d1)) / (2 * math.sqrt(T))
                 + r * K * math.exp(-r * T) * norm.cdf(-d2))
        rho = -K * T * math.exp(-r * T) * norm.cdf(-d2)

    else:
        raise ValueError("The option must be 'C' for call or 'P' for put.")
    
    theta_daily = theta / 365

    return {
        'Delta': delta,
        'Gamma': gamma,
        'Vega': vega,
        'Theta': theta_daily,
        'Rho': rho
    }
