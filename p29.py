import numpy as np

# Numbers to worry about: 1-10, 16, 25, 27, 32, 36, 49, 64, 81, 100

# Powers of 2: 1-6
# Powers of 3: 1-4
# Powers of 4: 1-3
# Powers of 5: 1-2
# Powers of 6: 1-2
# Powers of 8: 1-2

ans = 81*99

unaccounted = set([2, 3, 4, 5, 6, 7, 8, 9, 10, 16, 25, 27, 32, 36, 49, 64, 81, 100])
print len(unaccounted)

mult1 = set(range(2, 101))
mult2 = set((2*np.arange(2, 101)))
mult3 = set(3*np.arange(2, 101))
mult4 = set(4*np.arange(2, 101))
mult5 = set(5*np.arange(2, 101))
mult6 = set(6*np.arange(2, 101))

power1 = [2, 3, 5, 6, 7, 10]
for i in power1:
    ans += 99
unaccounted -= set(power1)

power2 = [4, 9, 25, 36, 49, 100]
# a = mult2-mult1
# print mult2
# print a
# print len(a)
a = mult3-mult2-mult1
print len(a)

for i in power2:
    ans += len(mult2-mult1)

unaccounted -= set(power2)

power3 = [8,27]
# print len(mult3-mult2-mult1)
unaccounted -= set(power3)
print unaccounted

for i in power3:
    ans += len(mult3-mult2-mult1)

ans += 2*len(mult4-mult3-mult2-mult1)
ans += len(mult5-mult4-mult3-mult2-mult1)
ans += len(mult6-mult5-mult4-mult3-mult2-mult1)
# print len(mult6-mult3-mult4)

print ans
