#include <iostream>
#include <vector>
#include <algorithm>

int bruteforce(std::vector<int> list);
int hash(std::vector<int> list);
bool mysort(int i, int j);
int sortthencompare(std::vector<int> list);
int binarysearch(std::vector<int> list, int n, int m);

int bruteforce(std::vector<int> list)
{
    for (auto i = 0; i < list.size(); i++)
    {
        for (auto j = i+1; j < list.size(); j++)
        {
            if (list[i] == list[j])
                return list[i];
        }
    }
    return -1;
}

int hash(std::vector<int> list)
{
    std::vector<bool> found = {false};
    for (auto i = 0; i < list.size(); i++)
    {
        if (found[list[i]])
            return list[i];
        found[list[i]] = true;
    }
    return -1;
}

bool mysort(int i, int j)
{
    return i < j;
}

int sortthencompare(std::vector<int> list)
{
    std::stable_sort(list.begin(), list.end(), mysort);
    for (auto i = 0; i < list.size(); i++)
    {
        if (list[i] == list[i+1])
            return list[i];
    }
    return -1;
}
    
int binarysearch(std::vector<int> list, int n, int m)
{
    while (n < m)
    {
        int count = 0;
        int mid = (n + m) / 2;
        for (int item : list)
            if (item >= n && item <= mid)
                count++;
        if (count > mid - n + 1)
            m = mid;
        else
            n = mid + 1;
    }
    return m;
}

int main()
{
    std::vector<int> list = {9, 8, 6, 7, 5, 7, 3, 4, 2, 1};
    std::cout << "Expected result: 7" << std::endl;
    std::cout << "Brute force: " << bruteforce(list) << std::endl;
    std::cout << "Using hash: " << hash(list) << std::endl;
    std::cout << "Sort then compare: " << sortthencompare(list) << std::endl;
    std::cout << "Binary search: " << binarysearch(list, 1, list.size() - 1) 
              << std::endl;
    return 0;
}
