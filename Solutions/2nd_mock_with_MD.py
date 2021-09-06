"""
Things I could do better:
  - Make sure I don't move on before fully understanding the problem
    - "can you walk me through an example?"
  - Test small
  - Psudo code before implenting

happy number 
n^2 == 1

7^2 = 49
4^2 = 16 
9^2 = 81 
16 + 81 = 97

9^2 = 81
7^2 = 49
81
49 = 130
1^2 = 1
3^2 = 9
0^2 = 0
1 + 9 + 0 = 10
1^2 = 1
0^2 = 0
1 + 0 = 1

11

if 0 == not happy

7
49
16 + 81
97

num > 0, will it ever trasform into 0
1 will never == 0
2 = 2^2 = 4, 16, 1 + 36 = 37, 9 + 49 = 58, 25 + 64,
89, 64 + 81 = 145, 1 + 16 + 25 = 42, 16 + 4 = 20,
4
it will never become happy because it loops forever while != 1 

n <= 1000

999 = 81 + 81 + 81, 

#1 --> loops
  - store each tranformation into a hashtable
  - set() --> hashtable with only keys
#2 --> becomes 1
"""

def is_happy(num):
  seen = set()

  while num != 1:
    num = sum(int(char)**2 for char in str(num))
    if num in seen: return False
    seen.add(num)
  
  return True

tests = [
  [0, False],
  [1, True], 
  [7, True],
  [2, False]
]
for input_num, correct_result in tests:
  our_result = is_happy(input_num)
  print(input_num, correct_result, our_result, our_result == correct_result, sep = " | ")


def cube(num):
  # 2 + 2
  # 4 + 4 = 8

  square = 0 # 2, 4
  # 0, 1
  for _ in range(num):
    square += num
  # square = 4
  cube = 0
  # 4, 8
  for _ in range(num):
    cube += square
  return cube

# tests = [
#   [1,1], 
#   [2,8],
#   [5, 125],
#   [25,15625],
#   [69, 328509]
# ]

# for input_num, correct_result in tests:
#   result = cube(input_num)
#   print(input_num, correct_result, result, result == correct_result, sep = " | " )