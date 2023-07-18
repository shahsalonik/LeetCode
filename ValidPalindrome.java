class Solution {
    public boolean isPalindrome(String s) {
        String checkString = s.replaceAll("[^a-zA-Z0-9]", "");
        checkString = checkString.toUpperCase();
        boolean isPal = true;
        for(int i = 0; i < checkString.length(); i++) {
            if(checkString.charAt(i) != checkString.charAt(checkString.length() - 1 - i)) {
                    isPal = false;
                    break;
                }
        }
        return isPal;
    }
}
