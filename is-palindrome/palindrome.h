#include <string>
#include <cctype>

bool IsPalindrome(std::string s) {
    // std::string rev = "";
    // for (char c : s) {
    //     if (c != ' ') {
    //     rev += std::tolower(c); // безопаснее std::tolower(static_cast<unsigned char>(c))
    //     }
    // }
    //std::string origin = rev;

    // int n = rev.length();
    // for (int i = 0; i < n / 2; ++i) {
    //     char temp = rev[i];
    //     rev[i] = rev[n - 1 - i];
    //     rev[n - 1 - i] = temp;
    // }

    // return rev == origin;

    int left = 0; 
    int right = s.length() - 1;
    while (left < right) {
        if (s[left] == ' ') {
            left++;
            continue;
        }
        if (s[right] == ' ') { 
            right--;
            continue;
        }
        if (std::tolower(s[left]) != std::tolower(s[right])) 
            return false;

        left++;
        right--;
    }

    return true;
}
