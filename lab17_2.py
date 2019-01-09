from math import pow
import timeit

print("power by 2: ")

print("shift power      : "  + str(timeit.timeit('10 << 2',number = 1000000)))
print("power by operator: "  + str(timeit.timeit('10 ** 2',number = 1000000)))
print("math.pow         : "  + str(timeit.timeit('pow(10.0, 2)',number = 1000000)))

def reverse(s : str):
  return "".join(reversed(s))

print("---------------------------------------")
print("reverse list of strings: ")

print("by loop          : " + str(timeit.timeit('for _ in data: _ = "".join(reversed(_))', "data = ['math', 'test', 'pow', 'shift']", number = 100000 )))
print("by map()         : " + str(timeit.timeit('map(reverse, data)', "data = ['math', 'test', 'pow', 'shift']",  number = 100000, globals = {'reverse' : globals().get('reverse')} )))
