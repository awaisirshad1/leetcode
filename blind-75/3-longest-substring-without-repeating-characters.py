class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # longest encountered substring, init to 0
        longest = 0
        # sliding window
        window = []

        for index, char in enumerate(s):
            # print("window at beginning:", window)
            # print("longest at beginning:", longest)
            if char in window:
                # if we've already encountered a character, slice from after that character to end of current list
                cutoff = window.index(char)
                window = window[cutoff + 1:]

            window.append(char)
            longest = max(len(window), longest)
        # print("window at end:", window)
        # print("longest at end:", longest)

        return longest
