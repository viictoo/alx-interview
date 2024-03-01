import time
from concurrent.futures import ProcessPoolExecutor

makeChangeDP = __import__('0-making_change').makeChangez
makeChangeGreedy = __import__('0-making_change').makeChange1

start = time.time()
# run on 2 CPU cores
with ProcessPoolExecutor(2) as exe:
        exe.map(makeChangeDP([1, 4, 5, 10], 1278652), range(1, 100))
end = time.time()
avg = (end - start) / 10

startg = time.time()
with ProcessPoolExecutor(2) as exe:
        exe.map(makeChangeGreedy([1, 4, 5, 10], 1278652), range(1, 100))

endg = time.time()
avgg = (endg - startg) / 10

start2 = time.time()
with ProcessPoolExecutor(2) as exe:
        exe.map(makeChangeDP([1, 4, 5, 10], 1278652), range(1, 100))
end2 = time.time()
avg2 = (end2 - start2) / 10


print(f"runtime greedy = {avgg}")
print(f"runtime dp = {avg}")
print(f"runtime dp2 = {avg2}")


if avg2 > 3:
    print("Runtime too long")
else:
    print("OK")
