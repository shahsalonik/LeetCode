class Solution {
    public String mergeAlternately(String word1, String word2) {
        int len = 0;
        boolean w1longer = true;
        int w1length = word1.length();
        int w2length = word2.length();
        char[] word1arr = word1.toCharArray();
        char[] word2arr = word2.toCharArray();
        if(w1length < w2length) {
            len = w1length;
            w1longer = false;
        } else if (w2length < w1length) {
            len = w2length;
        } else {
            len = w1length;
        }
        StringBuilder finalString = new StringBuilder();
        for(int i = 0; i < len; i++) {
            finalString.append(word1arr[i]);
            finalString.append(word2arr[i]);
        }
        if(!w1longer) {
            finalString.append(word2.substring(len));
        } else {
            finalString.append(word1.substring(len));
        }

        return finalString.toString();
    }
}