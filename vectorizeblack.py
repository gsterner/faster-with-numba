import numpy as np
import time
from numba import njit, vectorize, float64

@vectorize([float64(float64, float64, float64, float64, float64, float64)])
def prices_from_underlying(Z, S_zero, T, r, sigma, K):
    S = S_zero * np.exp((r - 0.5 * sigma * sigma) * T + sigma * np.sqrt(T) * Z)
    diff = S - K
    ismax = 0 < diff
    return np.multiply(diff, ismax)

@njit
def black_loop(N, S_zero, T, r, sigma, K):
    Z = np.random.normal(0, 1, size=(N))
    C = prices_from_underlying(Z, S_zero, T, r, sigma, K)
    C_total = np.sum(C)
    return np.exp(- r * T) * C_total / N

maturity = 1
underlying_start = 100
strike = 100
rate = 0.02
volatility = 0.2
scenarios = 100000000

start = time.perf_counter()
price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike)
end = time.perf_counter()
print("before", price, end - start)

start = time.perf_counter()
price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike)
end = time.perf_counter()
print("after", price, end - start)
