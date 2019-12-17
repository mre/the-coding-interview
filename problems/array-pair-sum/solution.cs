using System;
using System.Collections.Generic;
using System.Linq;

namespace Solution {
    class Program {
        static void Main(string[] args) {
            var input = args[0].Split(',').Select(int.Parse).ToArray();
            var k = input[0];
            var seen = new HashSet<int>();
            var pairs = new List<(int x, int y)>();

            for (var i = 1; i < input.Length; i++) {
                var n = input[i];
                var x = k - n;
                if (x != n) {
                    if (seen.Contains(x)) {
                        pairs.Add((Math.Min(x, n), Math.Max(x, n)));
                    } else {
                        seen.Add(n);
                    }
                }
            }

            Console.Write('[');
            for (var i = 0; i < pairs.Count; i++) {
                if (i != 0) {
                    Console.Write(", ");
                }
                Console.Write("(" + pairs[i].x + ", " + pairs[i].y + ")");
            }
            Console.Write(']');
        }
    }
}
