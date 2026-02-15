# Merge K Sorted Lists

Category: dsa
Date: 2026-02-15

**Merge K Sorted Lists System Design Discussion**

**1. Requirements (Functional + Non-functional)**

* Functional Requirements:
	+ Merge K sorted linked lists into one sorted linked list.
	+ Support insertion of new linked lists.
	+ Support removal of existing linked lists.
* Non-functional Requirements:
	+ Scalability: handle a large number of linked lists (hundreds or thousands).
	+ Performance: merge linked lists efficiently (O(N log K) time complexity).
	+ Availability: ensure system remains operational even in case of node failures.

**2. High-Level Architecture**

* **Data Ingestion**: Create a separate node in the system for each linked list. This node will be responsible for receiving new linked lists and inserting them into the system.
* **Merge Service**: This service will be responsible for merging the linked lists. It will utilize a priority queue data structure to efficiently select the next node from the linked lists to be merged.
* **Queue Service**: This service will manage the priority queue and ensure that nodes are inserted and removed efficiently.
* **Storage Service**: This service will store the merged linked list.

**High-Level Architecture Diagram**

```markdown
+---------------+
|  Data Ingestion  |
+---------------+
         |
         |
         v
+---------------+       +---------------+
|  Merge Service  |       |  Queue Service  |
+---------------+       +---------------+
         |                   |
         |                   |
         v                   v
+---------------+       +---------------+
|  Priority Queue |       |  Node Store  |
+---------------+       +---------------+
         |                   |
         |                   |
         v                   v
+---------------+       +---------------+
|  Storage Service |       |  Node Removal  |
+---------------+       +---------------+
```

**3. Database Design**

* **Node Table**: Store information about each node, including the linked list it belongs to and its priority in the priority queue.
* **Node Store Table**: Store the actual node data and its corresponding linked list.
* **Storage Table**: Store the merged linked list.

**Database Schema**

```sql
CREATE TABLE Node (
    id INT PRIMARY KEY,
    linked_list_id INT,
    priority INT
);

CREATE TABLE Node_Store (
    id INT PRIMARY KEY,
    data INT,
    linked_list_id INT
);

CREATE TABLE Storage (
    id INT PRIMARY KEY,
    data INT
);
```

**4. Scaling Strategy**

* **Horizontal Scaling**: Add more instances of the Merge Service, Queue Service, and Storage Service to handle increased load.
* **Load Balancing**: Use a load balancer to distribute incoming requests across multiple instances of the services.
* **Caching**: Implement caching at the Storage Service to reduce the number of database queries.

**5. Bottlenecks**

* **Priority Queue**: The priority queue can become a bottleneck when dealing with a large number of linked lists.
* **Node Removal**: Removing nodes from the priority queue can be expensive.

**6. Trade-offs**

* **Complexity**: The system design is complex due to the use of a priority queue and multiple services.
* **Scalability**: The system can scale horizontally, but may require additional infrastructure and maintenance.

**Solution using the First Principle of System Design (The Single Responsibility Principle)**

The Single Responsibility Principle (SRP) states that a class or module should have only one reason to change. In the context of this problem, we can apply the SRP as follows:

* **Node Class**: Responsible for storing and managing the data of a single node.
* **Priority Queue Class**: Responsible for managing the priority queue and selecting the next node to be merged.
* **Merge Class**: Responsible for merging the linked lists.
* **Storage Class**: Responsible for storing the merged linked list.

By applying the SRP, we can ensure that each class or module has a single responsibility and can be modified independently without affecting other parts of the system.

**Code Example**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, node):
        heapq.heappush(self.queue, node)

    def remove(self):
        return heapq.heappop(self.queue)

class Merge:
    def __init__(self):
        self.queue = PriorityQueue()

    def merge(self, node):
        self.queue.insert(node)

    def get_next_node(self):
        return self.queue.remove()

class Storage:
    def __init__(self):
        self.storage = []

    def store(self, node):
        self.storage.append(node)
```

Note: This is a simplified example and may not cover all edge cases. In a real-world implementation, you would need to consider additional factors such as error handling and edge cases.