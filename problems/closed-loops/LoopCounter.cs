using System;


namespace ClosedLoops
{
    public class LoopCounter
    {
        static void Main(string[] args)
        {
           int result = CountClosedLoops(2876);
            Console.Out.WriteLine("This method calculates the number of loops in a number. Expected value for {0} is {1}. Actual value is {2}.", 2876, 3, result);
            Console.ReadKey();
        }

        
        public static int CountClosedLoops(int number)
        {
            int loopCount = 0;
            string numberString = number.ToString(); 
            foreach(char digit in numberString)
            {
                switch(digit)
                {
                    case '0':
                        loopCount++;
                        break;
                    case '6':
                        loopCount++;
                        break;
                    
                    case '8':
                        loopCount += 2;
                        break;
                    case '9':
                        loopCount++;
                        break;
                    default:
                        break;
                }
            }
            return loopCount; 
        }
    }
}
