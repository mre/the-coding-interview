using System;

namespace Atbash
{
    class Program
    {

        const string letters = "abcdefghijklmnopqrstuvwxyz";

        static void Main(string[] args)
        {
            Console.WriteLine(_Cipher("irk"));
            Console.WriteLine(_Cipher("low"));
            Console.WriteLine(_Cipher("hob"));
            Console.WriteLine(_Cipher("hold"));
            Console.ReadKey();

        }

        private static string _Cipher(string text)
        {
            string cipheredText = "";
            int index;
            foreach (var c in text)
            {
                index = letters.IndexOf(c);
                cipheredText += letters.Substring(25 - (index), 1);
            }
            return cipheredText;
        }

    }
}
