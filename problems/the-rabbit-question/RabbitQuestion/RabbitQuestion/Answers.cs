namespace RabbitQuestion
{
    public class Answers
    {
        public int FibRecursive(int n)
        {
            // You sometimes see the below implemented with a switch
            if (n == 0)
            {
                return 0;
            }

            if (n == 1)
            {
                return 1;
            }

            return FibRecursive(n - 1) + FibRecursive(n - 2);
        }
    }
}
