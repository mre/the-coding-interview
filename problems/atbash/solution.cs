using System;

namespace Atbash {
    class Program {
        static void Main(string[] args) {
            const int z = (int) 'z';
            const int a = (int) 'a';
            string s = args[0];
            foreach (char c in s) {
                Console.Write(c == '\n' ? c : (char) (z - (((int)c) - a)));
            }
        }
    }
}
