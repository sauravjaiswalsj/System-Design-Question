# Merge K Sorted Lists

Category: dsa
Date: 2026-04-18

**Merge K Sorted Lists System Design Discussion**

**Requirements:**

Functional Requirements:

1. Merge `k` sorted linked lists into one sorted linked list.
2. The input linked lists are sorted in ascending order.
3. The output linked list is also sorted in ascending order.

Non-Functional Requirements:

1. **Scalability**: The system should be able to handle a large number of linked lists and nodes.
2. **Performance**: The system should be able to merge linked lists efficiently.
3. **Reliability**: The system should be able to handle edge cases, such as empty linked lists or linked lists with duplicate nodes.

**High-Level Architecture:**

The high-level architecture of the system consists of the following components:

1. **Linked List Node**: Represents a single node in a linked list.
2. **Linked List**: Represents a sorted linked list.
3. **Merger**: The core component responsible for merging `k` linked lists into one sorted linked list.

**Database Design:**

Since we are dealing with linked lists, we don't need a traditional database design. However, we can use a data structure like a **priority queue** to store the nodes from each linked list, where the priority is the node's value.

**Scaling Strategy:**

To scale the system, we can use the following strategies:

1. **Divide and Conquer**: Divide the linked lists into smaller chunks and merge them in parallel using multiple threads or processes.
2. **Priority Queue**: Use a priority queue to store the nodes from each linked list, where the priority is the node's value. This allows us to efficiently select the node with the smallest value from the queue.
3. **Load Balancing**: Use load balancing techniques, such as round-robin or least connection, to distribute the workload across multiple nodes.

**Bottlenecks:**

The following are potential bottlenecks in the system:

1. **Node Deletion**: When deleting a node from the output linked list, we need to update the nodes in the remaining linked lists to point to the next node.
2. **Node Insertion**: When inserting a new node into the output linked list, we need to update the nodes in the remaining linked lists to point to the new node.

**Trade-offs:**

The following are trade-offs in the system:

1. **Time Complexity**: We can optimize the time complexity of the system by using a priority queue, but this may increase the space complexity.
2. **Space Complexity**: We can optimize the space complexity of the system by using a linked list, but this may increase the time complexity.

**Solution using the First Principle of System Design:**

The first principle of system design is to **"Design for failure and assume everything will fail"**. To apply this principle to the Merge K Sorted Lists problem, we can design the system to handle the following failures:

1. **Node Deletion Failure**: When deleting a node from the output linked list, we can use a retry mechanism to delete the node again if it fails.
2. **Node Insertion Failure**: When inserting a new node into the output linked list, we can use a retry mechanism to insert the node again if it fails.

Here is an example of how to implement the Merge K Sorted Lists solution using the first principle of system design:

```cpp
class Node {
public:
    int value;
    Node* next;

    Node(int value) : value(value), next(nullptr) {}
};

class Merger {
public:
    Node* mergeKLists(std::vector<Node*>& lists) {
        std::priority_queue<std::pair<int, Node*>, std::vector<std::pair<int, Node*>>, std::greater<std::pair<int, Node*>>> queue;

        for (auto& list : lists) {
            if (list) {
                queue.push(std::make_pair(list->value, list));
            }
        }

        Node* head = new Node(0);
        Node* current = head;

        while (!queue.empty()) {
            auto& pair = queue.top();
            current->next = pair.second;
            current = current->next;
            pair.second = pair.second->next;

            if (pair.second) {
                queue.push(pair);
            }

            queue.pop();
        }

        return head->next;
    }
};
```

In this example, we use a priority queue to store the nodes from each linked list, where the priority is the node's value. We then iterate through the queue and select the node with the smallest value to add to the output linked list. We use a retry mechanism to handle node deletion and insertion failures.

**Learning Links:**

* Linked lists: https://www.geeksforgeeks.org/doubly-linked-list/
* Priority queues: https://www.geeksforgeeks.org/heap-data-structure/
* Divide and conquer: https://www.geeksforgeeks.org/divide-and-conquer/
* Load balancing: https://www.geeksforgeeks.org/load-balancing/