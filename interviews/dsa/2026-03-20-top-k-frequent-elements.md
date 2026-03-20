# Top K Frequent Elements

Category: dsa
Date: 2026-03-20

**Top K Frequent Elements System Design**

**Requirements**

Functional Requirements:

1. Input: A stream of integers (e.g., from a web service or file)
2. Output: The top K frequent elements in the stream, along with their frequencies
3. Real-time processing: Handle new elements as they arrive in the stream

Non-Functional Requirements:

1. Scalability: Support a large volume of incoming stream data (e.g., millions of elements per second)
2. Low latency: Respond to queries within a few milliseconds
3. Data consistency: Ensure accurate frequency counts for all elements

**High-Level Architecture**

1. **Stream Processor**: Collects and processes the incoming stream data
2. **Frequency Counter**: Maintains a data structure to store the frequency of each element
3. **Query Service**: Handles Top K queries from clients

**Database Design**

For the Frequency Counter, we'll use a combination of in-memory data structures and a database for persistence. This design balances performance and data durability:

1. **In-memory hash map** (e.g., Java's `ConcurrentHashMap`): Stores the frequency of each element for fast lookups and updates
2. **Redis or Memcached**: Stores the frequency counts in a database for persistence and scalability

**Scaling Strategy**

To handle a large volume of incoming stream data:

1. **Distributed Stream Processor**: Use a distributed streaming system like Apache Kafka, Apache Storm, or Flink to process the stream in parallel
2. **Horizontal scaling**: Add more nodes to the Frequency Counter and Query Service to handle increased loads
3. **Caching**: Use Redis or Memcached to cache frequent elements and reduce database queries

**Solution using the First Principle of System Design**

The first principle of system design states: "Simpllicity is the ultimate sophistication."

Our solution is simple and effective, with a clear separation of concerns:

1. **Stream Processor**: Focuses on collecting and processing the stream data
2. **Frequency Counter**: Maintains the frequency counts with a simple in-memory hash map
3. **Query Service**: Handles Top K queries with a simple database query

By following this principle, we've avoided unnecessary complexity and ensured a scalable, high-performance system.

**Bottlenecks**

Potential bottlenecks:

1. **Stream Processor**: Overwhelmed by a high volume of incoming stream data
2. **Frequency Counter**: Struggles to keep up with the frequency updates
3. **Query Service**: Faces high latency due to database queries

To mitigate these bottlenecks, we'll implement horizontal scaling, caching, and efficient data structures.

**Trade-offs**

Trade-offs:

1. **Scalability vs. Complexity**: A more complex system may be necessary for extreme scalability
2. **Latency vs. Data Consistency**: Balancing low latency with accurate frequency counts may require compromises
3. **Memory vs. Disk Storage**: Choosing between in-memory and disk-based storage depends on the specific use case

**Additional Reading**

* Apache Kafka: [https://kafka.apache.org/](https://kafka.apache.org/)
* Apache Storm: [https://storm.apache.org/](https://storm.apache.org/)
* Redis: [https://redis.io/](https://redis.io/)
* Memcached: [https://memcached.org/](https://memcached.org/)
* Java's `ConcurrentHashMap`: [https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ConcurrentHashMap.html)