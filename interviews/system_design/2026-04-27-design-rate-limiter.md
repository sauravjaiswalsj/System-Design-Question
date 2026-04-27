# Design Rate Limiter

Category: system_design
Date: 2026-04-27

**System Design Discussion: Rate Limiter**

**Requirements**

**Functional Requirements:**

1. Implement a rate limiter that restricts the frequency of requests from a user or IP address.
2. Allow for adjustable limits (e.g., 5 requests per minute).
3. Support both fixed and sliding window algorithms.
4. Provide APIs for adding, removing, and retrieving users/IPs from the rate limiter.

**Non-Functional Requirements:**

1. Scalability: handle a large number of users/IPs.
2. Performance: respond to requests within 50ms.
3. Fault Tolerance: recover from database failures.

**High-Level Architecture**

1. **Rate Limiter Service** (Microservice):
	* Handles incoming requests from clients.
	* Interacts with the database to store and retrieve user/IP data.
	* Implements the rate limiter algorithm.
2. **Database** (Redis or MySQL):
	* Stores user/IP data, including request counts and timestamps.
	* Supports high concurrency and low-latency operations.
3. **API Gateway** (Optional):
	* Acts as an entry point for client requests.
	* Routes requests to the Rate Limiter Service.

**Database Design**

1. **User/IP Table**:
	* Stores user/IP data, including ID, IP address, and request counts.
	* Index on IP address for efficient updates.
2. **Request Log Table**:
	* Stores individual request logs, including timestamp and user/IP ID.
	* Index on timestamp for efficient query.

**Scaling Strategy**

1. **Horizontal Scaling**:
	* Add more Rate Limiter Service instances behind a load balancer.
	* Use a distributed database (e.g., Redis Cluster) for high availability.
2. **Vertical Scaling**:
	* Increase the power of individual Rate Limiter Service instances.
	* Increase database instance power (e.g., larger MySQL instance).

**Bottlenecks**

1. **Database Write-Throughput**: high insertion rates can lead to performance degradation.
2. **Load Balancer**: becomes a bottleneck as the number of Rate Limiter Service instances increases.

**Trade-offs**

1. **Fixed Window vs. Sliding Window**: fixed window offers more predictable behavior, while sliding window provides better adaptability to changing rates.
2. **Database Choice**: Redis provides high performance and low latency, but may lack fault tolerance; MySQL offers strong consistency, but may require more resources.

**Design using the First Principle of System Design**

The first principle of system design is to **simplify the problem by minimizing the number of variables involved**.

In this case, we can simplify the problem by:

1. Decoupling the rate limiter logic from the database.
2. Using a distributed database (e.g., Redis Cluster) for high availability.
3. Implementing a fixed window algorithm for predictable behavior.

By simplifying the problem, we can reduce the number of variables involved and make the system easier to design, implement, and scale.

**Additional Learning Links**

* Rate Limiter Algorithms: [1, 2]
* Distributed Database: [1, 2]
* System Design Principles: [1, 2]

References:

[1] "Designing Data-Intensive Applications" by Martin Kleppmann
[2] "System Design Interview" by Alex Xu
[3] "Rate Limiting in Distributed Systems" by AWS
[4] "Distributed Database" by Cloudflare