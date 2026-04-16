# Practical Resources for System Design and ML interview Questions (repo+website)

Category: ml_system_design
Date: 2026-04-16

**Practical Resources for System Design and ML Interview Questions**

**Problem Description:**
Design a system to host and share practical resources for system design and machine learning interview questions.

**Requirements:**

1. **Functional Requirements:**
	* Users can create and manage accounts.
	* Users can upload and share resources (e.g., videos, articles, code snippets).
	* Users can search and filter resources by tags, categories, and keywords.
	* Users can comment and rate resources.
	* Admins can moderate comments and ratings.
2. **Non-functional Requirements:**
	* High availability (99.99% uptime).
	* Scalability to handle a large number of users and resources.
	* Fast response times (< 500ms).
	* Secure data storage and transmission.

**High-Level Architecture:**

1. **Frontend:** A web application built using React or Angular, with a RESTful API for interactions with the backend.
2. **Backend:** A microservices-based architecture with the following services:
	* **User Service:** Handles user authentication and management.
	* **Resource Service:** Manages resource uploading, storage, and retrieval.
	* **Search Service:** Provides search functionality for resources.
	* **Comment Service:** Handles comments and ratings.
	* **Admin Service:** Moderates comments and ratings for admins.
3. **Database:** A distributed database (e.g., Cassandra, MongoDB) for storing user data, resources, and comments.
4. **Cache:** A caching layer (e.g., Redis, Memcached) for storing frequently accessed data.

**Database Design:**

1. **User Table:** Stores user information (username, email, password, etc.).
2. **Resource Table:** Stores resource metadata (title, description, tags, categories, etc.).
3. **Comment Table:** Stores comments and ratings for resources.
4. **Tag Table:** Stores tags and their relationships with resources.
5. **Category Table:** Stores categories and their relationships with resources.

**Scaling Strategy:**

1. **Horizontal Scaling:** Add more instances of each service to handle increased traffic.
2. **Load Balancing:** Distribute incoming traffic across multiple instances of each service.
3. **Auto Scaling:** Automatically add or remove instances based on demand.
4. **Caching:** Use caching to reduce database queries and improve response times.

**Bottlenecks:**

1. **Database Queries:** Frequent database queries can lead to performance issues.
2. **Resource Uploads:** Large resource uploads can cause bottlenecks in the Resource Service.
3. **Comment Moderation:** Frequent comment moderation can lead to performance issues in the Admin Service.

**Trade-offs:**

1. **Data Consistency:** We may need to sacrifice some data consistency to achieve high availability and scalability.
2. **Security:** We need to balance security with performance to ensure user data is protected.
3. **Cost:** We need to balance cost with performance to ensure the system is cost-effective.

**Solution using the First Principle of System Design:**

The First Principle of System Design states that "the system should be simple." Our solution prioritizes simplicity by:

1. **Decoupling Services:** Each service is designed to be independent, making it easier to scale and maintain.
2. **Using Caching:** Caching reduces database queries and improves response times, making the system more efficient.
3. **Avoiding Complex Database Schemas:** We use simple database tables and relationships to reduce complexity.

**Learning Links:**

* Microservices architecture: https://microservices.io/
* Distributed databases: https://cassandra.apache.org/
* Caching: https://redis.io/
* System design principles: https://en.wikipedia.org/wiki/System_design

**Example Use Cases:**

1. A user uploads a new resource, which is stored in the Resource Service and cached in Redis.
2. A user searches for resources by tag, which is handled by the Search Service and returns results from the Resource Service.
3. A user comments on a resource, which is stored in the Comment Service and moderated by the Admin Service.

**Interview Questions:**

1. How would you design a system to handle a large number of resource uploads?
2. How would you optimize the database schema for search functionality?
3. How would you ensure data consistency in a distributed database?