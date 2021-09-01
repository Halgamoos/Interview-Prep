"""
don't do it in place
hash table to count then append occurences
sue count var instead of hash 

sort then reversed
  we can use reverse sort instead

count approach

two var for 0 and 1
copy arr

loop thru input array add each element to copy arr

loop copy arr, and add either + 1 for every occurence of 0 and 1

replace the amount of 1's that occur into the copy arr
do the same for the 0's 

return copy arr
"""
#  dsagfsdf
# fds

move_zeroes_to_end = lambda array: [1]*(count_1 := array.count(1)) + [0]*(len(array)-count_1)

tests = [
    [[], []],
    [[0], [0]],
    [[1], [1]],
    [[1, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0]],
]

for input_arr, correct_result in tests:
    result = move_zeroes_to_end(input_arr)
    print(input_arr, result, correct_result, result == correct_result, sep=" | ")