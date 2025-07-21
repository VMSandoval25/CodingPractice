def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)
    minLength = float('inf')
    left = 0
    current_sum = 0

    for right in range(n):
        current_sum += nums[right]
        print(f"Right: {right}, Sum: {current_sum}")
        
        while current_sum >= target:
            print(f"MinLength Before: {minLength}")
            minLength = min(minLength, right - left + 1)
            print(f"Right - Left + 1 = {right - left + 1}")
            print(f"MinLength After: {minLength}")
            current_sum -= nums[left]
            print(f"Current Sum: {current_sum}")
            left += 1

minSubArrayLen(7, [2,3,1,2,4,3])