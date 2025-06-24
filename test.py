
from typing import List
import random
import math
import statistics


##############################
# unused functions but keeping because i learnt stuff
##############################

# this is biased for sample variance calculation because statistics.mean divides by n rather than n - 1
def calculate_standard_deviation(a_list, mean: float = None):
    differences = []
    if mean is None:
        mean = statistics.mean(a_list)
    for value in a_list:
        square_distance_from_mean = math.pow((mean - value), 2)
        differences.append(square_distance_from_mean)
    variance = statistics.mean(differences)
    standard_deviation = math.sqrt(variance)
    return standard_deviation



def run_test_sim(size: int, num_d6: int = 4) -> List[int]:
    results: List[int] = []
    for x in range(0, size):
        results.append(sum(random.randint(1, 6) for x in range(0, num_d6)))
    return results



def get_standard_error(a_list: List[int]) -> float:
    return statistics.stdev(a_list) / math.sqrt(len(a_list))


def calculate_number_of_simulations_required_attempt2(a_list: List[int]) -> float:
    acceptable_uncertainty: float = 0.05
    standard_error: float = get_standard_error(a_list)

    # IE if actual uncertainty is 0.10 and acceptable is 0.05 will get 2
    divided: float = standard_error / acceptable_uncertainty

    # continuing on with example. 2 to the power of 2 is four. we do need to lower uncertainty by half and in a normal distribution stdev is reduced by half every 4n. 2 to the power of 2 is 4
    squared_divided: float = divided ** 2
    return math.ceil(squared_divided * len(a_list))


num_d6: int = 8
results: List[int] = run_test_sim(10000, num_d6=num_d6)

num_simulations_required: int = calculate_number_of_simulations_required_attempt2(results)
print(f"determined number of simulations required: {num_simulations_required}")
print(f"uncertainty of results: {get_standard_error(results)}")

print("verify suggested number of runs")
auto_results = run_test_sim(num_simulations_required, num_d6=num_d6)
print(f"uncertainty of suggested number of runs: {get_standard_error(auto_results)}")
