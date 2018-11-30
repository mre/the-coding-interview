using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ArraySum(new object[] { 3, 4, new object[] { 5, 6, new object[] { 6, 7 } } }));   // 31
            Console.WriteLine(ArraySum(new object[] { 3, 4, new object[] { 5, 6 }, new object[] { 6, 7 } }));   // 31
        }

        public static int ArraySum(object input)
        {
            if (input == null)
                return 0;

            int index = 0;
            int sum = 0;

            if (input is Array)
            {
                object[] inp = (object[])input;

                while (index < inp.Length)
                {
                    object currentValue = inp[index++];

                    if (currentValue is int)
                    {
                        sum += (int)currentValue;
                    }

                    if (currentValue is Array)
                    {
                        sum += ArraySum(currentValue);
                    }
                }
            }

            return sum;
        }
    }
}
