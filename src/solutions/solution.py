
# def two_sum(nums, target):
#     # Create a dictionary to store the difference and its index
#     num_to_index = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in num_to_index:
#             return [num_to_index[diff], i]  # Return indices if solution found
#         num_to_index[num] = i  # Store the index of the current number
#     return []  # Return an empty list if no solution is found

# # Input vector size
# size = int(input().strip())

# # Input vector elements
# nums = list(map(int, input().strip().split()))

# # Input target value
# target = int(input().strip())

# # Ensure the vector size matches the input size
# # if len(nums) != size:
# #     print("Error: The number of vector elements does not match the specified size.")
# # else:
# #     # Get the result
# result = two_sum(nums, target)

#     # Display the output
#     # if result:
# print(*result)  # Print the indices without brackets
#     # else:
#     #     print("No solution found.")



class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:  # Handle overflow
                return 0
        return sign * rev

# Input the integer to be reversed
line = input().strip()
x = int(line.split('=')[1].strip())  # If the input is 'x = 123'

# Create an instance of the Solution class
solution = Solution()

# Get the reversed integer
result = solution.reverse(x)

# Display the output
print(result)
