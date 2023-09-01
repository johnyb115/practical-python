"""
Exercise 1.5.

bounce.py
"""
initial_height = 100    # Meters
n_bounces = 10
act_height = 0
for bounce in range(n_bounces):
    act_height = initial_height*(3/5)
    initial_height = act_height
    print(f'{bounce+1} {round(act_height, 4)}')