using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World! 12091029");

            ArrayPairSum(10, new int[] { 3, 4, 5, 6, 7 }); // [[4, 6], [3, 7]]
            Console.WriteLine();
            ArrayPairSum(8, new int[] { 3, 4, 5, 4, 4 }); // [[3, 5], [4, 4]]
            Console.WriteLine();
            ArrayPairSum(8, new int[] { 4 }); // []
            Console.WriteLine();
            ArrayPairSum(0, new int[] { 4, -4 }); // [[-4,4]]
            Console.WriteLine();
        }

        public static int[][] ArrayPairSum(int sum, int[] input)
        {
            if (input == null || input.Length < 2)
                return new int[][] { };

            var seen = new HashSet<int>();
            var result = new HashSet<(int x, int y)>();

            for (int i = 0; i < input.Length; i++)
            {
                var num = input[i];
                var target = sum - num;
                if (!seen.Contains(target))
                    seen.Add(num);
                else
                    result.Add((target, num));
            }

            foreach (var pair in result)
            {
                Console.Write("[" + pair.x + "," + pair.y + "]; ");
            }

            return result.Select(pair => new int[] { pair.x, pair.y }).ToArray();
        }
    }
}
