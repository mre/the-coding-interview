using System;
using System.Linq;

namespace ConsoleApplication
{
   public class MissingNumberExample
    {
        public static void Main()
        {
            MissingNumber(new int[] { -3,-2,-1,0,1,3 }); 

            Console.ReadKey();
        }
 
      public static void MissingNumber(int[] arr)
        {
            int sum = arr.Sum();
            arr = arr.OrderBy(i => i).ToArray();
           int incremental_sum = ((arr.Length + 1) * (arr[arr.Length - 1] + arr[0])) / 2;
            Console.WriteLine($"The missing number is: { incremental_sum - sum}");
        }
    }
}
