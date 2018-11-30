using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World! 12091029");

            ArrayPairSum(10, new int[] { 3, 4, 5, 6, 7 }); // [[6, 4], [7, 3]]
            Console.WriteLine();
            ArrayPairSum(8, new int[] { 3, 4, 5, 4, 4 }); // [[3, 5], [4, 4], [4, 4], [4, 4]]
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

            Dictionary<int, int> complements = new Dictionary<int, int>();
            for (int x = 0; x < input.Length; x++)
            {
                if (!complements.ContainsKey(sum - input[x]) && (input[x] != sum - input[x]))
                {
                    complements.Add(sum - input[x], input[x]);
                }
            }

            List<int[]> valids = new List<int[]>();
            for (int x = 0; x < input.Length; x++)
            {
                if (complements.ContainsKey(input[x])
                    && (input[x] != sum - input[x]))
                {
                    valids.Add(new int[] { input[x], sum - input[x] });
                    complements.Remove(sum - input[x]);
                }
            }


            for (int v = 0; v < valids.Count; v++)
            {
                Console.Write("[" + valids[v][0] + "," + valids[v][1] + "]; ");
            }


            int[][] output = new int[valids.Count][];

            int index = 0;
            foreach (var v in valids)
            {
                output[index++] = new int[2] { v[0], v[1] };
            }

            return output;
        }
    }
}
