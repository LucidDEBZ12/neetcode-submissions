class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        boolean duplicate = false;

        for(int num : nums){
            if(seen.contains(num)){
                duplicate = true;
                break;
            }
            seen.add(num);
        }

        return duplicate;
    }
}