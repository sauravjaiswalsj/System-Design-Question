# Word Ladder

Category: dsa
Date: 2026-03-27

**System Design Discussion: Word Ladder**

**Problem Statement:**
Given two words, find a sequence of words where each word differs from the previous one by exactly one character, and the final word is the target word.

**Requirements:**

**Functional Requirements:**

1. Given two words, return a list of words that transform one word into the other.
2. Handle words with different lengths.
3. Handle words with special characters or non-ASCII characters.

**Non-Functional Requirements:**

1. Scalability: handle a large number of users and requests.
2. Performance: respond within 1 second for a typical request.
3. Availability: ensure the system is available 99.99% of the time.

**High-Level Architecture:**
The system will consist of three main components:

1. **Client:** a RESTful API that accepts user requests and sends them to the **Word Ladder Service**.
2. **Word Ladder Service:** a stateless service that performs the word ladder computation using a combination of graph algorithms and memoization.
3. **Database:** a distributed database that stores the precomputed word ladders and their metadata.

**Database Design:**
We'll use a graph database like Neo4j to store the word ladders. Each node will represent a word, and each edge will represent a single-character difference between two words.

* Node properties:
	+ `word`: the actual word
	+ `length`: the length of the word
	+ `precomputed`: a boolean indicating whether the word ladder has been precomputed
* Edge properties:
	+ `source`: the source word
	+ `target`: the target word
	+ `difference`: the character difference between the two words

**Scaling Strategy:**

1. **Horizontal scaling:** add more instances of the **Word Ladder Service** as the load increases.
2. **Caching:** use a distributed caching layer like Redis to store the precomputed word ladders and their metadata.
3. **Load balancing:** use a load balancer to distribute incoming requests across multiple instances of the **Word Ladder Service**.

**Bottlenecks:**

1. **Computational complexity:** the word ladder computation has a time complexity of O(n!), where n is the length of the word.
2. **Memory usage:** storing precomputed word ladders and their metadata can consume a significant amount of memory.

**Trade-offs:**

1. **Complexity vs. performance:** a more complex algorithm (e.g., using a genetic algorithm) may be faster but also more resource-intensive.
2. **Scalability vs. simplicity:** a simpler algorithm (e.g., using a brute-force approach) may be easier to understand but also less scalable.

**Solution using the First Principle of System Design:**

The First Principle of System Design states that "any system must be designed with the goal of achieving a balance between the competing goals of performance, scalability, and availability."

To achieve this balance, we'll use a combination of:

1. **Graph algorithms:** to efficiently compute the word ladders.
2. **Memoization:** to store precomputed word ladders and reduce the computational complexity.
3. **Distributed caching:** to store the precomputed word ladders and their metadata.
4. **Horizontal scaling:** to add more instances of the **Word Ladder Service** as the load increases.
5. **Load balancing:** to distribute incoming requests across multiple instances of the **Word Ladder Service**.

By following this approach, we can achieve a system that is both scalable and performant, while also ensuring high availability.

**Learning links:**

* Graph databases: [Neo4j](https://neo4j.com/)
* Distributed caching: [Redis](https://redis.io/)
* Load balancing: [HAProxy](https://www.haproxy.org/)
* Graph algorithms: [Khan Academy](https://www.khanacademy.org/computing/computer-science/graphs)
* System design principles: [System Design Primer](https://github.com/donnemartin/system-design-primer)