# Fix evaluation timeout for long system design interviews

Category: system_design
Date: 2026-04-08

**Fix Evaluation Timeout for Long System Design Interviews**

**Problem Statement:**
Design a system to detect and prevent evaluation timeouts for long system design interviews, ensuring timely and fair evaluation of candidate responses.

**Requirements**

1. **Functional Requirements:**
	* Detect when a candidate's response exceeds a specified time limit (e.g., 30 minutes).
	* Interrupt the interview and alert the interviewer to review the candidate's response.
	* Allow the interviewer to resume the interview from the point where it was interrupted.
2. **Non-Functional Requirements:**
	* Ensure high availability (HA) and scalability to handle multiple concurrent interviews.
	* Minimize latency and maximize throughput to prevent delays.
	* Implement security measures to prevent tampering with the system.

**High-Level Architecture**

1. **Frontend:** Implement a web-based interface for the interviewer to conduct the system design interview. Use a library like React or Angular for the frontend.
2. **Backend:** Design a RESTful API using a language like Java or Python to manage interviews, detect timeouts, and alert interviewers.
3. **Database:** Use a NoSQL database like MongoDB or Cassandra to store interview metadata, candidate responses, and interviewer feedback.
4. **Real-time Messaging:** Employ WebSockets or WebRTC for real-time communication between the frontend and backend.

**Database Design**

1. **Interview Collection:** Store interview metadata (e.g., interview ID, candidate ID, start time, end time).
2. **Response Collection:** Store candidate responses, including the response text and timestamp.
3. **Feedback Collection:** Store interviewer feedback and ratings for each candidate.

**Scaling Strategy**

1. **Horizontal Scaling:** Use a load balancer to distribute incoming traffic across multiple instances of the backend API.
2. **Vertical Scaling:** Increase the power of individual instances as needed to handle increased traffic.
3. **Database Sharding:** Divide the database into smaller, independent chunks to improve read and write performance.

**Bottlenecks**

1. **Database Read-Write Contention:** High concurrency may lead to contention between reads and writes.
2. **Network Latency:** Delays in data transmission can impact real-time feedback and evaluation.
3. **Timeout Detection:** Accurate detection of timeouts may be challenging, especially for complex system design interviews.

**Trade-offs**

1. **Accuracy vs. Latency:** Balancing accuracy in timeout detection with minimizing latency for real-time feedback.
2. **Scalability vs. Complexity:** Ensuring the system can scale while maintaining a simple and maintainable architecture.
3. **Security vs. Usability:** Implementing robust security measures while providing a seamless user experience.

**Solution using the First Principle of System Design:**

The first principle of system design is to **"Keep it Simple, Stupid"** (KISS). To fix evaluation timeouts for long system design interviews, we should focus on a simple, scalable architecture that minimizes complexity and latency.

* Implement a straightforward timeout detection mechanism using a timer.
* Use a load balancer to distribute traffic across multiple instances of the backend API.
* Employ a NoSQL database to store interview metadata and candidate responses.
* Utilize WebSockets or WebRTC for real-time communication between the frontend and backend.

By following the KISS principle, we can design a system that effectively detects and prevents evaluation timeouts, ensuring timely and fair evaluation of candidate responses.

**Relevant Learning Links:**

* System Design Principles: [https://lethain.com/design-principles/](https://lethain.com/design-principles/)
* Real-time Messaging: [https://www.websocket.org/](https://www.websocket.org/)
* NoSQL Databases: [https://www.mongodb.com/](https://www.mongodb.com/) (MongoDB) | [https://cassandra.apache.org/](https://cassandra.apache.org/) (Cassandra)