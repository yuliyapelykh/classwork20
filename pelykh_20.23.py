import numpy as np

num_simulations = 1000000

num_red_balls = 4
num_blue_balls = 4
num_black_balls = 4

def contains_at_least_two_black_balls(draw):
    black_count = np.sum(draw == "Чорний")
    return black_count >= 2

simulations = np.random.choice(["Червоний", "Синій", "Чорний"], size=(num_simulations, 3), p=[num_red_balls / 12, num_blue_balls / 12, num_black_balls / 12])

satisfying_simulations = np.apply_along_axis(contains_at_least_two_black_balls, axis=1, arr=simulations)
probability = np.mean(satisfying_simulations)

print("Ймовірність того, що з трьох кульок не менше 2 чорних:", probability)