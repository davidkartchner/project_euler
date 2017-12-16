import numpy as np
from tqdm import tqdm, trange

ans = 0
for num in trange(2, 6*9**5):
    digits = np.array([int(digit) for digit in str(num)])
    digit_sum = np.sum(digits**5)
    if digit_sum == num:
        # print digits, digit_sum
        ans += num

print ans
