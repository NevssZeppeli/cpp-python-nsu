#include "modular-sorting.h"

#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <iomanip>

using namespace std;

int main() {
    // Размеры для тестирования
    vector<size_t> test_sizes = {10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000};
    
    // Генератор случайных чисел
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(-100000000, 100000000);
    
    cout << fixed << setprecision(6);
    cout << "Размер\t\tВремя (секунды)\n";
    cout << "------\t\t--------------\n";
    
    for (size_t size : test_sizes) {
        // Создаем и заполняем вектор случайными числами
        vector<int> vec(size);
        for (int& item : vec) {
            item = dis(gen);
        }
        
        // Измеряем время выполнения ModularSort
        auto start = chrono::high_resolution_clock::now();
        ModularSort(vec);
        auto end = chrono::high_resolution_clock::now();
        
        // Вычисляем время в секундах
        auto duration = chrono::duration_cast<chrono::duration<double>>(end - start);
        
        cout << size << "\t\t" << duration.count() << "\n";
    }
    
    return 0;
}