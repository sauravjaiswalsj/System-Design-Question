# Build system design interview practice tool

Category: system_design
Date: 2026-02-16

**System Design Interview Practice Tool**

**1. Requirements (Functional + Non-functional)**

Functional Requirements:

- User authentication and authorization
- Practice problem uploading and management (e.g., problem name, description, tags, difficulty level)
- User submission of solutions with code and execution result
- Practice problem categorization (e.g., by tags, difficulty level)
- Search functionality for practice problems
- User profile management (e.g., dashboard, practice problem history)

Non-functional Requirements:

- High availability and reliability
- Scalability to handle a large number of users and practice problems
- Performance: fast problem uploading, submission, and execution
- Security: protect user data and prevent cheating
- Maintainability: easy to modify and extend the system

**2. High-Level Architecture**

- **Frontend**: Client-side application built using JavaScript frameworks like React or Angular for a user-friendly interface
  - [https://reactjs.org/](https://reactjs.org/) 
  - [https://angular.io/](https://angular.io/)

- **Backend**: Server-side application built using a language like Java, Python, or Node.js for API management, database interaction, and computation
  - [https://www.java.com/en/](https://www.java.com/en/)
  - [https://www.python.org/](https://www.python.org/)
  - [https://nodejs.org/en/](https://nodejs.org/en/)

- **Database**: Relational database like MySQL or PostgreSQL for storing user and practice problem data
  - [https://www.mysql.com/](https://www.mysql.com/)
  - [https://www.postgresql.org/](https://www.postgresql.org/)

- **Message Queue**: Distributed message queue like RabbitMQ or Apache Kafka for handling practice problem submissions and execution results
  - [https://www.rabbitmq.com/](https://www.rabbitmq.com/)
  - [https://kafka.apache.org/](https://kafka.apache.org/)

- **API Gateway**: API gateway like NGINX or Amazon API Gateway for API management and security
  - [https://www.nginx.com/](https://www.nginx.com/)
  - [https://aws.amazon.com/api-gateway/](https://aws.amazon.com/api-gateway/)

**3. Database Design**

- **User Table**: stores user information (e.g., username, email, password)
- **Practice Problem Table**: stores practice problem information (e.g., problem name, description, tags, difficulty level)
- **Submission Table**: stores user submission data (e.g., submission ID, user ID, practice problem ID, submission time)
- **Execution Result Table**: stores execution result data (e.g., execution ID, submission ID, execution time, result)

**4. Scaling Strategy**

- **Horizontal Scaling**: add more instances of the frontend, backend, and message queue services as needed
- **Load Balancing**: use a load balancer like HAProxy or Amazon ELB to distribute traffic across instances
- **Caching**: use a caching layer like Redis or Memcached to reduce database queries and improve performance
- **Auto Scaling**: use a cloud provider's auto scaling feature to automatically add or remove instances based on traffic

**5. Bottlenecks**

- **Database Performance**: frequent database queries can lead to performance issues, consider caching and indexing
- **Message Queue Processing**: slow message queue processing can lead to delays in execution results, consider parallel processing and message queue optimization
- **API Gateway Performance**: high API gateway traffic can lead to performance issues, consider caching and load balancing

**6. Trade-offs**

- **Security vs. Performance**: balancing security and performance requirements, consider using a web application firewall (WAF) and load balancing
- **Scalability vs. Complexity**: balancing scalability and complexity requirements, consider using a microservices architecture and containerization
- **Development Time vs. Maintenance Time**: balancing development time and maintenance time requirements, consider using a framework like Django or Spring Boot

**Solution using the First Principle of System Design**

The first principle of system design is "Simplicity is the ultimate sophistication". When designing the system, consider the following:

- **Separate Concerns**: separate the frontend, backend, and message queue services to improve maintainability and scalability
- **Use Established Technologies**: use established technologies and frameworks to reduce development time and improve reliability
- **Prioritize Performance**: prioritize performance and scalability requirements to ensure a high-quality user experience
- **Monitor and Optimize**: continuously monitor the system and optimize performance and scalability as needed