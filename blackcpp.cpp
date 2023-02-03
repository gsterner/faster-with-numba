#include <iostream>
#include <random>
#include <math.h>
#include <algorithm>
#include <chrono>

double black_loop(const int N,
                  const double S_zero,
                  const double T,
                  const double r,
                  const double sigma,
                  const double K) {
    std::default_random_engine generator;
    std::normal_distribution<double> distribution(0.0, 1.0);
    double C_total=0;
    for (int i = 0 ; i < N; i++) {
        double z = distribution(generator);
        double S = S_zero * exp((r - 0.5 * sigma * sigma) * T + sigma * sqrt(T) * z);
        double C = std::max(0.0, S - K);
        C_total += C;
    }
    return exp(- r * T) * C_total / N;
}

int main()
{
    double maturity = 1;
    double underlying_start = 100;
    double strike = 100;
    double rate = 0.02;
    double volatility = 0.2;
    int scenarios = 100000000;

    auto start = std::chrono::high_resolution_clock::now();
    auto price = black_loop(scenarios, underlying_start, maturity, rate, volatility, strike);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> interval = end - start;

    std::cout << price << " " << interval.count() << std::endl;
}
