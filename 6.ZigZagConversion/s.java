class Solution {
    
    /*# init a 2D array 
    # iterate s from left to right, add each char to appropriate row
    # num of rows min(numRows, len(s))
    # use current row and current direction to control*/
               
public String convert(String s, int numRows) {
    
    if (numRows == 1) return s;
    /* init a list of StringBuilder to store strings*/
    List<StringBuilder> rows = new ArrayList<>();
    for(int i = 0; i < Math.min(numRows, s.length()); i++)
        rows.add(new StringBuilder());
    
    /* vars for controling iteration and adding values to list*/
    int curRow = 0;
    boolean goingDown = false;
    
    /* start to add values to the list*/
    for (char c : s.toCharArray()){
        rows.get(curRow).append(c);
        if (curRow == 0 || curRow == numRows - 1) goingDown = !goingDown;
        curRow += goingDown? 1 : -1;
    }
    
    StringBuilder ret = new StringBuilder();
    for (StringBuilder row : rows) ret.append(row);
    return ret.toString();
}
}