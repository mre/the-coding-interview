using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1 {
    class Program {
        static void Main(string[] args) {
            string input = new string(args[0].OrderBy(c => c).ToArray());

            string lower = "";
            string upper = "";
            string even = "";
            string odd = "";
            for (int i = 0; i < input.Length; i++) {
                if (Char.IsLower(input[i])) {
                    lower += input[i];
                } else if (Char.IsUpper(input[i])) {
                    upper += input[i];
                } else {
                    switch (input[i]) {
                        case '0':
                        case '2':
                        case '4':
                        case '6':
                        case '8':
                            even += input[i];
                            break;

                        default:
                            odd += input[i];
                            break;
                    }
                }
            }
            Console.WriteLine(lower + upper + even + odd);
        }
    }
}
