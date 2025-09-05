import numpy as np

# update/add code below ...

def ways(n):
    if n < 0:
        return 0;
    return n // 5 + 1

def lowest_score(names, scores):
    names = np.array(names)
    scores = np.array(scores)
    idx = np.argmin(scores)
    return names[idx]

def sort_names(names, scores):
    names = np.array(names)
    scores = np.array(scores)
    # if len(names) != len(scores):
    idx_sorted = np.argsort(scores)[::-1]
    return names[idx_sorted]
    


print(ways(5))
print(lowest_score(['A', 'B', 'C'], [90, 80, 85]))
print(sort_names(['A', 'B', 'C'], [90, 80, 85]))