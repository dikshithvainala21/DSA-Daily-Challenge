def two_sum(nums, target):
    """
    Return the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): The input array of integers.
        target (int): The target sum.

    Returns:
        list[int]: A list containing the indices [i, j] if found; otherwise []
    """
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum(numbers, target)

    if result:
        print(f"Indices of the two numbers that add up to {target}: {result}")
    else:
        print(f"No two numbers found that add up to {target}.")
