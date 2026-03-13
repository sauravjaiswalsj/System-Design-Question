# feat: Add mock interview, system design, and coding patterns features

Category: system_design
Date: 2026-03-13

**System Design Discussion: Adding Mock Interview, System Design, and Coding Patterns Features**

**1. Requirements (Functional + Non-functional)**

* Functional Requirements:
	+ Users can schedule mock interviews with other users.
	+ Users can participate in mock interviews.
	+ Users can view and rate their mock interview performance.
	+ Users can view and rate other users' mock interview performance.
	+ System design and coding patterns can be shared and discussed among users.
* Non-functional Requirements:
	+ High availability: system should be available 99.99% of the time.
	+ Scalability: system should be able to handle a large number of users.
	+ Performance: system should respond within 2 seconds.
	+ Security: user data should be encrypted and secure.

**2. High-Level Architecture**

* **Microservices Architecture**: Separate services for:
	+ User Management (User Service)
	+ Mock Interview Scheduling (Mock Interview Service)
	+ Mock Interview Participation (Mock Interview Participation Service)
	+ Rating System (Rating Service)
	+ System Design and Coding Patterns Sharing (Knowledge Sharing Service)
* **Load Balancer**: distribute incoming traffic across multiple instances of each service.
* **API Gateway**: provide a single entry point for clients to access the system.
* **Database**: use a relational database (e.g., MySQL) for storing user data and a NoSQL database (e.g., MongoDB) for storing mock interview data.

**3. Database Design**

* **User Table**:
	+ id (primary key)
	+ name
	+ email
	+ password (hashed)
* **Mock Interview Table**:
	+ id (primary key)
	+ user_id (foreign key referencing User Table)
	+ interview_date
	+ interview_time
* **Rating Table**:
	+ id (primary key)
	+ user_id (foreign key referencing User Table)
	+ mock_interview_id (foreign key referencing Mock Interview Table)
	+ rating

**4. Scaling Strategy**

* **Horizontal Scaling**: add more instances of each service as traffic increases.
* **Load Balancing**: distribute incoming traffic across multiple instances of each service.
* **Auto Scaling**: automatically add or remove instances based on traffic.
* **Caching**: use Redis or Memcached to cache frequently accessed data.

**5. Bottlenecks**

* **Database**: as the number of users and mock interviews increases, the database may become a bottleneck.
* **API Gateway**: as the number of clients increases, the API Gateway may become a bottleneck.
* **Network**: as the number of services increases, network latency may become a bottleneck.

**6. Trade-offs**

* **Single Page Application (SPA) vs. Multi-Page Application (MPA)**: SPA provides a better user experience but may be more difficult to scale.
* **Relational Database vs. NoSQL Database**: relational databases provide strong consistency but may be more difficult to scale.
* **Centralized vs. Decentralized Architecture**: centralized architecture provides easier management but may be less scalable.

**Solution using the First Principle of System Design**

The first principle of system design is: **"Do not optimize for the wrong problem."**

In this case, the wrong problem to optimize for is the number of features. Instead, we should focus on optimizing for the most critical requirement: high availability.

To achieve high availability, we can use a microservices architecture with load balancing and auto scaling. We can also use caching to reduce the load on the database.

By focusing on high availability, we can ensure that the system is able to handle a large number of users and provide a good user experience.

**Learning Links**

* Microservices Architecture: https://microservices.io/
* Load Balancing: https://en.wikipedia.org/wiki/Load_balancing_(computing)
* Auto Scaling: https://en.wikipedia.org/wiki/Auto_scaling
* Caching: https://en.wikipedia.org/wiki/Cache_(computing)
* First Principle of System Design: https://medium.com/@danielwhgray/the-first-principle-of-system-design-do-not-optimize-for-the-wrong-problem-8f8c5e8c4b8f