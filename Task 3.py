import time
import matplotlib.pyplot as plt

# simple naive search
def naive(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break

# data for graph
sizes = [100, 200, 400, 800, 1600]
times = []

for n in sizes:
    text = "A" * n + "B"
    
    start = time.time()
    naive(text, "AB")
    end = time.time()
    
    times.append(end - start)

# plot graph
plt.plot(sizes, times, marker='o')
plt.xlabel("Text Size")
plt.ylabel("Execution Time")
plt.title("String Matching (Naive) Graph")
plt.grid()
plt.show()