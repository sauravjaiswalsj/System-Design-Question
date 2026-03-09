# Design URL Shortener

Category: system_design
Date: 2026-03-09

**Problem Statement:** Design a URL Shortener system that can handle a large number of short URLs, support fast lookups and updates, and scale horizontally to handle increasing traffic.

**Requirements (Functional + Non-functional)**

* Functional Requirements:
	+ Create a short URL for a given long URL
	+ Redirect a user to the original long URL when accessing the short URL
	+ Store metadata for each short URL (e.g., creation time, hit count)
* Non-functional Requirements:
	+ High availability and uptime (99.9%)
	+ Low latency for URL creation and redirection ( < 100ms)
	+ Scalability to handle 10,000,000 short URLs and 100,000,000 requests per day
	+ Secure data storage and transmission (HTTPS, encryption)

**High-Level Architecture**

1. **API Gateway**: Handle incoming requests, authenticate users, and route requests to the correct service.
2. **URL Shortener Service**: Create and manage short URLs, store metadata, and handle redirects.
3. **Database**: Store short URL metadata and user data.
4. **Cache**: Cache short URL metadata and user data for fast lookups.

**Database Design**

1. **Short URL Table**: Store the mapping between short URLs and long URLs.
	* Columns: `id` (primary key), `short_url`, `long_url`, `created_at`, `updated_at`, `hits`
2. **User Table**: Store user data for authentication and authorization.
	* Columns: `id` (primary key), `username`, `password`, `email`
3. **Cache**: Implement a cache layer using Redis or Memcached to store frequently accessed data.

**Scaling Strategy**

1. **Horizontal Scaling**: Add more instances of the URL Shortener Service and Database to handle increasing traffic.
2. **Load Balancing**: Distribute incoming requests across multiple instances of the API Gateway and URL Shortener Service.
3. **Auto Scaling**: Use cloud providers' auto-scaling features to dynamically add or remove instances based on traffic.

**Bottlenecks**

1. **Database Concurrency**: High concurrency can lead to database contention and slow down the system.
2. **Cache Misses**: Frequent cache misses can lead to slow performance and increased database load.
3. **API Gateway Overload**: High traffic can lead to API Gateway overload and slow down the system.

**Trade-offs**

1. **Cache vs. Database**: Caching can improve performance but may lead to cache misses and increased database load. A trade-off between cache size and database load is necessary.
2. **Scalability vs. Complexity**: Adding more instances and services can improve scalability but increase system complexity. A trade-off between scalability and complexity is necessary.
3. **Security vs. Performance**: Implementing robust security measures can improve security but may lead to increased latency and decreased performance. A trade-off between security and performance is necessary.

**Design URL Shortener Solution using the First Principle of System Design**

The first principle of system design is to "keep it simple, stupid" (KISS). To apply this principle, we can simplify the system design by:

1. **Reducing the number of services**: Instead of having multiple services for metadata and user data, we can store both in a single database.
2. **Using a simple caching mechanism**: Instead of using a complex caching mechanism, we can use a simple in-memory cache to store frequently accessed data.
3. **Using a load balancer**: Instead of implementing a custom load balancing mechanism, we can use a cloud provider's load balancer to distribute incoming requests across multiple instances.

By simplifying the system design, we can improve its maintainability, scalability, and performance.

**References**

* [System Design Primer](https://github.com/donnemartin/system-design-primer)
* [URL Shortener System Design](https://www.toptal.com/software/url-shortener-system-design)
* [High-Level System Design](https://www.guru99.com/high-level-system-design.html)
* [System Design Principles](https://www.slideshare.net/PranavKumarBhambhwani/system-design-principles)