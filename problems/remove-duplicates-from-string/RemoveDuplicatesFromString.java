import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

import org.junit.Assert;

public class RemoveDuplicatesFromString {
	
	public static void main (String args[]) {
		new RemoveDuplicatesFromString().removeCharacterDuplicatesTest();
	}
	
	public String removeDuplicateCharacters(String s) {
		List<String> characters = new ArrayList<String>();
		StringBuffer sb = new StringBuffer();
		
		for (int c=0; c<s.length();c++) {
			Character characterToCompare = s.charAt(c);
			
			if (!characters.contains(characterToCompare.toString())) {
				sb.append(characterToCompare);
				characters.add(characterToCompare.toString());
			}
		}
 		
		return sb.toString();
	}

	@Test
	public void removeCharacterDuplicatesTest() {
		Assert.assertEquals(this.removeDuplicateCharacters("tree traversal"), "tre avsl");
		Assert.assertEquals(this.removeDuplicateCharacters("Tree Level"), "Tre Lvl");
		Assert.assertEquals(this.removeDuplicateCharacters("Tree level"), "Tre lv");
		Assert.assertEquals(this.removeDuplicateCharacters("aabb  ccdd"), "ab cd");
	}

}
