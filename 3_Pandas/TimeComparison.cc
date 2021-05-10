#include <iostream>
#include <array>
#include <random>
#include <algorithm>

#include "Timer.h"

constexpr std::size_t LEN = 10000;

void fillRandom(std::array<float, LEN>& arr)
{
    std::random_device rnd_device;
    std::mt19937 mersenne_engine {rnd_device()};
    std::normal_distribution<float> dist { 0.0f, 1.0f };

    auto gen = [&dist, &mersenne_engine](){
                   return dist(mersenne_engine);
               };

    std::generate(arr.begin(), arr.end(), gen);
}

void head(std::array<float, LEN>& arr, std::size_t n = 10)
{
    for (std::size_t i = 0; i < n; ++i)
    {
        std::cout << arr[i] << ", ";
    }

    std::cout << "\n";
}

void apply(std::array<float, LEN>& arr)
{
    for (auto& val : arr)
    {
        if (val < 0.5f)
        {
            val = 0.0f;
        }
    }
}

void transform(std::array<float, LEN>& arr)
{
    for (auto& val : arr)
    {
        val += 1.0f;
    }
}

int main()
{
    int num_runs = 10000;
    double total_time = 0.0f;
    std::array<float, LEN> A;

    total_time = 0.0f;
    fillRandom(A);
    for (int i = 0; i < num_runs; ++i)
    {
        cpptiming::Timer t;
        apply(A);
        total_time += t.elapsed_time<cpptiming::nanosecs, double>();
    }
    std::cout << "Mean time apply: " << total_time / num_runs << " ns" << std::endl;
    head(A);

    total_time = 0.0f;
    fillRandom(A);
    for (int i = 0; i < num_runs; ++i)
    {
        cpptiming::Timer t;
        transform(A);
        total_time += t.elapsed_time<cpptiming::nanosecs, double>();
    }
    std::cout << "Mean time transform: " << total_time / num_runs << " ns" << std::endl;
    head(A);

    return 0;
}
