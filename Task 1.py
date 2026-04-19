import time
import matplotlib.pyplot as plt

crew = ['C1', 'C2', 'C3']

# simple overlap check
def valid(assign, crew_member, flight):
    for f, c in assign.items():
        if c == crew_member:
            if not (flight[2] <= f[1] or flight[1] >= f[2]):
                return False
    return True

# backtracking
def solve(flights, assign={}, i=0):
    if i == len(flights):
        return True
    
    for c in crew:
        if valid(assign, c, flights[i]):
            assign[flights[i]] = c
            if solve(flights, assign, i+1):
                return True
            del assign[flights[i]]
    return False

# graph data
sizes = [4,5,6,7,8]
times = []

for n in sizes:
    flights = [(f"F{i}", i, i+2) for i in range(n)]
    assign = {}

    start = time.time()
    solve(flights, assign)
    times.append(time.time() - start)

    print("\nFlights:", n)
    print(assign)

# graph
plt.plot(sizes, times, marker='o')
plt.xlabel("Flights")
plt.ylabel("Time")
plt.title("Backtracking Graph")
plt.show()