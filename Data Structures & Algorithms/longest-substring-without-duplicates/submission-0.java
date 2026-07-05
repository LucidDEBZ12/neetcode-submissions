class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashMap<Character, Integer> map = new HashMap<>();

        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            // Duplicate character inside the current window
            if (map.containsKey(ch) && map.get(ch) >= left) {
                left = map.get(ch) + 1;
            }

            // Update latest index of the character
            map.put(ch, right);

            // Update maximum window size
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}