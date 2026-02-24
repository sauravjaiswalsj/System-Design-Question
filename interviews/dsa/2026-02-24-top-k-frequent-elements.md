# Top K Frequent Elements

Category: dsa
Date: 2026-02-24

**Top K Frequent Elements System Design Discussion**

### 1. Requirements (Functional + Non-functional)

**Functional Requirements:**

* Given an array of integers, find the top K most frequent elements.
* Return the elements in descending order of frequency.

**Non-functional Requirements:**

* High performance: Handle large input arrays (e.g., 10^6 elements) with minimal latency.
* Memory efficiency: Optimize memory usage to handle large inputs.

### 2. High-Level Architecture

We will use a distributed system architecture to handle large inputs. The architecture consists of three layers:

1. **Load Balancer**: Distributes incoming requests across multiple worker nodes.
2. **Worker Node**: Processes the input array, counts frequencies, and stores them in a distributed hash table (DHT).
3. **Result Node**: Combines the frequency counts from all worker nodes and returns the top K elements.

**Technology Stack:**

* Load Balancer: HAProxy or NGINX
* Worker Node: Java/Scala with Apache Cassandra (DHT) or Redis
* Result Node: Java/Scala with Apache Cassandra (DHT) or Redis

### 3. Database Design

We will use a distributed hash table (DHT) to store the frequency counts. Each worker node will store the frequency counts for a subset of the input array.

**DHT Design:**

* Use Apache Cassandra or Redis as the DHT.
* Define a key-space for the frequency counts, e.g., `element-frequency-{worker-node-id}`.
* Store the frequency count for each element in the DHT, e.g., `{element-frequency-{worker-node-id}} -> {element-id}:{frequency}`.

### 4. Scaling Strategy

To handle large inputs, we can scale the system horizontally by adding more worker nodes. Each worker node will process a subset of the input array and store the frequency counts in the DHT.

**Scaling Strategy:**

* Add more worker nodes to the system as the input size increases.
* Use a load balancer to distribute incoming requests across the worker nodes.
* Use a distributed hash table (DHT) to store the frequency counts, allowing multiple worker nodes to access the same data.

### 5. Bottlenecks

The following are potential bottlenecks in the system:

* **DHT Write Performance**: The DHT write performance may degrade as the number of worker nodes increases.
* **Result Node Processing**: The result node may become a bottleneck as the number of worker nodes increases.
* **Network Latency**: Network latency may impact the system performance, especially if the worker nodes and result node are located in different data centers.

### 6. Trade-offs

The following are trade-offs in the system design:

* **Memory vs. Scalability**: Increasing the memory capacity of each worker node may improve performance, but may also limit the scalability of the system.
* **DHT Write Performance vs. Read Performance**: Optimizing DHT write performance may impact read performance, and vice versa.
* **Result Node Processing vs. Distributed Computing**: Using a result node to combine the frequency counts may improve performance, but may also limit the scalability of the system.

### Top K Frequent Elements Solution using the First Principle of System Design

The first principle of system design is to "Keep it Simple, Stupid" (KISS). In this case, we can use a simple algorithm to find the top K frequent elements:

1. Count the frequency of each element in the input array.
2. Sort the elements by frequency in descending order.
3. Return the top K elements.

However, this algorithm may not be efficient for large inputs. To improve performance, we can use a distributed system architecture and a distributed hash table (DHT) to store the frequency counts.

**Code Example:**

```scala
// Define a class to represent a frequency count
case class FrequencyCount(elementId: Int, frequency: Int)

// Define a class to represent the Top K Frequent Elements result
case class TopKFrequentElements(k: Int, result: List[FrequencyCount])

// Define a function to count the frequency of each element
def countFrequency(inputArray: Array[Int]): Map[Int, Int] = {
  inputArray.groupBy(identity).mapValues(_.size)
}

// Define a function to find the top K frequent elements
def findTopKFrequentElements(inputArray: Array[Int], k: Int): TopKFrequentElements = {
  val frequencyCounts = countFrequency(inputArray)
  val sortedFrequencyCounts = frequencyCounts.toList.sortBy(_._2)(Ordering.Int.reverse)
  val topKFrequentElements = sortedFrequencyCounts.take(k).map { case (elementId, frequency) => FrequencyCount(elementId, frequency) }
  TopKFrequentElements(k, topKFrequentElements)
}
```

Note that this is a simplified example and may not be suitable for production use. A more robust solution would involve using a distributed system architecture and a distributed hash table (DHT) to store the frequency counts.