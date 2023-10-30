import string
import time


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        length = 0
        left_pointer = 0
        for right_pointer, current_char in enumerate(s):
            if current_char in seen:
                left_pointer = max(left_pointer, seen[current_char] + 1)
            length = max(length, right_pointer - left_pointer + 1)
            seen[current_char] = right_pointer

        return length

def run_tests(tested_function, test_cases):
    for test in test_cases:
        try:
            start = time.time()
            output = tested_function(test['input'])
            end = time.time()
            input_str = str(test['input'])[:100]
            assert test['expected'] == output
            print(f"Test passed in {end - start} seconds")
            print(f"Test passed for expected {test['expected']} for input {input_str} outputted {output} instead")

        except AssertionError:
            print(f"Test failed for expected {test['expected']} for input {input_str} outputted {output} instead")

long_test_case = ''
alphabet = string.ascii_letters
for i in range(0, 50000):
    long_test_case += alphabet[i % 52]

test_cases = [
    {'input': '', 'expected': 0},
    {'input': 'abc', 'expected': 3},
    {'input': 'abcdefgbhijklmnop', 'expected': 15},
    {'input': 'aa', 'expected': 1},
    {'input': long_test_case, 'expected': 52},
]

run_tests(Solution().lengthOfLongestSubstring, test_cases)
