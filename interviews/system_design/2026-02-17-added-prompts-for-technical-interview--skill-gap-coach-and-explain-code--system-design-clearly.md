# Added prompts for technical interview & skill gap coach and Explain Code / System Design Clearly

Category: system_design
Date: 2026-02-17

**Added Prompts for Technical Interview & Skill Gap Coach**

To enhance the technical interview experience and provide a comprehensive skill gap analysis, consider the following added prompts:

1. **Design a system for...** (e.g., a real-time chat application, a recommendation engine, or a data analytics platform).
	* Requirements: Provide a clear definition of the system's functional and non-functional requirements, including scalability, availability, and performance constraints.
2. **Optimize the following system components** (e.g., database queries, API endpoints, or caching mechanisms).
	* Requirements: Identify the bottleneck components and propose optimizations to improve performance, scalability, or maintainability.
3. **Design a system to handle...** (e.g., high traffic, large data sets, or complex transactions).
	* Requirements: Develop a high-level architecture and database design to accommodate the specific requirements.

**Explain Code / System Design Clearly**

To ensure that system designs and code explanations are clear and concise, adhere to the following guidelines:

1. **Use simple, consistent terminology**: Avoid technical jargon and use industry-standard terminology to facilitate understanding.
2. **Provide a high-level overview**: Explain the overall system architecture and its components before diving into details.
3. **Focus on key components and interactions**: Emphasize the most critical components and their interactions, rather than minor details.
4. **Use diagrams and visual aids**: Utilize diagrams, flowcharts, or other visual aids to illustrate complex system designs and interactions.

**System Design Discussion**

Let's design a system for a **Real-Time Chat Application**.

**Requirements:**

1. **Functional Requirements:**
	* Users can create accounts and log in to access the chat application.
	* Users can send and receive messages in real-time.
	* Messages are persisted in a database for later retrieval.
2. **Non-Functional Requirements:**
	* The system must handle 10,000 concurrent users with an average message rate of 100 messages per second.
	* Messages must be delivered within 1 second of sending.
	* The system must be highly available, with a maximum uptime of 99.99%.

**High-Level Architecture:**

1. **Load Balancer**: Distribute incoming traffic across multiple instances of the chat application.
2. **Chat Application**: Handle user authentication, message processing, and database interactions.
3. **Database**: Store chat data, including user accounts and messages.
4. **Message Queue**: Handle high-volume message processing and guarantee message delivery.

**Database Design:**

1. **Users Table**: Store user account information (e.g., username, password, email).
2. **Messages Table**: Store chat messages, including sender ID, recipient ID, and message content.
3. **Message Queue Table**: Store incoming messages for processing.

**Scaling Strategy:**

1. **Horizontal Scaling**: Add more instances of the chat application and database to handle increased traffic.
2. **Load Balancing**: Distribute incoming traffic across multiple instances.
3. **Message Queue**: Utilize a message queue to handle high-volume message processing.

**Bottlenecks:**

1. **Database Performance**: High message rates may cause database performance issues.
2. **Message Queue**: High message volumes may cause message queue bottlenecks.

**Trade-offs:**

1. **Database Performance vs. Message Queue**: Balancing database performance with message queue efficiency.
2. **Scalability vs. Complexity**: Trade-offs between horizontal scaling and system complexity.

**Learning Links:**

1. **System Design Principles**: [https://medium.com/@romanpustovyi/system-design-principles-4f7f1ac4e3f4](https://medium.com/@romanpustovyi/system-design-principles-4f7f1ac4e3f4)
2. **Message Queue Architecture**: [https://www.toptal.com/software/what-is-message-queue](https://www.toptal.com/software/what-is-message-queue)
3. **Database Design**: [https://www.geeksforgeeks.org/database-design/](https://www.geeksforgeeks.org/database-design/)