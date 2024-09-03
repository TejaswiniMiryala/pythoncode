def generate_range(min_val, max_val, step):
    return list(range(min_val, max_val + 1, step))
# Function to process multiple test cases
def process_test_cases(test_cases):
    result = []
    for case in test_cases:
        min_val, max_val, step = case
        result.append(generate_range(min_val, max_val, step))
    return result

# Reading input
T = int(input("Enter number of test cases: "))
test_cases = []

for _ in range(T):
    case = list(map(int, input().split()))
    test_cases.append(case)

# Generating output
output = process_test_cases(test_cases)

# Printing output
for o in output:
    print(o)
