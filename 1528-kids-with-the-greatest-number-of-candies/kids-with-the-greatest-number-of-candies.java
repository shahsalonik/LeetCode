class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> returnList = new ArrayList<>();
        int currMax = 0;

        for(int j = 0; j < candies.length; j++) {
            int current = candies[j];
            if(current > currMax) {
                currMax = current;
            }
        }

        for(int i = 0; i < candies.length; i++) {
             int current = candies[i];
            if(current + extraCandies >= currMax) {
                returnList.add(true);
            } else {
                returnList.add(false);
            }
        }

        return returnList;
    }
}