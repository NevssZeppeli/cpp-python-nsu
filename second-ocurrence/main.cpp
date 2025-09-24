#include <iostream>
#include <string>

int main() {
    // std::string s;
    // std::cin >> s;

    // int counter = 0;

    // for (int i = 0; i < s.size(); i++) {
    //     if (s[i] == 'f') {
    //         counter++;

    //         if (counter == 2) {
    //             std::cout << i;
    //         }
    //     }
    // }

    // if (counter == 1) {
    //     std::cout << "-1";
    // } else if (counter == 0) {
    //     std::cout << "-2";
    // }

    // return 0;
    std::string s;
    std::cin >> s;

    bool first_found = false;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'f') {
            if (first_found) { // если мы прошли цикл один раз, флаг меняет значение на True, и уже при втором проходе мы найдем индекс второго вхождения 
                std::cout << i << std::endl;
                return 0;
            }
            first_found = true;
        }
    }

    std::cout << (first_found ? -1 : -2) << std::endl;
    // if (first_found) { // случай если мы нашли первое вхождение, но не нашли второго
    //     std::cout << -1 << std::endl;
    // } else { // вообще ничего не нашли :(
    //     std::cout << -2 << std::endl;
    // }

    return 0;
}
