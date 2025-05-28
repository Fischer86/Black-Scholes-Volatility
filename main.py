import argparse
from BlackScholes import BlackScholes, ComputeGreeks
from ImpliedVol import ImpliedVolatility

def main():
    parser = argparse.ArgumentParser(description="Black-Scholes Option Calculator")

    parser.add_argument('--mode', type=str, required=True, choices=['price', 'greeks', 'iv'],
                        help='Choose a mode: price, greeks, or iv (implied volatility)')
    parser.add_argument('--S', type=float, required=True, help='Spot price of the underlying asset')
    parser.add_argument('--K', type=float, required=True, help='Strike price')
    parser.add_argument('--T', type=float, required=True, help='Time to maturity (in years)')
    parser.add_argument('--r', type=float, required=True, help='Risk-free interest rate (decimal)')
    parser.add_argument('--option', type=str, choices=['C', 'P'], required=True, help='Option type: C (Call) or P (Put)')
    parser.add_argument('--sigma', type=float, help='Volatility (required for price and greeks)')
    parser.add_argument('--Cm', type=float, help='Market price of the option (required for implied volatility)')

    args = parser.parse_args()

    if args.mode == 'price':
        if args.sigma is None:
            raise ValueError("Volatility (--sigma) is required to compute price.")
        price = BlackScholes(args.S, args.K, args.T, args.r, args.sigma, args.option)
        print(f"Option price ({args.option}): {round(price, 4)} €")

    elif args.mode == 'greeks':
        if args.sigma is None:
            raise ValueError("Volatility (--sigma) is required to compute Greeks.")
        greeks = ComputeGreeks(args.S, args.K, args.T, args.r, args.sigma, args.option)
        print("Greeks:")
        for name, value in greeks.items():
            print(f"{name}: {round(value, 6)}")

    elif args.mode == 'iv':
        if args.Cm is None:
            raise ValueError("Market price (--Cm) is required for implied volatility.")
        iv = ImpliedVolatility(args.S, args.K, args.T, args.r, args.Cm, args.option)
        print(f"Implied Volatility: {round(iv * 100, 4)} %")

if __name__ == "__main__":
    main()
