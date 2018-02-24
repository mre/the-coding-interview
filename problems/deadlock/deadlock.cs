using System;
using System.Threading;
using System.Threading.Tasks;

namespace ConsoleApplication
{
   public class DeadlockSamples
{
    private static object A = new Object();
    private static object B = new Object();
 
    public static void Main()
    {
        Thread thread1 = new Thread(Lock1);
        Thread thread2 = new Thread(Lock2);
        thread1.Start();
        thread2.Start();

        thread1.Join();
        thread2.Join();

        // Will never come here.
        Console.WriteLine("End");
    }
 
    private static void Lock1()
    {
        lock (A)
        {
            Console.WriteLine("Trying to acquire lock on B");
            Thread.Sleep(1000);
            lock (B)
            {
                // Will never come here.
                Console.WriteLine("In Lock1 Critical Section.");
            }
        }
    }
 
    private static void Lock2()
    {
        lock (B)
        {
            Console.WriteLine("Trying to acquire lock on A");
            lock (A)
            {
                // Will never come here.
                Console.WriteLine("In Lock2 Critical Section.");
            }
        }
    }
}
}