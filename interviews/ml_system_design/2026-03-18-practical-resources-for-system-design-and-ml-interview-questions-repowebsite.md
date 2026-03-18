# Practical Resources for System Design and ML interview Questions (repo+website)

Category: ml_system_design
Date: 2026-03-18

**Practical Resources for System Design and ML Interview Questions**

**Requirements:**

1. **Functional Requirements:**
	* Users can upload and store resources (e.g., PDF, image, video) on the platform.
	* Users can browse and view stored resources.
	* Users can search resources by keyword, category, or tags.
	* Users can save and organize resources for later use.
	* Admins can manage user accounts, resource categories, and tags.
2. **Non-Functional Requirements:**
	* High availability and scalability to handle a large number of users.
	* Fast resource uploading, browsing, and searching.
	* Secure authentication and authorization mechanisms.
	* Regular backups and data durability.

**High-Level Architecture:**

1. **Frontend:**
	* Client-side: React.js or Angular.js for a responsive and interactive UI.
	* Server-side: RESTful API using Node.js and Express.js for handling requests.
2. **Backend:**
	* Resource Storage: Distributed file system like Amazon S3 or Google Cloud Storage for storing resources.
	* Database: Relational database like MySQL or PostgreSQL for storing metadata (e.g., resource title, description, tags).
	* Search Engine: Elasticsearch or Apache Solr for efficient resource searching.
3. **Authentication and Authorization:**
	* OAuth 2.0 for user authentication.
	* Role-Based Access Control (RBAC) for user authorization.

**Database Design:**

1. **Resource Table:**
	* `id` (primary key): unique identifier for each resource.
	* `title`: resource title.
	* `description`: resource description.
	* `tags`: list of tags associated with the resource.
	* `category_id`: foreign key referencing the category table.
2. **Category Table:**
	* `id` (primary key): unique identifier for each category.
	* `name`: category name.
3. **User Table:**
	* `id` (primary key): unique identifier for each user.
	* `username`: username.
	* `email`: email address.

**Scaling Strategy:**

1. **Horizontal Scaling:**
	* Add more servers to handle increased traffic.
	* Use load balancers to distribute traffic across servers.
2. **Vertical Scaling:**
	* Upgrade server hardware to handle increased traffic.
3. **Database Sharding:**
	* Split large databases into smaller, more manageable pieces.
	* Use sharding keys to determine which shard to query.

**Bottlenecks:**

1. **Resource Uploading:**
	* High upload traffic can cause server overload.
	* Solution: Use a content delivery network (CDN) to distribute upload traffic.
2. **Resource Searching:**
	* Large number of resources can slow down search queries.
	* Solution: Use a search engine like Elasticsearch or Apache Solr.

**Trade-offs:**

1. **Data Consistency vs. Availability:**
	* Strong consistency can lead to high latency and reduced availability.
	* Solution: Use eventual consistency to allow for faster writes and reads.
2. **Scalability vs. Complexity:**
	* Simple designs can be less scalable.
	* Solution: Use a scalable architecture that balances simplicity and complexity.

**First Principle of System Design:**

The first principle of system design is to "design for the unknown." In this case, we can use the following approach:

1. **Identify Uncertainties:**
	* What are the unknowns in this system?
	* What are the potential risks and challenges?
2. **Anticipate and Address Uncertainties:**
	* Design the system to handle unexpected traffic or failures.
	* Use techniques like load balancing, caching, and sharding to distribute load.
3. **Monitor and Adapt:**
	* Continuously monitor system performance and logs.
	* Adapt the system design as needed to handle changing user behavior and traffic patterns.

**Learning Links:**

1. System design principles: <https://github.com/donnemartin/system-design-primer>
2. RESTful API design: <https://restfulapi.net/>
3. Elasticsearch: <https://www.elastic.co/elasticsearch/>
4. Apache Solr: <https://lucene.apache.org/solr/>
5. Load balancing: <https://en.wikipedia.org/wiki/Load_balancing>
6. Caching: <https://en.wikipedia.org/wiki/Cache_(computing)>
7. Sharding: <https://en.wikipedia.org/wiki/Shard_(database_architecture)>