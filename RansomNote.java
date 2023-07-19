class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int count = 0;
        for(char c : ransomNote.toCharArray()) {
            if(magazine.contains("" + c)) {
                int ind = magazine.indexOf(c);
                magazine = "" + magazine.substring(0, ind) + magazine.substring(ind + 1);
                count += 1;
            }
        }
        if(count == ransomNote.length()) {
            return true;
        }
        else {
            return false;
        }
    }
}
