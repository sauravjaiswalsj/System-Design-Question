# Word Ladder

Category: dsa
Date: 2026-03-03

**Word Ladder System Design**

### Problem Statement:
Given two words, find a sequence of words where each word differs from the previous one by exactly one character, and all words in the sequence are valid English words.

### Requirements (Functional + Non-functional):

**Functional Requirements:**

1. **Word Ladder Generation**: Given two input words, generate a sequence of words that satisfy the one-character difference constraint.
2. **Word Validation**: Validate whether an input word is a valid English word.
3. **Sequence Visualization**: Display the generated word ladder sequence.

**Non-functional Requirements:**

1. **Scalability**: Handle a large number of inputs and generate ladders for a large vocabulary.
2. **Performance**: Respond quickly to user queries.
3. **Data Integrity**: Store and retrieve words from the vocabulary efficiently.
4. **Security**: Protect against invalid or malicious input.

### High-Level Architecture:

1. **Vocabulary Service**: Manages a large vocabulary of English words.
2. **Word Ladder Generator**: Given two input words, generates a sequence of words that satisfy the one-character difference constraint.
3. **API Gateway**: Handles incoming requests, validates inputs, and routes requests to the Word Ladder Generator.

### Database Design:

1. **Vocabulary Table**: Stores a large vocabulary of English words (approx. 170,000 words).
	* Columns: `word`, `definition`, `synonyms`, `antonyms`, `pronunciation`
2. **Word Ladder Table**: Stores generated word ladders.
	* Columns: `ladder_id`, `word1`, `word2`, `sequence` (JSON array of words)

**Database Schema:**
```sql
CREATE TABLE vocabulary (
  word VARCHAR(255) PRIMARY KEY,
  definition TEXT,
  synonyms TEXT,
  antonyms TEXT,
  pronunciation VARCHAR(255)
);

CREATE TABLE word_ladder (
  ladder_id INT PRIMARY KEY,
  word1 VARCHAR(255) REFERENCES vocabulary(word),
  word2 VARCHAR(255) REFERENCES vocabulary(word),
  sequence JSON
);
```
### Scaling Strategy:

1. **Horizontal Partitioning**: Split the vocabulary table across multiple shards based on the first letter of each word.
2. **Sharding**: Store generated word ladders in a distributed database, with each shard containing a subset of the generated ladders.
3. **Caching**: Cache frequently accessed words and ladders in an in-memory cache to improve performance.

### Bottlenecks:

1. **Vocabulary Size**: As the vocabulary size increases, the Word Ladder Generator may become slow due to the time complexity of the algorithm (O(n^m), where n is the vocabulary size and m is the maximum length of a word).
2. **Generated Ladder Size**: As the number of generated ladders increases, the Word Ladder Table may become large and slow to query.

### Trade-offs:

1. **Vocabulary Size vs. Performance**: Increasing the vocabulary size improves the accuracy of the Word Ladder Generator but may degrade performance.
2. **Generated Ladder Size vs. Scalability**: Increasing the number of generated ladders improves the utility of the Word Ladder System but may degrade performance and scalability.

### Solution using the First Principle of System Design:

The First Principle of System Design is to "Design for Change" by anticipating and accommodating changes in the system's requirements and environment.

In the case of the Word Ladder System, the First Principle is applied by:

1. **Modular Design**: Breaking down the system into separate modules (Vocabulary Service, Word Ladder Generator, API Gateway) to allow for easier maintenance and updates.
2. **Interface-Based Design**: Defining clear interfaces between modules to ensure loose coupling and flexibility.
3. **Scalable Architecture**: Designing the system for horizontal partitioning, sharding, and caching to accommodate increasing data volumes and user loads.

By following the First Principle, the Word Ladder System can be designed to adapt to changing requirements and scale efficiently to meet growing demands.

**Learning Links:**

* [System Design Principles](https://www.youtube.com/watch?v=ZfB2T4tQJ3k)
* [Word Ladder Algorithm](https://en.wikipedia.org/wiki/Word_ladder)
* [Scalable Architecture](https://www.toptal.com/software/scalability-architecture-design)
* [Database Design](https://www.tutorialspoint.com/database_design/index.htm)

Note: This is a simplified example and a real-world implementation may require additional considerations, such as security, error handling, and logging.