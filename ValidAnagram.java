class Solution {
    public boolean isAnagram(String s, String t) {
        boolean isAnagramBool = true;
        for(int i = 0; i < s.length(); i++) {
            if(t.length() > s.length()) {
                isAnagramBool = false;
                break;
            }
            if(t.contains("" + s.charAt(i))) {
                int ind = t.indexOf(s.charAt(i));
                t = t.substring(0, ind) + t.substring(ind + 1, t.length());
            }
            else {
                isAnagramBool = false;
                break;
            }
        }
        return isAnagramBool;
    }
}
