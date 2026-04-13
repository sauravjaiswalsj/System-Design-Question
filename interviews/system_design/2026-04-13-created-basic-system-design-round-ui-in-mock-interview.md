# Created basic System Design Round UI in mock interview

Category: system_design
Date: 2026-04-13

**Mock Interview System Design UI:**

**Problem Statement:** 
Design a UI for a basic system design round in a mock interview. The system should allow users to enter their name, describe their system design, and submit it for review.

**Requirements (Functional + Non-functional):**

1. **User**: 
   - Register/ login functionality
   - Enter name and description of system design
   - Submit system design for review
   - View submitted designs and reviews

2. **Admin**: 
   - Manage user accounts
   - Review and rate submitted system designs
   - Display top-rated designs

3. **Non-functional requirements:**
   - High availability and reliability
   - Scalability
   - Data consistency
   - Performance
   - Security

**High-Level Architecture:**

1. **Frontend**: 
   - Client-side interface using React or Angular
   - Use HTML5, CSS3 for styling and UI

2. **Backend**: 
   - RESTful API using Node.js, Express, or Django
   - Database interaction (using MongoDB, MySQL, or PostgreSQL)

3. **Database**: 
   - Store user accounts, system designs, and reviews
   - Use NoSQL or relational databases based on data complexity

**Database Design:**

1. **User Table**: 
   - `id` (primary key)
   - `username`
   - `email`
   - `password` (hashed)

2. **System Design Table**: 
   - `id` (primary key)
   - `title`
   - `description`
   - `user_id` (foreign key referencing User Table)

3. **Review Table**: 
   - `id` (primary key)
   - `rating`
   - `comment`
   - `system_design_id` (foreign key referencing System Design Table)

**Scaling Strategy:**

1. **Horizontal scaling**: 
   - Add more servers to handle increased traffic

2. **Caching**: 
   - Use Redis or Memcached to store frequently accessed data

3. **Load balancing**: 
   - Distribute incoming traffic across multiple servers

**Bottlenecks:**

1. **Database performance**: 
   - Optimize queries and indexing
   - Use connection pooling

2. **API performance**: 
   - Optimize API endpoints and response times
   - Use caching and content delivery networks (CDNs)

**Trade-offs:**

1. **Complexity vs. simplicity**: 
   - Balance system complexity with user needs and requirements

2. **Scalability vs. performance**: 
   - Allocate resources and make trade-offs between scalability and performance

**First Principle of System Design:**

The first principle of system design is **Separation of Concerns**. It involves dividing the system into smaller, independent components, each responsible for a specific function. This principle helps to:

1. **Improve maintainability**: 
   - Easier to modify or replace individual components

2. **Enhance scalability**: 
   - Components can be scaled independently

3. **Reduce complexity**: 
   - Components are easier to understand and manage

In the context of the mock interview system design UI, we can apply the first principle by separating the system into the following components:

1. **Frontend**: 
   - Handles user input and interactions

2. **Backend**: 
   - Handles database interaction, API requests, and business logic

3. **Database**: 
   - Stores user data and system designs

By separating these concerns, we can improve the maintainability, scalability, and performance of the system, making it easier to manage and evolve over time.

**Learning Links:**

1. System Design Principles: <https://www.toptal.com/software/system-design-principles>
2. Separation of Concerns: <https://en.wikipedia.org/wiki/Separation_of_concerns>
3. Node.js and Express: <https://nodejs.org/en/>
4. Django: <https://www.djangoproject.com/>
5. MongoDB: <https://www.mongodb.com/>
6. React and Angular: <https://reactjs.org/> and <https://angular.io/>
7. Load Balancing: <https://en.wikipedia.org/wiki/Load_balancing>
8. Caching: <https://en.wikipedia.org/wiki/Cache>
9. Connection Pooling: <https://en.wikipedia.org/wiki/Connection_pooling>