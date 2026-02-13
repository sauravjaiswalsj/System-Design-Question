# Design Twitter

Date: 2026-02-13

**System Design Discussion: Design Twitter**

**1. Requirements (Functional + Non-functional)**

- **Functional Requirements:**
  - User Registration and Login
  - Posting Tweets (max 280 characters)
  - Viewing and Filtering Tweets
  - Replying and Retweeting
  - Hashtag Support
  - User Profile Management (e.g., followers, following, bio)
  - Search functionality for tweets and users
- **Non-Functional Requirements:**
  - High Availability (99.99% uptime)
  - Scalability to handle 100 million users
  - Low latency (< 1s) for tweet posting and retrieval
  - Data consistency across all regions
  - Support for at least 500,000 tweets per second
  - Data retention for a minimum of 6 months

**2. High-Level Architecture**

- **Components:**
  - **1. API Gateway:** Load balancer and API entry point for the system (e.g., NGINX)
  - **2. Load Balancer:** Distributes traffic across multiple instances of the application (e.g., HAProxy)
  - **3. Application Server:** Handles tweet posting, retrieval, and user management (e.g., Java, Node.js, or Python)
  - **4. Database:** Stores tweet data, user information, and relationships (e.g., MySQL, PostgreSQL, or Cassandra)
  - **5. Message Queue:** Handles asynchronous tasks, such as sending notifications and processing tweets (e.g., RabbitMQ or Apache Kafka)
  - **6. Cache:** Reduces database load and improves performance for frequently accessed data (e.g., Redis or Memcached)
- **Communication:**
  - API Gateway -> Load Balancer
  - Load Balancer -> Application Server
  - Application Server -> Database
  - Application Server -> Message Queue
  - Application Server -> Cache

**3. Database Design**

- **Schema:**
  - **Users Table:** stores user information (id, username, password, bio, etc.)
  - **Tweets Table:** stores tweet data (id, user_id, text, timestamp, etc.)
  - **Followers Table:** stores user relationships (user_id, followed_id)
  - **Hashtags Table:** stores hashtag data (id, text)
  - **Tweet_Hashtags Table:** stores tweet-hashtag relationships (tweet_id, hashtag_id)
- **Indexing:**
  - Create indexes on user_id, followed_id, and tweet_id to improve query performance

**4. Scaling Strategy**

- **Horizontal Scaling:** Add more application servers and load balancers to handle increased traffic
- **Vertical Scaling:** Increase the power of individual application servers and load balancers to handle increased traffic
- **Database Sharding:** Split the database into smaller, independent pieces to improve performance and scalability
- **Read Replicas:** Create read-only copies of the database to improve read performance and reduce load on the primary database

**5. Bottlenecks**

- **Database Bottleneck:** Tweet posting and retrieval may become slow due to high traffic and data volume
- **Message Queue Bottleneck:** Processed tweets may become delayed due to high load on the message queue

**6. Trade-offs**

- **Database vs. Cache:** Trade-off between data consistency and performance. Using a cache can improve performance but may lead to data inconsistencies
- **Scalability vs. Cost:** Trade-off between scalability and cost. Adding more resources may improve scalability but increase costs
- **Data Retention vs. Storage:** Trade-off between data retention and storage. Retaining more data may improve user experience but increase storage costs