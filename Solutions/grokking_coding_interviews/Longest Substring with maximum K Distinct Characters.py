"""
Problem Statement:
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
"""

def longest_substring_with_k_distinct(str1, k):
  char_frequency = {}
  window_start = 0
  max_length = 0
  for window_end in range(len(str1)):
    # make a "rightmost" variable that can be used to check if the var is in the hashtable
    right_char = str1[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1
    # whenever the amount of distinct chars in the hash is > k, shrink window 
    # when shrinking, subtract char_frequecy val by one. Whenever it is 0, remove the key value
    while len(char_frequency) > k: 
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1
    max_length = max(max_length, window_end - window_start + 1)
  return max_length