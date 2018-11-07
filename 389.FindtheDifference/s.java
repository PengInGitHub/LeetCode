class Solution {
    public char findTheDifference(String s, String t) {
        int charCode = t.charAt(s.length());
        // Iterate over both strings and charcodes
        for(int i = 0; i < s.length(); i++){
            charCode -= (int) s.charAt(i);
            charCode += (int) t.charAt(i);
        }
        return (char) charCode;
    }
}