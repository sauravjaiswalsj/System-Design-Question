# Word Ladder

Category: dsa
Date: 2026-03-10

**System Design Discussion: Word Ladder**

**Problem Statement:** Given two words, find a sequence of words where each word is formed by changing one letter from the previous word, with the goal of transforming the first word into the second word.

**Requirements (Functional + Non-functional)**

Functional Requirements:

* Take two input words: `start` and `end`
* Return a sequence of words from `start` to `end` with one-letter differences between consecutive words
* If no such sequence exists, return an empty list or an error message
* Support large input words (up to 100 characters)

Non-functional Requirements:

* Low latency (less than 100ms) for small input words
* High throughput (100 requests per second) for the system
* Scalability to handle large inputs and multiple users

**High-Level Architecture:**

The system will consist of a single microservice written in a language like Java or Python, using a framework like Spring Boot or Flask. The service will be deployed on a cloud provider like AWS or GCP, using a containerization platform like Docker.

**Database Design:**

We will use a NoSQL database like Redis or Cassandra to store the word ladder graph. The graph will be represented as an adjacency list, where each node represents a word and each edge represents a one-letter difference between two words.

**Scaling Strategy:**

To scale the system, we will use the following strategies:

* Horizontal scaling: deploy multiple instances of the microservice behind a load balancer
* Caching: use Redis to cache frequently accessed words and their neighbors
* Data partitioning: partition the word ladder graph across multiple nodes in the database

**Bottlenecks:**

Potential bottlenecks in the system include:

* High computational complexity of the word ladder algorithm (O(n^3))
* Large memory usage due to the adjacency list representation of the graph
* High latency due to network I/O and database queries

**Trade-offs:**

Trade-offs in the system include:

* Choosing between a more efficient algorithm (e.g. Breadth-First Search) vs. a more scalable architecture (e.g. distributed graph processing)
* Balancing memory usage vs. computational complexity in the word ladder algorithm
* Choosing between a more robust database (e.g. relational database) vs. a more scalable one (e.g. NoSQL database)

**Solution using the 1st Principle of System Design:**

The 1st principle of system design is to "Keep it Simple, Stupid" (KISS). To apply this principle to the Word Ladder problem, we can simplify the system by:

* Focusing on the most common use case (short input words) and optimizing for that case
* Using a simple algorithm (Breadth-First Search) to find the word ladder sequence
* Using a lightweight database (Redis) to store the word ladder graph

By keeping the system simple, we can reduce the complexity and increase the performance of the system.

**Learning Links:**

* Word Ladder algorithm: https://en.wikipedia.org/wiki/Word_ladder
* Graph algorithms: https://en.wikipedia.org/wiki/Graph_algorithm
* System design principles: https://en.wikipedia.org/wiki/System_design

**Code Snippet (Python):**
```python
from collections import deque

def word_ladder(start, end):
    graph = {}
    # build the word ladder graph using a dictionary
    for word in words:
        graph[word] = []
        for other_word in words:
            if len(word) == len(other_word) and sum(c1 != c2 for c1, c2 in zip(word, other_word)) == 1:
                graph[word].append(other_word)

    queue = deque([(start, [start])])
    visited = set()
    while queue:
        word, path = queue.popleft()
        if word == end:
            return path
        for neighbor in graph[word]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return []

# usage
start_word = "cat"
end_word = "dog"
print(word_ladder(start_word, end_word))
```