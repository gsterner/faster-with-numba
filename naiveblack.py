import random
import math
import time
#from numba import jit

#@jit(nopython=True)
def black_loop(N, S_zero, T, r, sigma, K):
    Z = [random.normalvariate(0.0, 1.0) for n in range(N)]
    C_total = 0
    for z in Z:
        S = S_zero * math.exp((r - 0.5 * sigma * sigma) * T + sigma * math.sqrt(T) * z)
        C = max(0, S - K)
        C_total = C_total + C
    return math.exp(- r * T) * C_total / N

maturity = 1
underlying_start = 100
strike = 100
rate = 0.02
volatility = 0.2
#scenarios = 100000000 # 8
scenarios = 1000000 # 6


start = time.perf_counter()
price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike)
end = time.perf_counter()
print("before", price, end - start)

start = time.perf_counter()
price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike)
end = time.perf_counter()
print("after", price, end - start)
