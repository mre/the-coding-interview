#include <iostream>
#include <string>
#include <algorithm>
#include <math.h>

std::string convert(long long num, int base) {
    std::string char_list = "0123456789ABCDEF";
    if (num < base) return char_list.substr(num, 1);
    return convert((long long)num/base, base) + char_list.at(num % base);
}

bool is_prime(int num)
{
    if (num <=1)
        return false;
    else if (num == 2)         
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int limit = static_cast<int>(sqrt(num_d) +1);
        
        while (divisor <= limit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

bool is_cross_base_prime(int n, int base)
{
    if (is_prime(n) && is_prime(std::stoi(convert(n, base))))
        return true;
    return false;
}


int main()
{   
    std::cout << is_cross_base_prime(69, 2) << std::endl;      // 0 (false)
    std::cout << is_cross_base_prime(131, 16) << std::endl;    // 1 (true)
    std::cout << is_cross_base_prime(1312, 8) << std:: endl;   // 0 (false)
    std::cout << is_cross_base_prime(67, 11) << std::endl;     // 1 (true)
}
