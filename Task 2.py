import time
import matplotlib.pyplot as plt

crew_members = ['C1', 'C2', 'C3']

def generate_flights(n):
    return [(f"F{i+1}", i+9, i+11) for i in range(n)]

# Bounding function (pruning)
def is_valid(crew, flight, assignment):
    for f, c in assignment.items():
        if c == crew:
            if not (flight[2] <= f[1] or flight[1] >= f[2]):
                return False
    return True

# Branch and Bound
def branch_and_bound(flights, assignment, index):
    if index == len(flights):
        return True

    flight = flights[index]

    for crew in crew_members:
        if is_valid(crew, flight, assignment):  # bound condition
            assignment[flight] = crew
            if branch_and_bound(flights, assignment, index + 1):
                return True
            del assignment[flight]

    return False

# Profiling
sizes = [4,5,6,7,8,9,10]
times = []

for n in sizes:
    flights = generate_flights(n)
    assignment = {}

    start = time.time()
    branch_and_bound(flights, assignment, 0)
    end = time.time()

    times.append(end - start)

    print(f"\nFlights: {n}")
    for f, c in assignment.items():
        print(f"{f} -> {c}")

# Graph
plt.plot(sizes, times, marker='o')
plt.xlabel("Number of Flights")
plt.ylabel("Execution Time")
plt.title("Branch and Bound Performance")
plt.grid()
plt.show()