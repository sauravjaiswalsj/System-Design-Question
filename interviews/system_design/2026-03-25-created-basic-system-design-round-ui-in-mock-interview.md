# Created basic System Design Round UI in mock interview

Category: system_design
Date: 2026-03-25

**System Design Round UI Mock Interview**

**Problem Statement:**
Design a UI for a mock interview system that conducts system design interviews for experienced engineers. The system should have the following features:

1. Create a mock interview room with a candidate and interviewer.
2. Conduct a system design interview and store the interview details.
3. Provide a review and feedback mechanism for the interviewer.
4. Support multiple interviewers and candidates.

**Requirements:**

### Functional Requirements:

1. Create a mock interview room.
2. Conduct a system design interview.
3. Store interview details.
4. Provide review and feedback mechanism.
5. Support multiple interviewers and candidates.

### Non-Functional Requirements:

1. Scalability: Handle a large number of interviewers and candidates.
2. Performance: Fast response time for user interactions.
3. Availability: Ensure system uptime and reliability.
4. Security: Protect sensitive data and prevent unauthorized access.

**High-Level Architecture:**

1. **Frontend:** Use a modern web framework like React or Angular for building the UI.
2. **Backend:** Design a RESTful API using Node.js or Python to handle requests and store data.
3. **Database:** Use a relational database like MySQL or PostgreSQL to store interview details.
4. **Storage:** Use a cloud storage service like AWS S3 for storing interview recordings and files.

**Database Design:**

1. **Interviewer Table:**
	* id (primary key)
	* name
	* email
2. **Candidate Table:**
	* id (primary key)
	* name
	* email
3. **Interview Table:**
	* id (primary key)
	* interviewer_id (foreign key)
	* candidate_id (foreign key)
	* interview_date
	* interview_details
4. **Review Table:**
	* id (primary key)
	* interview_id (foreign key)
	* reviewer_id (foreign key)
	* review_date
	* feedback

**Scaling Strategy:**

1. **Horizontal Scaling:** Add more instances of the backend server to handle increased traffic.
2. **Load Balancing:** Use a load balancer to distribute traffic across multiple instances.
3. **Caching:** Implement caching mechanisms to reduce database queries and improve performance.
4. **Database Sharding:** Split large databases into smaller, independent pieces to improve scalability.

**Bottlenecks:**

1. **Database Performance:** Queries on large datasets can lead to slow response times.
2. **Server Overload:** Increased traffic can cause server overload and crashes.
3. **Data Consistency:** Ensuring data consistency across multiple instances can be challenging.

**Trade-offs:**

1. **Scalability vs. Complexity:** Adding more instances and load balancers increases complexity, but improves scalability.
2. **Performance vs. Cost:** Implementing caching mechanisms improves performance, but increases cost.
3. **Security vs. Accessibility:** Implementing robust security measures can improve security, but may limit accessibility.

**Solution using the First Principle of System Design:**

The first principle of system design is to **identify the constraints** and **design for the edge case**.

In this solution, the constraint is the scalability of the system to handle a large number of interviewers and candidates. The edge case is the scenario where the system is handling a massive influx of users, causing server overload and crashes.

To design for this edge case, we implement horizontal scaling, load balancing, caching, and database sharding to improve scalability and reduce the impact of increased traffic. This ensures that the system can handle the edge case and provides a good user experience even under heavy load.

**Learning Links:**

1. System Design Principles: [https://en.wikipedia.org/wiki/System_design](https://en.wikipedia.org/wiki/System_design)
2. System Design Interview: [https://github.com/checkio/system-design-interview](https://github.com/checkio/system-design-interview)
3. Scaling Strategies: [https://aws.amazon.com/blogs/architecture/scaling-strategies-for-distributed-systems/](https://aws.amazon.com/blogs/architecture/scaling-strategies-for-distributed-systems/)