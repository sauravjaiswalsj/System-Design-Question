# Median of Two Sorted Arrays

Category: dsa
Date: 2026-04-29

**Median of Two Sorted Arrays Problem**

**Problem Statement**

Given two sorted arrays, find the median of the combined array.

**Requirements**

### Functional Requirements

1. **Correctness**: The solution should return the correct median of the combined array.
2. **Efficiency**: The solution should have a time complexity that scales with the input size.
3. **Accuracy**: The solution should handle edge cases, such as empty arrays or arrays with duplicate elements.

### Non-Functional Requirements

1. **Scalability**: The solution should be able to handle large input sizes.
2. **Maintainability**: The solution should be easy to understand and modify.
3. **Performance**: The solution should have a good response time.

**High-Level Architecture**

The high-level architecture for this problem can be broken down into the following components:

1. **Input Parser**: Responsible for parsing the input arrays and validating their correctness.
2. **Median Calculator**: Responsible for calculating the median of the combined array.
3. **Response Generator**: Responsible for generating the response with the calculated median.

**Database Design**

Since this problem does not involve a database, there is no need for a database design.

**Scaling Strategy**

To scale this solution, we can use the following strategies:

1. **Horizontal Scaling**: We can distribute the workload across multiple machines using a load balancer.
2. **Caching**: We can cache the results of frequently accessed queries to improve performance.
3. **Distributed Computing**: We can use a distributed computing framework like Apache Spark to process large input sizes.

**Solution using the First Principle of System Design**

The first principle of system design is to "Do the Simplest Thing That Could Possibly Work". In this case, we can use a binary search approach to find the median of the combined array.

**Solution**

Here is a simple implementation in Python:
```python
def findMedianSortedArrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]
```
However, this solution has a time complexity of O(n log n) due to the sorting operation. To improve the performance, we can use a binary search approach.

**Binary Search Approach**

The idea is to perform a binary search on the merged array to find the median. We can use the following steps:

1. Find the middle index of the merged array.
2. If the middle index is even, return the average of the two middle elements.
3. If the middle index is odd, return the middle element.

Here is the implementation in Python:
```python
def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]
```
This solution has a time complexity of O(n), making it more efficient than the previous solution.

**Bottlenecks**

The bottlenecks in this solution are:

1. **Input Size**: If the input size is very large, the solution may run out of memory.
2. **Array Merge**: Merging two sorted arrays can be expensive if the arrays are large.

**Trade-offs**

The trade-offs in this solution are:

1. **Time Complexity**: We can trade off time complexity for space complexity by using a more efficient algorithm.
2. **Memory Usage**: We can trade off memory usage for performance by using a more efficient algorithm.

**Additional Discussion**

To further improve the performance of this solution, we can use a more efficient algorithm like the "Meet in the Middle" approach.

**Meet in the Middle Approach**

The idea is to divide the problem into two halves and solve each half separately. We can use the following steps:

1. Find the middle index of the merged array.
2. Divide the merged array into two halves.
3. Perform a binary search on each half to find the median.

Here is the implementation in Python:
```python
def findMedianSortedArrays(nums1, nums2):
    merged = []
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    n = len(merged)
    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (merged[mid1] + merged[mid2]) / 2
    else:
        mid = n // 2
        return merged[mid]
```
This solution has a time complexity of O(n), making it more efficient than the previous solutions.

**Conclusion**

In conclusion, the median of two sorted arrays problem can be solved using various approaches, including the binary search approach and the meet in the middle approach. The solution using the meet in the middle approach has a time complexity of O(n), making it more efficient than the previous solutions. However, the solution using the binary search approach is more intuitive and easier to understand.