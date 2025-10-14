#pragma once

#include <vector>
#include <algorithm>
#include <cmath>

// bool compare_abs(int a, int b) {
    // return std::abs(a) < std::abs(b);
// }

void ModularSort(std::vector<int>& v) {
    std::sort(v.begin(), v.end(), [](int a, int b) {
        return std::abs(a) < std::abs(b);
    });
}

// написать оценку для векторов длиной 10, 100 и тд
// https://docs.google.com/spreadsheets/d/1m0qyL0gERJmRQWqzvWoswb3b2y3i8jG4eHVwUr5LglY/edit?gid=0#gid=0