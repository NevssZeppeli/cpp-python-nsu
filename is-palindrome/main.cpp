#include <iostream>
#include <string>

#include "palindrome.h"

int main() {
    std::string s;
    std::getline(std::cin, s);
    std::cout << IsPalindrome(s);
    return 0;
}
