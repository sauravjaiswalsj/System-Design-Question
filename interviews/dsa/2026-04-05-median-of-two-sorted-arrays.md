# Median of Two Sorted Arrays

Category: dsa
Date: 2026-04-05

**Median of Two Sorted Arrays**

**Problem Statement:**
Given two sorted arrays, find the median of the combined array.

**Requirements (Functional + Non-functional):**

* Functional Requirements:
	+ Given two sorted arrays, return the median of the combined array.
	+ Handle edge cases: empty arrays, arrays with single elements, arrays with even and odd lengths.
* Non-functional Requirements:
	+ Time complexity: O(log(min(n, m))), where n and m are the lengths of the two arrays.
	+ Space complexity: O(1), excluding the output array.
	+ Scalability: handle large input arrays (e.g., millions of elements).
	+ Robustness: handle edge cases and invalid input.

**High-Level Architecture:**

1. **Input**: Two sorted arrays.
2. **Median Calculation**:
	* Use a modified binary search approach to find the median.
	* Divide the arrays into two halves and calculate the median using the following steps:
		+ Find the middle index of the combined array.
		+ Compare the elements at the middle index in both arrays.
		+ If one array has a smaller element, discard the smaller array and move the middle index to the other array.
		+ Repeat until the middle index is between the two arrays.
	* Calculate the median using the elements at the middle index.
3. **Output**: The median of the combined array.

**Database Design:**

No database design is required for this problem, as it involves only array operations.

**Scaling Strategy:**

1. **Horizontal Scaling**: Add more machines to the cluster to handle larger input arrays.
2. **Load Balancing**: Distribute the workload across multiple machines to avoid bottlenecks.
3. **Caching**: Cache the results of expensive operations (e.g., sorting arrays) to improve performance.

**Bottlenecks:**

1. **Sorting**: Sorting the combined array can be an expensive operation.
2. **Memory**: Handling large input arrays can lead to memory issues.

**Trade-offs:**

1. **Time complexity vs. Space complexity**: Achieving O(log(min(n, m))) time complexity requires additional space for storing the merged array.
2. **Scalability vs. Robustness**: Improving scalability may compromise robustness, especially when handling edge cases.

**Median of Two Sorted Arrays Solution using the First Principle of System Design:**

The first principle of system design is to **"start with the problem statement and identify the key requirements."**

1. **Problem Statement**: Find the median of the combined array.
2. **Key Requirements**: Time complexity: O(log(min(n, m))), Space complexity: O(1).
3. **System Design**: Use a modified binary search approach to find the median.
4. **Implementation**: Implement the binary search approach and test it with edge cases.

**Example Implementation in Python:**
```python
def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else nums1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else nums2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
```
This implementation uses a modified binary search approach to find the median of the combined array in O(log(min(n, m))) time complexity.

**Learning Links:**

* Binary Search: [https://en.wikipedia.org/wiki/Binary_search](https://en.wikipedia.org/wiki/Binary_search)
* Median Finding: [https://en.wikipedia.org/wiki/Median](https://en.wikipedia.org/wiki/Median)
* System Design Principles: [https://www.toptal.com/system-design/system-design-primer](https://www.toptal.com/system-design/system-design-primer)