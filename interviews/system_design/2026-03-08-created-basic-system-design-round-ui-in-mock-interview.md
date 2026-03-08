# Created basic System Design Round UI in mock interview

Category: system_design
Date: 2026-03-08

**System Design Round UI Mock Interview Solution**

**Problem Statement:** Design a UI for a mock interview system that allows users to create and manage interview questions, schedule interviews, and view interview results.

**First Principle of System Design:**
The first principle of system design emphasizes the importance of **Separation of Concerns (SoC)**. It suggests that a system should be divided into distinct components, each with its own responsibility, to promote modularity, maintainability, and scalability.

**Requirements (Functional + Non-functional)**

1. **Functional Requirements:**
	* Create and manage interview questions
	* Schedule interviews
	* View interview results
	* User authentication and authorization
	* Search and filtering of interview questions
2. **Non-functional Requirements:**
	* High availability (99.99% uptime)
	* Scalability ( handle 1000+ concurrent users)
	* Performance (response time < 500ms)
	* Data security and integrity

**High-Level Architecture**

1. **Frontend:**
	* Client-side: React.js or Angular.js for building the UI
	* Server-side: Node.js with Express.js for handling API requests
2. **Backend:**
	* Database: MongoDB or PostgreSQL for storing interview questions, user data, and interview results
	* API Gateway: NGINX or Amazon API Gateway for routing API requests
3. **Infrastructure:**
	* Cloud provider: AWS or Google Cloud for scalability and high availability
	* Load balancer: HAProxy or Amazon Elastic Load Balancer for distributing traffic

**Database Design**

1. **User Collection:**
	* _id (primary key)
	* username
	* password (hashed)
	* email
2. **Interview Question Collection:**
	* _id (primary key)
	* question_text
	* category
	* difficulty_level
3. **Interview Result Collection:**
	* _id (primary key)
	* user_id (foreign key referencing User Collection)
	* interview_question_id (foreign key referencing Interview Question Collection)
	* result (pass/fail)

**Scaling Strategy**

1. **Horizontal Scaling:**
	* Add more instances of the application server, load balancer, and database to handle increased traffic
	* Use a auto-scaling service (e.g., AWS Auto Scaling) to dynamically adjust instance count based on demand
2. **Vertical Scaling:**
	* Upgrade instance types (e.g., from t2.micro to c4.xlarge) to increase CPU and memory resources
	* Use a load balancer to distribute traffic across multiple instances

**Bottlenecks**

1. **Database Performance:**
	* Use an optimized database index on the interview question collection
	* Implement caching (e.g., Redis) to store frequently accessed data
2. **API Gateway Performance:**
	* Use a content delivery network (CDN) to cache static assets
	* Implement rate limiting and IP blocking to prevent abuse

**Trade-offs**

1. **Database Choice:**
	* MongoDB provides a flexible schema, but may impact performance and data consistency
	* PostgreSQL provides strong consistency, but may require more configuration and maintenance
2. **Frontend Framework:**
	* React.js provides a fast and efficient development experience, but may require more configuration and optimization
	* Angular.js provides a robust and feature-rich framework, but may be overkill for a simple UI

**Learning Links:**

1. **Separation of Concerns (SoC):** https://en.wikipedia.org/wiki/Separation_of_concerns
2. **Microservices Architecture:** https://en.wikipedia.org/wiki/Microservices
3. **Database Indexing:** https://en.wikipedia.org/wiki/Index_(database)
4. **Caching:** https://en.wikipedia.org/wiki/Cache_(computing)
5. **Load Balancing:** https://en.wikipedia.org/wiki/Load_balancing_(computing)