import java.util.ArrayList;
import java.util.Vector;
import java.util.HashSet;


public class KnightProblem {

	private static boolean duplicate_characters(ArrayList<Character> sequence) {
	    HashSet<Character> unique = new HashSet<Character>();
	    for (char c : sequence) {
	    	unique.add(c);
	    }
	    return unique.size() == sequence.size();
	}

	private static boolean is_valid(ArrayList<Character> sequence) {
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
	    		
	private static Vector<ArrayList<Character>> sequences(char [][] board, int x, int y, ArrayList<Character> seq) {
	    // Check for out of range errors
		char letter;
		Vector<ArrayList<Character>> dummy = new Vector<ArrayList<Character>>();
	    try {
	    	letter = board[x][y];
	    } catch (Exception e) {
	    	return dummy;
	    }
	    seq.add(letter);
	    if (!is_valid(seq)) {
	    	return dummy;
	    }
	    Vector<ArrayList<Character>> result = new Vector<ArrayList<Character>>();
	    result.add(seq);
	    
	    
	    // Continue with all other possible moves
	    //moves = [(-1,-2),(1,-2),(-1,2), (1,2),(-2,-1),(2,-1),(-2,1),(2,1)]
	    //for move in moves:
	    
	    for (ArrayList<Character> s : sequences(board, x-1, y-2, seq)) {
	    	result.add(s);
	    }
	    
	    return result;
	}
	       
	public static void knight(char[][] board) {
	    // We can start at any position on the board
		for (int x = 0; x < board.length; ++x) {
	        for (int y = 0; y < board[0].length; ++y) {
	            // Generate all move sequences from that position
	            System.out.println("Starting position: " + x + " " + y);
	            ArrayList<Character> seq = new ArrayList<Character>();
	            for (ArrayList<Character >sequence : sequences(board, x, y, seq)) {
	                System.out.println(sequence);
	            }
	        }
		}
	}

	public static void main(String[] args) {
		// Move knight on board
		char[][] board = {	{'A','B','C','_', 'E'},
							{'_','G','H','I', 'J'},
							{'K','L','M','N','O'},
							{'P','Q','R','S','T'},
							{'U','V','_','_','Y'}};
		knight(board);
	}

}

