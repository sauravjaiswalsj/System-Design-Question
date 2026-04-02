# Median of Two Sorted Arrays

Category: dsa
Date: 2026-04-02

**Median of Two Sorted Arrays System Design Discussion**

**Problem Statement:** Given two sorted arrays, find the median of the combined array.

**Requirements (Functional + Non-functional):**

* Functional Requirements:
	+ Find the median of two sorted arrays.
	+ Support arrays of various lengths.
	+ Support large input sizes.
* Non-functional Requirements:
	+ High performance (O(log n) time complexity).
	+ Scalability (handle large input arrays).
	+ Low memory usage.

**High-Level Architecture:**

1. **Input Processing:** Take two sorted arrays as input and validate their lengths.
2. **Median Calculation:** Use a binary search approach to find the median.
3. **Result Generation:** Return the calculated median.

**Database Design (Not applicable for this problem, as it's a standalone algorithm)**

**Scaling Strategy:**

1. **Distributed Binary Search:** Divide the input arrays into smaller chunks and perform binary search on each chunk. This approach can scale horizontally to handle large input sizes.
2. **Parallel Processing:** Use multiple threads or processes to perform binary search on each chunk concurrently, reducing overall processing time.

**Bottlenecks:**

1. **Binary Search Overhead:** The overhead of binary search can be significant for large input arrays.
2. **Memory Usage:** Large input arrays can consume excessive memory, causing performance issues.

**Trade-offs:**

1. **Time Complexity:** A binary search approach provides O(log n) time complexity, but it can be slower than a simple merge approach for small input sizes.
2. **Memory Usage:** A distributed binary search approach can reduce memory usage, but it adds overhead due to data transfer and synchronization.

**Solution using the First Principle of System Design (Separation of Concerns):**

1. **Separate Input Processing and Median Calculation:** Break down the problem into two distinct components: input processing and median calculation.
2. **Use a Binary Search Approach for Median Calculation:** Utilize a binary search approach to find the median, separating the calculation from the input processing.
3. **Decouple Result Generation from Median Calculation:** Return the calculated median without coupling it to the input processing.

**Median of Two Sorted Arrays Solution:**

```python
def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array to simplify logic
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    total_len = len(nums1) + len(nums2)
    half_len = total_len // 2

    left = 0
    right = len(nums1) - 1

    while True:
        # Find the partition for nums1
        i = (left + right) // 2
        # Find the corresponding partition for nums2
        j = half_len - i - 2

        nums1_left = nums1[i] if i >= 0 else float('-infinity')
        nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else float('infinity')
        nums2_left = nums2[j] if j >= 0 else float('-infinity')
        nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else float('infinity')

        # Check if the partitions are correct
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Check if the total length is odd or even
            if total_len % 2 == 0:
                # Return the average of the two middle elements
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            else:
                # Return the middle element
                return min(nums1_right, nums2_right)
        # Adjust the partition for nums1
        elif nums1_left > nums2_right:
            right = i - 1
        else:
            left = i + 1
```

This solution follows the first principle of system design by separating input processing and median calculation, using a binary search approach for median calculation, and decoupling result generation from median calculation.