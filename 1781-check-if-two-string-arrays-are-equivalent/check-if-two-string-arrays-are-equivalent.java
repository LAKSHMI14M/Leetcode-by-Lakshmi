class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String A=String.join("",word1);
        String B=String.join("",word2);
        return A.equals(B);  
    }
}