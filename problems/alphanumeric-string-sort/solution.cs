using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1 {
    class Program {
        static void Main(string[] args) {
            string input = new string(args[0].OrderBy(c => c).ToArray());

            string lower = "", upper = "", even = "", odd = "";
            for (int i = 0; i < input.Length; i++) {
                if (Char.IsLower(input[i])) {
                    lower += input[i];
                } else if (Char.IsUpper(input[i])) {
                    upper += input[i];
                } else if (Char.GetNumericValue(input[i]) % 2 == 0) {
                    even += input[i];
                } else {
                    odd += input[i];
                }
            }

            Console.WriteLine(lower + upper + even + odd);
        }
    }
}
