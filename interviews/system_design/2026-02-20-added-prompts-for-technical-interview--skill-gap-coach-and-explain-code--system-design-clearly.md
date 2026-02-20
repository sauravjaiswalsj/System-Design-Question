# Added prompts for technical interview & skill gap coach and Explain Code / System Design Clearly

Category: system_design
Date: 2026-02-20

**Added Prompts for Technical Interview & Skill Gap Coach:**

As a principal FAANG system design interviewer, I'd like to add the following prompts to assess a candidate's skills:

1. **System Design for a given Problem Statement**: Ask the candidate to design a system for a specific problem statement, and evaluate their ability to identify key requirements, high-level architecture, database design, and scaling strategy.
2. **Trade-off Analysis**: Present a scenario where multiple design choices are available, and ask the candidate to analyze the trade-offs and choose the best approach.
3. **Code Review and Refactoring**: Provide a sample code snippet and ask the candidate to review and refactor it to improve performance, scalability, and maintainability.
4. **System Design for a Real-World Problem**: Ask the candidate to design a system for a real-world problem, such as a social media platform or an e-commerce site.

**Skill Gap Coach Prompts:**

To identify skill gaps, I'd like to add the following prompts:

1. **System Design for a Domain**: Ask the candidate to design a system for a specific domain (e.g., finance, healthcare, or e-commerce).
2. **Database Design for a Large Dataset**: Provide a sample dataset and ask the candidate to design a database schema to handle large-scale data.
3. **Scalability and Performance Optimization**: Ask the candidate to identify bottlenecks in a system and suggest optimizations to improve scalability and performance.

**Explain Code / System Design Clearly:**

To evaluate a candidate's ability to explain code and system design clearly, I'd like to ask the following prompts:

1. **Code Review and Explanation**: Provide a sample code snippet and ask the candidate to explain the code's functionality, design decisions, and trade-offs.
2. **System Design Walkthrough**: Ask the candidate to explain the high-level architecture, database design, and scaling strategy of a system.
3. **Complexity Reduction**: Provide a complex system design and ask the candidate to simplify it by identifying key components and explaining their interactions.

**First Principle of System Design:**

The first principle of system design is to **Separate Concerns**. This principle states that a system should be designed to separate different concerns, such as business logic, data storage, and scalability, to improve maintainability, scalability, and performance.

**Example System Design Discussion:**

Let's consider a real-world problem statement: Design a system for a social media platform with the following requirements:

1. **Functional Requirements**:
	* Users can create accounts and post updates.
	* Users can follow other users to see their updates.
	* Users can like and comment on updates.
2. **Non-Functional Requirements**:
	* The system should handle 10,000 concurrent users.
	* The system should store 100 million updates.
	* The system should handle 1000 updates per second.

**High-Level Architecture:**

The high-level architecture of the system would involve the following components:

1. **API Gateway**: Handles incoming requests from users.
2. **User Service**: Manages user accounts and follows.
3. **Content Service**: Stores and retrieves updates.
4. **Notification Service**: Sends notifications to users when they are followed or liked.

**Database Design:**

The database design would involve the following tables:

1. **Users**: stores user information (e.g., username, password).
2. **Follows**: stores follow relationships between users.
3. **Updates**: stores updates (e.g., text, image).
4. **Likes**: stores likes on updates.
5. **Comments**: stores comments on updates.

**Scaling Strategy:**

To handle 10,000 concurrent users, we would implement the following scaling strategy:

1. **Horizontal Partitioning**: Divide the user base into smaller partitions based on geography or user behavior.
2. **Load Balancing**: Distribute incoming requests across multiple API gateways.
3. **Caching**: Cache frequently accessed data to reduce database queries.
4. **Sharding**: Shard the database across multiple servers to handle large-scale data.

**Bottlenecks:**

The bottlenecks in the system would be:

1. **Database queries**: Handling 1000 updates per second would put a high load on the database.
2. **API gateway**: Handling 10,000 concurrent users would require a high-performance API gateway.
3. **Notification service**: Sending notifications to users would require a scalable notification service.

**Trade-offs:**

The trade-offs in the system would be:

1. **Data consistency**: Sacrificing data consistency for high availability and performance.
2. **Scalability**: Sacrificing scalability for data consistency and performance.
3. **Complexity**: Sacrificing complexity for maintainability and scalability.

Note: This is a simplified example, and a real-world system design would require a more detailed analysis of the requirements, architecture, database design, and scaling strategy.