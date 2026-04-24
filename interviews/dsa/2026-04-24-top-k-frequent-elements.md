# Top K Frequent Elements

Category: dsa
Date: 2026-04-24

**System Design Discussion: Top K Frequent Elements**

**Problem Statement:**
Given a large dataset of integers, return the top K frequent elements.

**Requirements (Functional + Non-functional):**

Functional Requirements:

1. Retrieve the top K frequent elements from a large dataset of integers.
2. The system should handle a large volume of data (e.g., billions of integers).
3. The system should be able to process data in real-time.

Non-functional Requirements:

1. Scalability: The system should be able to handle increasing data volume and user load.
2. Performance: The system should be able to process data efficiently.
3. Fault tolerance: The system should be able to recover from failures and data corruption.

**High-Level Architecture:**

1. **Data Ingestion Layer**:
	* Use a message queue (e.g., Apache Kafka) to handle data ingestion.
	* Process data in batches to reduce latency.
2. **Frequent Element Counting Layer**:
	* Use a distributed hash table (e.g., Apache Cassandra) to store frequency counts.
	* Implement a data structure (e.g., Trie, Counter) to efficiently count frequencies.
3. **Top K Retrieval Layer**:
	* Use a sorted set (e.g., Redis) to maintain a top K frequency list.
	* Implement a data structure (e.g., heap, priority queue) to efficiently retrieve top K elements.

**Database Design:**

1. **Frequent Element Counting Layer (Apache Cassandra)**:
	* Use a partitioned column family (PCF) to store frequency counts.
	* Define a composite key (e.g., integer value, frequency count) to facilitate efficient counting.
2. **Top K Retrieval Layer (Redis)**:
	* Use a sorted set to store top K frequency elements.
	* Define a score (e.g., frequency count) to facilitate efficient retrieval.

**Scaling Strategy:**

1. **Horizontal Scaling**:
	* Add more nodes to the Cassandra cluster to increase storage capacity.
	* Add more instances to the Redis cluster to increase retrieval capacity.
2. **Vertical Scaling**:
	* Increase memory and CPU resources on each node to improve performance.
3. **Sharding**:
	* Shard data across multiple Cassandra clusters to improve data locality.
	* Shard data across multiple Redis clusters to improve retrieval efficiency.

**Bottlenecks:**

1. **Data Ingestion Layer**:
	* High data ingestion latency due to batch processing.
2. **Frequent Element Counting Layer**:
	* High frequency counting latency due to Cassandra's partitioning.
3. **Top K Retrieval Layer**:
	* High retrieval latency due to Redis's sorted set implementation.

**Trade-offs:**

1. **Scalability vs. Complexity**:
	* A more complex system design may provide better scalability but may also introduce additional latency and overhead.
2. **Performance vs. Fault Tolerance**:
	* A faster system design may sacrifice fault tolerance to improve performance.

**Solution using the First Principle of System Design:**

The first principle of system design is "do the simplest thing that could possibly work." In this case, we can use a simple data structure, such as a hash table, to count frequencies and store top K elements. However, this approach may not scale well and may introduce high latency.

To improve performance, we can use a more complex data structure, such as a Trie or a Counter, to efficiently count frequencies. However, this approach may introduce additional latency and overhead.

**Code Example:**
```python
import collections
import heapq

def top_k_frequent(nums, k):
    freq = collections.Counter(nums)
    heap = []
    for num, count in freq.items():
        heapq.heappush(heap, (-count, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]
```
This implementation uses a hash table to count frequencies and a heap to efficiently retrieve top K elements. However, this approach may not scale well for large datasets.

**Learning Links:**

1. Apache Kafka: <https://kafka.apache.org/>
2. Apache Cassandra: <https://cassandra.apache.org/>
3. Redis: <https://redis.io/>
4. Trie: <https://en.wikipedia.org/wiki/Trie>
5. Counter: <https://docs.python.org/3/library/collections.html#collections.Counter>
6. Heap: <https://en.wikipedia.org/wiki/Heap_(data_structure)>
7. Priority Queue: <https://en.wikipedia.org/wiki/Priority_queue>