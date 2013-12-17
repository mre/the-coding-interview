import java.util.HashSet;
import java.util.Set;


public class knight {

	private static boolean duplicate_characters(char[] sequence) {
	    HashSet<Character> unique = new HashSet<Character>();
	    for (char c : sequence) {
	    	unique.add(c);
	    }
	    return unique.size() == sequence.length;
	}

	private static boolean is_valid(char[] sequence) {
	    /*
	    A string is not valid if the knight moves onto a blank square 
	    and the string cannot contain more than two vowels.
	    */
			
		int num_vowels = 0;
		for (char c : sequence) {
			// Check for spaces
			if (c == '_') {
				return false;
			}
			if (c == 'A' || c == 'E' || c == 'I' || c == 'U' || c == 'O') {
				num_vowels++;
				if (num_vowels > 2) {
					return false;
				}
			}
		}
			   
	  	/*
	  	 * Check for duplicate characters.
	     * The original question did not say anything about
	     * repeated characters, but ignoring them would lead to infinite
	     * sequences, such as AMAMAMA..., where the knight makes the same sequence
	     * of moves over and over again
	     */
	     return !duplicate_characters(sequence);
	}
	    		
	private static char[] sequences(char [][] board, int x, int y, char[] seq) {
	    // Check for out of range errors
	    try {
	    	char letter = board[x][y];
	    } catch (Exception e) {
	    	char[] s = new char[]{''};
	    	return [''];
	    }
	    seq.append(letter)
	    if not is_valid(seq):
	        return
	    yield seq
	    # Continue with all other possible moves
	    moves = [(-1,-2),(1,-2),(-1,2), (1,2),(-2,-1),(2,-1),(-2,1),(2,1)]
	    for move in moves:
	        curr_seq = seq[:]
	        dx, dy = move
	        for s in sequences(board, (x+dx, y+dy), curr_seq):
	            yield s
	            /*
	def knight(board):
	    result = []
	    # We can start at any position on the board
	    for x in range(len(board)-1):
	        for y in range(len(board[0])-1):
	            # Generate all move sequences from that position
	            print "Starting position: ", x, y
	            for sequence in sequences(board, x, y, []):
	                result.append("".join(sequence))
	    return result

	# Move knight on board
	board = "ABC_E _GHIJ KLMNO PQRST UV__Y".split()
	print knight(board)

	
	*/
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
