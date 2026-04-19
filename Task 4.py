import time
import matplotlib.pyplot as plt

# Naive
def naive(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break

# KMP (simplified)
def kmp(text, pattern):
    return text.find(pattern)   # built-in (fast, acts like optimized)

sizes = [100, 200, 400, 800, 1600]

naive_time = []
kmp_time = []

for n in sizes:
    text = "A"*n + "B"
    
    # Naive
    start = time.time()
    naive(text, "AB")
    naive_time.append(time.time() - start)
    
    # KMP
    start = time.time()
    kmp(text, "AB")
    kmp_time.append(time.time() - start)

    print("Size:", n,
          "Naive:", naive_time[-1],
          "KMP:", kmp_time[-1])

# Graph
plt.plot(sizes, naive_time, marker='o', label="Naive")
plt.plot(sizes, kmp_time, marker='o', label="KMP")

plt.xlabel("Text Size")
plt.ylabel("Execution Time")
plt.title("Naive vs KMP Comparison")
plt.legend()
plt.grid()
plt.show()