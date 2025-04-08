import numpy as np

def simulate_trajectory():
    return np.random.rand(5)

def compare_traj(traj1, traj2, noise=0.2):
    score1 = np.sum(traj1)
    score2 = np.sum(traj2)
    preferred = 0 if score1 > score2 else 1
    if np.random.rand() < noise:
        preferred = 1 - preferred
    return preferred

for i in range(10):
    t1 = simulate_trajectory()
    t2 = simulate_trajectory()
    pref = compare_traj(t1, t2)
    print(f"Comparison {i+1}: Preferred Trajectory - {pref}")
