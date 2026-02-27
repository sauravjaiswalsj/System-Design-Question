# Median of Two Sorted Arrays

Category: dsa
Date: 2026-02-27

**Median of Two Sorted Arrays Problem Statement**

Given two sorted arrays, find the median of the combined array. If the total number of elements is odd, the median is the middle element. If the total number of elements is even, the median is the average of the two middle elements.

**Requirements (Functional + Non-functional)**

Functional Requirements:

1. Given two sorted arrays, return the median of the combined array.
2. Handle edge cases where one or both arrays are empty.
3. Handle edge cases where one or both arrays are very large.

Non-functional Requirements:

1. Efficiency: The algorithm should have a time complexity of O(log(m+n)), where m and n are the sizes of the two input arrays.
2. Scalability: The algorithm should be able to handle large input arrays.
3. Code quality: The code should be concise and well-structured.

**High-Level Architecture**

The high-level architecture for this problem can be broken down into the following components:

1. **Input Handler**: Responsible for parsing and validating the input arrays.
2. **Median Calculator**: Responsible for calculating the median of the combined array.
3. **Output Handler**: Responsible for formatting and returning the result.

**Database Design**

Since this problem does not require a database, we can skip this step.

**Scaling Strategy**

To scale the solution, we can use a binary search approach to find the median in O(log(m+n)) time complexity. Here's an example implementation in Python:

```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    total_length = len(nums1) + len(nums2)
    half_length = total_length // 2
    
    left = 0
    right = len(nums1) - 1
    
    while True:
        i = (left + right) // 2
        j = half_length - i - 2
        
        nums1_left = nums1[i] if i >= 0 else float("-infinity")
        nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float("infinity")
        nums2_left = nums2[j] if j >= 0 else float("-infinity")
        nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float("infinity")
        
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if total_length % 2:
                return min(nums1_right, nums2_right)
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1
```

**Bottlenecks**

The bottleneck of this solution is the while loop, which runs in O(log(m+n)) time complexity. However, if the input arrays are very large, the binary search approach may not be efficient due to the overhead of function calls and array indexing.

**Trade-offs**

The trade-off of this solution is the use of binary search, which reduces the time complexity to O(log(m+n)) but increases the code complexity. An alternative solution using a sorting approach would have a time complexity of O((m+n)log(m+n)) but would be simpler to implement.

**First Principle of System Design:**

The first principle of system design is to **divide and conquer**. This means breaking down the problem into smaller sub-problems, solving each sub-problem independently, and then combining the solutions to solve the original problem.

In the case of the Median of Two Sorted Arrays problem, we can divide the problem into the following sub-problems:

1. **Find the median of a single sorted array**: This sub-problem can be solved using a simple binary search approach.
2. **Combine two sorted arrays**: This sub-problem can be solved using a merge approach.
3. **Find the median of the combined array**: This sub-problem can be solved using a binary search approach.

By dividing the problem into these sub-problems, we can solve each sub-problem independently and then combine the solutions to solve the original problem. This approach reduces the time complexity of the solution to O(log(m+n)).