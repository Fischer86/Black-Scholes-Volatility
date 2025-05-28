# Black-Scholes option pricing tool

A simple Python tool to compute:
- European option prices (Call & Put)
- Option Greeks
- Implied volatility

## 🧠 Theory

This script is based on the [**Black-Scholes**](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model) model, an essential tool in quantitative finance. It prices European options under several assumptions:
- The market follows a [**geometric Brownian motion**](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)
- Markets are [**frictionless**](https://en.wikipedia.org/wiki/Frictionless_market)
- The option can only be exercised at maturity ([**European style**](https://en.wikipedia.org/wiki/Option_style))

## ⚙️ Features

- 💲 **European option pricing**
- 🧮 **Analytical Greeks calculation**
- 🔎 **Implied volatility estimation** (bisection method)
- 🖥️ **CLI-based interface**

## ❓Usage

### 1. Price calculation
```bash
python main.py --mode price --S 100 --K 110 --T 1 --r 0.05 --sigma 0.2 --option C
```

### 2. Greeks calculation
```bash
python main.py --mode greeks --S 100 --K 110 --T 1 --r 0.05 --sigma 0.2 --option C
```

### 3. Implied volatility estimation
```bash
python main.py --mode iv --S 100 --K 110 --T 1 --r 0.05 --Cm 5 --option C
```