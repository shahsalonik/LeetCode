import java.util.StringTokenizer;

class Solution {
    public String reverseWords(String s) {
        ArrayList<String> sentenceList = new ArrayList<String>();
        StringTokenizer st = new StringTokenizer(s);

        while(st.hasMoreTokens()) {
            sentenceList.add(st.nextToken());
        }

        String finalString = "";

        for(int i = sentenceList.size() - 1; i >= 0; i--) {
            finalString += sentenceList.get(i) + " ";
        }

        return finalString.strip();
        
    }
}
