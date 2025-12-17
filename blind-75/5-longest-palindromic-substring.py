class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(i: int, j: int):
            left = i
            right = j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        ans_indices = [0, 0]

        for i in range(len(s)):
            # odd length palindromes
            odd_length = expand(i, i)
            if odd_length > ans_indices[1] - ans_indices[0] + 1:
                dist = odd_length // 2
                ans_indices[0] = i - dist
                ans_indices[1] = i + dist
            # even length palindromes
            even_length = expand(i, i + 1)
            if even_length > ans_indices[1] - ans_indices[0] + 1:
                dist = (even_length // 2) - 1
                ans_indices[0] = i - dist
                ans_indices[1] = i + dist + 1

        i, j = ans_indices
        return s[i: j + 1]






