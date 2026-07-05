class Solution {
    public int characterReplacement(String s, int k) {

        int[] freq = new int[26];

        int left = 0;
        int maxFreq = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);

            // Increase frequency of current character
            freq[ch - 'A']++;

            // Update the highest frequency in the current window
            maxFreq = Math.max(maxFreq, freq[ch - 'A']);

            // If window is invalid, shrink it
            while ((right - left + 1) - maxFreq > k) {

                freq[s.charAt(left) - 'A']--;
                left++;
            }

            // Update answer
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}