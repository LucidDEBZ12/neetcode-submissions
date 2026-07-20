class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();
        boolean duplicate= false;
        for(int num:nums){
            if(!seen.add(num)){
                duplicate=true;
                break;
            }
        }
        return duplicate;
    }
}