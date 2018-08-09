#include <iostream>
#include <string>
#include <algorithm>

std::string lower_upper_order(std::string upper_lower_string)
{
    std::string lower_string = "";
    std::string upper_string = "";
    
    for (auto c : upper_lower_string) {
        // Using ASCII values to sort the string
        if (int(c) >= 97) {
            lower_string += c;
        } else {
            upper_string += c;
        }
    }
    
    return lower_string + upper_string;
}

std::string alphanum_sort(std::string alphanum_string)
{
    std::string num_chars = "0246813579";
    std::string alpha_sorted_string = "";
    std::string num_sorted_string = "";
    std::string num_str_even = "";
    std::string num_str_odd = "";
    
    for (auto c : alphanum_string) {
        if (num_chars.find(c) == std::string::npos) {
            alpha_sorted_string += c;
        } else {
            num_sorted_string += c;
        }
    }
    
    for (auto tc : num_sorted_string) {
        // Using the properties of ASCII chars
        // Even numbers have even ASCII values and vice versa
        if (int(tc) % 2 == 0) {
            num_str_even += tc;
        } else {
            num_str_odd += tc;
        }
    }
    
    std::sort(alpha_sorted_string.begin(), alpha_sorted_string.end());
    std::sort(num_str_even.begin(), num_str_even.end());
    std::sort(num_str_odd.begin(), num_str_odd.end());
    
    num_sorted_string = num_str_even + num_str_odd;
  
    return lower_upper_order(alpha_sorted_string) + num_sorted_string;
}        


int main()
{
    std::cout << alphanum_sort("Sorting0123456789") << std::endl;             // ginortS0246813579
    std::cout << alphanum_sort("foobar1237348421") << std::endl;              // abfoor2244811337
    std::cout << alphanum_sort("789765445whjdbjwhwfbs977865") << std::endl;   // bbdfhhjjswww446688555777799
}
