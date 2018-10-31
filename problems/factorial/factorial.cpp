#include <iostream>

using namespace std;

// Making these return doubles allows for calculating much higher factorials
// If these return ints, then you can only do up to 12!
double factorialRecursive(int num);
double factorialReverse(int num);
double factorialIterative(int num);

int main() {
	cout << "factorialRecursive(3): " << factorialRecursive(3) << endl;
	cout << "factorialRecursive(-2): " << factorialRecursive(-2) << endl;
	cout << "factorialRecursive(70): " << factorialRecursive(70) << endl;
	cout << "factorialReverse(3): " << factorialReverse(3) << endl;
	cout << "factorialReverse(-2): " << factorialReverse(-2) << endl;
	cout << "factorialReverse(70): " << factorialReverse(70) << endl;
	cout << "factorialIterative(3): " << factorialIterative(3) << endl;
	cout << "factorialIterative(-2): " << factorialIterative(-2) << endl;
	cout << "factorialIterative(70): " << factorialIterative(70) << endl;
	return 0;
}

// Recursive example
double factorialRecursive(int num) {
	if (num < 2)
		return 1;
	else
		return num * factorialRecursive(num - 1);
}

// Reverse reverse loop example
double factorialReverse(int num) {
	double fact = 1;
	while (num > 1)
		fact *= num--;
	return fact;
}

// Iterative example
double factorialIterative(int num) {
	double fact = 1;
	for (int i = 2; i <= num; i++)
		fact *= i;
	return fact;
}
