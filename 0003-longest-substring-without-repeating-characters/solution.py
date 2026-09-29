class Solution:
  def lengthOfLongestSubstring(self, s): 
    d = {} 
    i = 0
    ans = 0
    for j, c in enumerate(s):
      if c in d:
        i = max(i, d[c] + 1)
      d[c] = j
      ans = max(ans, j - i + 1)
    return ans