# Build system design interview practice tool

Category: system_design
Date: 2026-04-14

**System Design Interview Practice Tool**

**1. Requirements (Functional + Non-functional)**

Functional Requirements:

- User registration and login
- System design question creation and submission
- User can view and rate submitted designs
- User can view and share public questions
- User can view their submitted designs and ratings

Non-functional Requirements:

- High availability (HA)
- Scalability
- Performance (low latency)
- Security (user authentication and authorization)
- Data consistency

**2. High-Level Architecture**

- **Frontend**: RESTful API using Node.js and Express.js
- **Backend**: Microservices-based architecture using Node.js, Express.js, and MongoDB
- **Database**: MongoDB for storing user information, questions, and ratings
- **Queueing System**: Apache Kafka for handling background tasks (e.g., sending notifications)
- **Storage**: Amazon S3 for storing design files and question assets

**3. Database Design**

- **User Collection** (MongoDB):
  - `username` (string)
  - `email` (string)
  - `password` (hashed string)
  - `designs` (array of design IDs)
  - `ratings` (array of rating IDs)

- **Question Collection** (MongoDB):
  - `id` (ObjectId)
  - `title` (string)
  - `description` (string)
  - `designs` (array of submitted designs)
  - `ratings` (array of ratings)

- **Design Collection** (MongoDB):
  - `id` (ObjectId)
  - `questionId` (reference to Question Collection)
  - `userId` (reference to User Collection)
  - `designFile` (string, stored on Amazon S3)
  - `rating` (integer)

**4. Scaling Strategy**

- **Horizontal Scaling**: Increase the number of instances for each microservice as traffic increases
- **Load Balancing**: Use HAProxy or NGINX to distribute incoming traffic across instances
- **Auto Scaling**: Use AWS Auto Scaling to automatically adjust instance count based on traffic
- **Caching**: Use Redis or Memcached to cache frequently accessed data

**5. Bottlenecks**

- **Database**: MongoDB can become a bottleneck as the number of users and questions increases
- **Queueing System**: Apache Kafka can become a bottleneck if too many messages are being processed simultaneously
- **Storage**: Amazon S3 can become a bottleneck if too many design files and question assets are being stored

**6. Trade-offs**

- **Database**: MongoDB provides a flexible schema, but can lead to performance issues if not optimized
- **Queueing System**: Apache Kafka provides high-throughput messaging, but can lead to latency if not properly configured
- **Storage**: Amazon S3 provides scalable storage, but can lead to higher costs for storing large files

**First Principle of System Design**

The first principle of system design is to **Separate Concerns**. In the case of the Build system design interview practice tool, we separate concerns by:

- **Decoupling**: Decoupling the frontend and backend using RESTful APIs
- **Loose Coupling**: Using microservices to ensure each service is loosely coupled and can be scaled independently
- **Separation of Concerns**: Separating database concerns from application logic concerns using MongoDB and Node.js

**Implementation**

To implement the system design interview practice tool, we would:

1. Set up a MongoDB cluster using MongoDB Atlas
2. Create a Node.js microservice for handling user registration and login
3. Create a Node.js microservice for handling system design question creation and submission
4. Set up an Apache Kafka cluster for handling background tasks
5. Set up an Amazon S3 bucket for storing design files and question assets
6. Implement caching using Redis or Memcached
7. Implement load balancing using HAProxy or NGINX
8. Implement auto scaling using AWS Auto Scaling