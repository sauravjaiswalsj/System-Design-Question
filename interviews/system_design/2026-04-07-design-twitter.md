# Design Twitter

Category: system_design
Date: 2026-04-07

**Design Twitter System**

**1. Requirements (Functional + Non-functional)**

Functional Requirements:

- User Authentication and Authorization
- Tweet Creation and Posting
- Follow/Unfollow Users
- Search and Display Tweets
- Real-time Updates

Non-Functional Requirements:

- Scalability (Handling 500M+ users and 6,000 tweets/second)
- High Availability (99.99%)
- Low Latency (< 100ms)
- Data Consistency (Strong Consistency)
- Data Durability (Durability of 3 copies of data)

**2. High-Level Architecture**

- **Load Balancer**: Distributes incoming traffic across multiple instances of the application.
- **API Gateway**: Handles API requests, authentication, and rate limiting.
- **Application Server**: Handles business logic and interacts with the database.
- **Database**: Stores tweets, user information, and relationships between users.
- **Message Queue**: Handles real-time updates and notifications.
- **Caching Layer**: Reduces database queries and improves performance.

**3. Database Design**

- **Sharded Database**: Divide users into shards based on their IDs (e.g., user IDs 1-10^6 in one shard, 10^6-2*10^6 in another).
- **Horizontal Partitioning**: Store tweets and user information in separate tables.
- **Cache-aside Pattern**: Store frequently accessed data in a caching layer.

**Database Schema**

- **users** table: stores user information (id, username, etc.)
- **tweets** table: stores tweet information (id, user_id, text, etc.)
- **follows** table: stores follow relationships between users (user_id, followed_id, etc.)

**4. Scaling Strategy**

- **Horizontal Scaling**: Add more instances of the application and database as traffic increases.
- **Load Balancing**: Distribute traffic across instances using a load balancer.
- **Auto-scaling**: Automatically add or remove instances based on traffic.
- **Distributed Cache**: Use a distributed cache like Redis or Memcached to reduce database queries.

**5. Bottlenecks**

- **Database Queries**: High volume of queries can lead to performance issues.
- **Message Queue**: High volume of messages can lead to delays in real-time updates.
- **Network Latency**: High latency in communication between instances can lead to performance issues.

**6. Trade-offs**

- **Strong Consistency vs. Availability**: Implement strong consistency using distributed transactions, but sacrifice some availability in case of network partitions.
- **Cache vs. Database**: Use caching to reduce database queries, but sacrifice some data freshness.

**Design Twitter Solution using the First Principle of System Design**

The first principle of system design is: **"Keep it Simple, Stupid (KISS)**".

**Design Twitter Solution**

1. **Simplify the System**: Break down the system into smaller, independent components.
2. **Focus on Key Features**: Prioritize key features like user authentication, tweet posting, and search.
3. **Use Established Technologies**: Leverage established technologies like sharding, load balancing, and caching.
4. **Avoid Over-Engineering**: Avoid over-engineering the system to accommodate future scalability.
5. **Monitor and Optimize**: Monitor the system and optimize it as needed to ensure scalability and performance.

**References**

- [System Design Principles](https://en.wikipedia.org/wiki/System_design)
- [Sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture))
- [Load Balancing](https://en.wikipedia.org/wiki/Load_balancing_(computing))
- [Caching](https://en.wikipedia.org/wiki/Cache_(computing))
- [Scalability](https://en.wikipedia.org/wiki/Scalability)
- [Distributed Systems](https://en.wikipedia.org/wiki/Distributed_system)