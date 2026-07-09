class Solution {
    public String minWindow(String s, String t) {

        if (t.length() > s.length()) {
            return "";
        }

        HashMap<Character, Integer> target = new HashMap<>();
        HashMap<Character, Integer> window = new HashMap<>();

        // Build target frequency map
        for (char c : t.toCharArray()) {
            target.put(c, target.getOrDefault(c, 0) + 1);
        }

        int have = 0;
        int need = target.size();

        int left = 0;

        int minLength = Integer.MAX_VALUE;
        int start = 0;

        // Expand window
        for (int right = 0; right < s.length(); right++) {

            char ch = s.charAt(right);
            window.put(ch, window.getOrDefault(ch, 0) + 1);

            // Requirement satisfied
            if (target.containsKey(ch) &&
                window.get(ch).intValue() == target.get(ch).intValue()) {
                have++;
            }

            // Shrink window
            while (have == need) {

                // Update answer
                if ((right - left + 1) < minLength) {
                    minLength = right - left + 1;
                    start = left;
                }

                char leftChar = s.charAt(left);

                window.put(leftChar, window.get(leftChar) - 1);

                // Requirement broken
                if (target.containsKey(leftChar) &&
                    window.get(leftChar) < target.get(leftChar)) {
                    have--;
                }

                left++;
            }
        }

        if (minLength == Integer.MAX_VALUE) {
            return "";
        }

        return s.substring(start, start + minLength);
    }
}