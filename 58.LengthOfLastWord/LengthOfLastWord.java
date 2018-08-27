public class LengthOfLastWord{
    public static int lastWordLength(String s){
        if(s.contains(" ")){
            if(s==" "){
                return 0;
            }
            String w =s.trim();
            String lastWord = w.substring(w.lastIndexOf(" ")+1);            
            return lastWord.length();
        }
        return s.length();
    }

    public static void main(String[] args){
        String[] tests = {"", " ", "thereisnospace","I am ok", " ok", "ok "};
        for (String test:tests){
            System.out.println(lastWordLength(test));
        }
    }
}