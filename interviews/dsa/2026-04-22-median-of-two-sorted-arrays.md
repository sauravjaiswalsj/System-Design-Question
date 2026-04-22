# Median of Two Sorted Arrays

Category: dsa
Date: 2026-04-22

**Median of Two Sorted Arrays System Design Discussion**

**Problem Statement:** Given two sorted arrays, find the median of the combined array.

**Requirements**

**Functional Requirements:**

1. Given two sorted arrays, the system should return the median of the combined array.
2. The system should handle arrays of any size.

**Non-Functional Requirements:**

1. **Performance:** The system should return the result within a reasonable time complexity (O(log(m+n))).
2. **Scalability:** The system should be able to handle large inputs with multiple threads.
3. **Efficiency:** The system should minimize memory usage.

**High-Level Architecture:**

1. **API Gateway:** Accepts input arrays and returns the median.
2. **Algorithm Module:** Implements the median calculation logic.
3. **Database (optional):** Stores the result cache for future requests.

**Database Design (if using caching):**

1. **Table:** `median_cache`
2. **Columns:** `array_1`, `array_2`, `median`
3. **Index:** `array_1`, `array_2` (for efficient lookups)

**Scaling Strategy:**

1. **Horizontal Scaling:** Add more machines to the algorithm module to handle increased load.
2. **Sharding:** Divide the input arrays into smaller chunks and process them in parallel.
3. **Caching:** Store frequently accessed result in the database to reduce computation.

**Median of Two Sorted Arrays solution using the First Principle of System Design:**

The first principle of system design is to "divide and conquer" complex problems. We can use the following approach:

1. **Divide:** Find the partition point in the combined array such that the elements on the left are less than or equal to the elements on the right.
2. **Conquer:** Recursively find the median in the left and right partitions.

**Algorithm:**

1. `findMedianSortedArrays(nums1, nums2)`:
    1. If `nums1` is longer than `nums2`, swap them to ensure `nums1` is the shorter array.
    2. Calculate the total length `m + n`.
    3. If `m + n` is odd, the median is the middle element. If `m + n` is even, the median is the average of the two middle elements.
    4. If `m + n` is odd, the partition point is `(m + n) / 2`. If `m + n` is even, the partition point is `(m + n) / 2 - 1` and `(m + n) / 2`.
    5. Recursively find the median in the left and right partitions.
    6. Combine the results to get the final median.

**Pseudocode:**
```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total_len = len(nums1) + len(nums2)
    if total_len % 2 == 1:
        partition = total_len // 2
    else:
        partition = (total_len // 2) - 1

    left, right = 0, len(nums1) - 1
    while True:
        i = (left + right) // 2
        j = partition - i - 2

        nums1_left = nums1[i] if i >= 0 else float('-infinity')
        nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
        nums2_left = nums2[j] if j >= 0 else float('-infinity')
        nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if total_len % 2 == 1:
                return min(nums1_right, nums2_right)
            else:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1
```

**Bottlenecks:**

1. **Scalability:** The recursive approach may lead to stack overflow for large inputs.
2. **Efficiency:** The algorithm has a time complexity of O(log(m+n)), but it may still be slow for very large inputs.

**Trade-offs:**

1. **Time complexity vs. Space complexity:** The algorithm has a time complexity of O(log(m+n)), but it uses O(1) extra space.
2. **Scalability vs. Accuracy:** The algorithm is designed to be scalable, but it may sacrifice accuracy for very large inputs.
3. **Efficiency vs. Readability:** The algorithm is designed to be efficient, but it may be less readable due to the recursive approach.

**Learning Links:**

* [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* [Binary Search](https://en.wikipedia.org/wiki/Binary_search)
* [Divide and Conquer](https://en.wikipedia.org/wiki/Divide_and_conquer_algorithm)
* [System Design Principles](https://www.guru99.com/system-design-principles.html)