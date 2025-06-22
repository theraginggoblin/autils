import random
import math
import statistics

def run_test_sim(size: int, num_d6: int = 4):
    results = []
    for x in range (0, size):
        a_sum = sum([random.randint(1,6) for x in range(0, num_d6)])
        results.append(a_sum)
    
    return results

def calculate_standard_deviation(a_list, mean: float = None):
    differences = []
    if mean is None:
        mean = statistics.mean(a_list)
    for value in a_list:
        square_distance_from_mean = math.pow((mean - value),2)
        differences.append(square_distance_from_mean)
    variance = statistics.mean(differences)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

def get_uncertainty(a_list):
    return calculate_standard_deviation(a_list) / math.sqrt(len(a_list))

#https://stats.stackexchange.com/questions/28987/calculate-number-of-needed-simulations
def calculate_number_of_simulations_reqired(a_list):
    mean = statistics.mean(a_list)
    standard_deviation = calculate_standard_deviation(a_list, mean)
    error = 0.05
    uncertainty = 0.05
    above_line = (1 - (uncertainty / 2) * standard_deviation)
    below_line = error * mean
    in_brackets = above_line / below_line
    simulations_required = math.pow(in_brackets, 2)
    return simulations_required * len(a_list)

results = run_test_sim(10000, num_d6 = 8)
num_simulations_required = calculate_number_of_simulations_reqired(results)
print(f"static list number of simulations required: {num_simulations_required}")

print(f"uncertainty of static list: {get_uncertainty(results)}")

print("running another test sim to see if above is accurate")
auto_results = run_test_sim(int(num_simulations_required))
print(f"uncertainty of automatically determined test run: {get_uncertainty(auto_results)}")

# run_test_sim(int(num_simulations_required))
# print(f"uncertainty of automatically determined test run: {get_uncertainty(auto_results)}")