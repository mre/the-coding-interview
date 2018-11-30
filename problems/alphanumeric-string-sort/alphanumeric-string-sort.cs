using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World! 12091029");
            Console.WriteLine(alphaNumericSort("Hello World! 12091029"));
            Console.WriteLine(alphaNumericSort("Sorting0123456789"));             // ginortS0246813579
            Console.WriteLine(alphaNumericSort("foobar1237348421"));              // abfoor2244811337
            Console.WriteLine(alphaNumericSort("789765445whjdbjwhwfbs977865"));   // bbdfhhjjswww446688555777799
        }
        
        public static string alphaNumericSort(string input)
        {
            if (string.IsNullOrEmpty(input))
                return input;

            char[] iChars = input.ToCharArray();
            Array.Sort(iChars);

            string processStr = new string(iChars);

            string upperCase = "", lowerCase = "", even = "", odd = "";

            for (int x = 0; x < processStr.Length; x++)
            {
                if (processStr[x] - 'z' <= 0 && processStr[x] - 'a' >= 0)
                {
                    lowerCase += processStr[x] + "";
                }
                else if (processStr[x] - 'Z' <= 0 && processStr[x] - 'A' >= 0)
                {
                    upperCase += processStr[x] + "";
                }
                else if (processStr[x] - '9' <= 0 && processStr[x] - '0' >= 0)
                {
                    int num = 0;
                    int.TryParse(processStr[x] + "", out num);

                    if (num % 2 == 0)
                    {
                        even += processStr[x];
                    }
                    else
                    {
                        odd += processStr[x];
                    }
                }
            }

            return lowerCase + upperCase + even + odd;
        }
    }
}
