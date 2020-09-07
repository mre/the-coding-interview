class sum35 {
	//We find sum of natural numbers using the formula
	//k = n(n+1)/2
	public static int sum(int n) {
		return (n*(n+1))/2;
	}

	public static void main(String[] args) {
		//sum() is used to calculate the sum of natural numbers
		//We use number/3(or 5 or 15) to ensure a integral division
		//Explanation for why this works can be found here - 
		//https://math.stackexchange.com/questions/9259/find-the-sum-of-all-the-multiples-of-3-or-5-below-1000
		
		int sum = 3*sum(999/3) + 5*sum(999/5) - 15*sum(999/15);	

		System.out.println("The sum of integers that are a multiple of 3 or 5 until 1000 is " + sum);
	}
}
