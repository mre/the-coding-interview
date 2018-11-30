using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program4
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ReverseWordsInAString("a quick brown fox")); // fox brown quick a
        }

	//
	// This verison uses additional memory
	//
        public static string ReverseWordsInAString(string input)
        {
            if (string.IsNullOrEmpty(input)) return "";

            List<string> revWords = new List<string>();
            string cWord = "";
            for (int x = 0; x < input.Length; x++)
            {
                if (input[x] == ' ')
                {
                    revWords.Add(cWord);
                    cWord = "";
                }
                else
                {
                    cWord += input[x];
                }
            }

            if (!string.IsNullOrEmpty(cWord))
            {
                revWords.Add(cWord);
            }

            string output = "";
            for (int x = revWords.Count - 1; x >= 0; x--)
            {
                output += revWords[x] + " ";
            }

            return output;
        }
    }
}
