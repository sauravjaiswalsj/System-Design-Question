# feat: new library FR-NFR system design interview

Category: system_design
Date: 2026-02-21

**New Library FR-NFR System Design Interview**

**Problem Statement:**

Design a system to manage a new library's features (FR) and non-functional requirements (NFR). The system should allow librarians to create, update, and delete books, patrons can check out and return books, and system administrators can manage user roles and permissions.

**Requirements (Functional + Non-functional):**

### Functional Requirements:

1. **User Management**: Create, read, update, and delete user accounts (librarians, patrons, and system administrators).
2. **Book Management**: Create, read, update, and delete book records.
3. **Checkout Management**: Allow patrons to check out books, and librarians to manage checkout status.
4. **Return Management**: Allow patrons to return books.

### Non-functional Requirements:

1. **Security**: Implement authentication and authorization mechanisms to ensure only authorized users can access the system.
2. **Scalability**: Design the system to handle a large number of users and book records.
3. **Availability**: Ensure the system is always available to users.
4. **Performance**: Optimize system response times.

**High-Level Architecture:**

1. **API Gateway**: Use a scalable API gateway (e.g., NGINX, Amazon API Gateway) to handle incoming requests.
2. **Service Registry**: Implement a service registry (e.g., Eureka, etcd) to manage service instances and their locations.
3. **Microservices**:
	* **User Service**: Handles user management, authentication, and authorization.
	* **Book Service**: Manages book records, checkout, and return status.
	* **Admin Service**: Provides system administrators with tools to manage user roles and permissions.
4. **Database**: Use a scalable database (e.g., MySQL, PostgreSQL, Amazon Aurora) to store user and book data.

**Database Design:**

1. **Users Table**: Store user information (id, username, password, role).
2. **Books Table**: Store book information (id, title, author, status).
3. **Checkout Table**: Store checkout information (id, user_id, book_id, checkout_date, return_date).
4. **Returns Table**: Store return information (id, user_id, book_id, return_date).

**Scaling Strategy:**

1. **Horizontal Scaling**: Use a load balancer to distribute incoming requests across multiple instances of each microservice.
2. **Auto Scaling**: Use cloud provider services (e.g., AWS Auto Scaling, Google Cloud Auto Scaling) to automatically add or remove instances based on demand.
3. **Sharding**: Divide the database into smaller, independent pieces (shards) to improve scalability and performance.

**Bottlenecks:**

1. **Database Queries**: Frequent database queries can lead to performance issues.
2. **Traffic Peaks**: Unexpected traffic surges can cause system overload.
3. **Service Dependencies**: Complex service dependencies can lead to cascading failures.

**Trade-offs:**

1. **Scalability vs. Complexity**: Adding more services and infrastructure can increase complexity, but also improve scalability.
2. **Security vs. Performance**: Implementing robust security mechanisms can impact system performance.
3. **Data Consistency vs. Availability**: Ensuring data consistency can impact system availability.

**Solution Using the First Principle of System Design:**

According to the first principle of system design, "Simplicity is a fundamental virtue of good design," we should strive to minimize the number of moving parts and interactions in the system.

To apply this principle, we can simplify the system by:

1. **Consolidating Services**: Combine the User Service and Admin Service into a single service, reducing the number of service instances and interactions.
2. **Reducing Database Complexity**: Simplify the database schema by removing the separate Checkout and Returns tables, and instead storing checkout and return information in the Books table.
3. **Optimizing Infrastructure**: Use a single load balancer and auto scaling service to manage traffic and instance scaling, reducing complexity and improving performance.

By following the first principle of system design and simplifying the system, we can improve scalability, performance, and maintainability.