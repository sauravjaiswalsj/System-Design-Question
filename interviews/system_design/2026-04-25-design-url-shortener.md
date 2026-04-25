# Design URL Shortener

Category: system_design
Date: 2026-04-25

**System Design Discussion: Design URL Shortener**

### 1. Requirements (Functional + Non-functional)

**Functional Requirements:**

* Users can submit a long URL to be shortened.
* Users can retrieve the shortened URL.
* Users can track the number of clicks on the shortened URL.

**Non-functional Requirements:**

* High availability: The system must be available 99.99% of the time.
* Scalability: The system must handle a large number of users and URLs.
* Performance: The system must respond to user requests within 100ms.
* Security: The system must prevent abuse and maintain user data privacy.

### 2. High-Level Architecture

The system will consist of the following components:

* **Frontend:** A RESTful API to handle user requests.
* **Backend:** A caching layer to store frequently accessed URLs, and a database to store persistent data.
* **Database:** A NoSQL database to store URL metadata (e.g., origin URL, shortened URL, click count).
* **Load Balancer:** To distribute traffic across multiple backend instances.
* **Cache Cluster:** A Redis or Memcached cluster to store frequently accessed URLs.

### 3. Database Design

We will use a NoSQL database (e.g., MongoDB) to store URL metadata. The collection will have the following schema:

```json
{
  "_id" : ObjectId,
  "origin_url" : String,
  "short_url" : String,
  "click_count" : Number,
  "created_at" : Date
}
```

### 4. Scaling Strategy

To handle a large number of users and URLs, we will implement the following scaling strategies:

* **Horizontal Scaling:** Add more backend instances to handle increased traffic.
* **Load Balancing:** Distribute traffic across multiple backend instances using a load balancer.
* **Caching:** Store frequently accessed URLs in a cache cluster to reduce database queries.
* **Sharding:** Split the database into smaller shards to handle increased data volume.

### 5. Bottlenecks

Potential bottlenecks include:

* **Database queries:** Frequent database queries can lead to performance issues.
* **Cache hits:** Low cache hit rates can lead to increased database queries.
* **Backend instances:** Insufficient backend instances can lead to performance issues.

### 6. Trade-offs

Trade-offs include:

* **Cache vs. Database:** Using a cache cluster can reduce database queries, but may lead to cache inconsistencies.
* **Horizontal Scaling vs. Vertical Scaling:** Horizontal scaling can handle increased traffic, but may lead to increased complexity.
* **Load Balancing vs. Sharding:** Load balancing can distribute traffic, but may lead to single points of failure.

**Design URL Shortener Solution using the First Principle of System Design:**

The first principle of system design is to **Keep It Simple, Stupid (KISS)**.

Our design should follow the KISS principle by:

* Using a simple, lightweight database schema.
* Implementing a caching layer to reduce database queries.
* Using a load balancer to distribute traffic across multiple backend instances.
* Avoiding unnecessary complexity, such as implementing a complex sharding strategy.

By following the KISS principle, we can design a simple, scalable, and maintainable URL shortener system.

**Learning Links:**

* [System Design Principles](https://en.wikipedia.org/wiki/Systems_design_principles)
* [NoSQL Database Design](https://www.mongodb.com/developer/article/designing-nosql-database-schema/)
* [Caching Strategies](https://en.wikipedia.org/wiki/Cache_(computing))

**Code Example:**

```python
# Frontend API
from flask import Flask, request, jsonify
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/shorten', methods=['POST'])
def shorten_url():
    # Get the origin URL from the request body
    origin_url = request.json['origin_url']

    # Check if the URL is already shortened
    shortened_url = cache.get(origin_url)
    if shortened_url:
        return jsonify({'short_url': shortened_url})

    # Shorten the URL and store it in the database
    shortened_url = shorten_url(origin_url)
    cache.set(origin_url, shortened_url)
    db.insert({'origin_url': origin_url, 'short_url': shortened_url, 'click_count': 0})

    return jsonify({'short_url': shortened_url})

def shorten_url(origin_url):
    # Implement URL shortening logic here
    return 'http://short.url/' + hashlib.sha256(origin_url.encode()).hexdigest()
```

Note: This is a simplified example and may not cover all edge cases.