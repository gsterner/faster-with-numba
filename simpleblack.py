import numpy as np
import time
from numba import jit

@jit(nopython=True)
def black_loop(N, S_zero, T, r, sigma, K):
    Z = np.random.normal(0, 1, size=(N))
    C_total = 0
    for z in Z:
        S = S_zero * np.exp((r - 0.5 * sigma * sigma) * T + sigma * np.sqrt(T) * z)
        C = np.maximum(0, S - K)
        C_total = C_total + C
    return np.exp(- r * T) * C_total / N

#T_start = 0
maturity = 1
# T_steps = 10
# t = (T_end - T_start) / T_steps
# T = np.arange(T_start, T_end, t)
underlying_start = 100
strike = 100
#S = np.ones(T.size) * S_zero
rate = 0.02
volatility = 0.2
scenarios = 10000000

start = time.perf_counter()
price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike)
end = time.perf_counter()
print("before", price, end - start)

start = time.perf_counter()
price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike)
end = time.perf_counter()
print("after", price, end - start)
