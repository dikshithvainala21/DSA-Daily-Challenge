def two_sum(numbers, target):
    """
    Find two numbers in the list that add up to the target value.

    Args:
        numbers (list): A list of integers.
        target (int): The target sum."""

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return None
numbers = [2, 7, 11, 15]
target = 9  
result = two_sum(numbers, target)
if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")
else:
    print(f"No two numbers found that add up to {target}.")