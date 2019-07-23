#include <iostream>
#include <unordered_map>

// map of all upper case and lower case chars with prime numbers
const static std::unordered_map<char, int> hash{
    {'a' , 2},
    {'b' , 3},
    {'c' , 5},
    {'d' , 7},
    {'e' , 11},
    {'f' , 13},
    {'g' , 17},
    {'h' , 19},
    {'i' , 23},
    {'j' , 29},
    {'k' , 31},
    {'l' , 37},
    {'m' , 41},
    {'n' , 43},
    {'o' , 47},
    {'p' , 53},
    {'q' , 59},
    {'r' , 61},
    {'s' , 67},
    {'t' , 71},
    {'u' , 73},
    {'v' , 79},
    {'w' , 83},
    {'x' , 89},
    {'y' , 97},
    {'z' , 101},
    {'A' , 103},
    {'B' , 107},
    {'C' , 109},
    {'D' , 113},
    {'E' , 127},
    {'F' , 131},
    {'G' , 137},
    {'H' , 139},
    {'I' , 149},
    {'J' , 151},
    {'K' , 163},
    {'L' , 167},
    {'M' , 173},
    {'N' , 179},
    {'O' , 181},
    {'P' , 191},
    {'Q' , 193},
    {'R' , 197},
    {'S' , 199},
    {'T' , 211},
    {'U' , 223},
    {'V' , 227},
    {'W' , 229},
    {'X' , 233},
    {'Y' , 239},
    {'Z' , 241 }
};

// returns the hash of string which is unique for the combination
// of characters in that string.
// By unique factorization theorem there won't be any hash collisions
long long get_hash(const std::string& str) {
  long long hash_val = 1;
  for (char c : str) {
    hash_val *= hash.at(c);
  }

  return hash_val;
}

// This funtion calculates the hash of string
long long anagram_count(const std::string& parent, const std::string& child) {
  long long hash_child = get_hash(child);

  // to keep count of all anagrams
  long long count = 0;

  // get the hash of first n characters where n is length of child
  long long hash_val = get_hash(parent.substr(0, child.size()));
  if (hash_val == hash_child) {
    count++;
  }

  // As we are moving ahead one char at a time, to calculate the hash_val of next string
  // we can divide the last hash_val by the hash of char which is moving out
  // and multiply by the hash of char being moving in
  // e.g. in abcd, if hash_val of "abc" is n, then hash_val of "bcd" is: n / hash.at('a') * hash.at('d');
  for (size_t index = child.size(); index < parent.size(); ++index) {
    hash_val /= hash.at(parent[index - child.size()]);
    hash_val *= hash.at(parent[index]);
    if (hash_val == hash_child) {
      count++;
    }
  }

  return count;
}

int main() {
  std::cout << anagram_count("forbtorfxdofrm", "for") << std::endl; // 3
  std::cout << anagram_count("aabaabaa", "aaba") << std::endl; // 4
  std::cout << anagram_count("AdnBndAndBdaBn", "dAn") << std::endl; // 4
  std::cout << anagram_count("AbrAcadAbRa", "cAda") << std::endl; // 2
  return 0;
}
