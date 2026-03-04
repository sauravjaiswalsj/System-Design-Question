# Added prompts for technical interview & skill gap coach and Explain Code / System Design Clearly

Category: system_design
Date: 2026-03-04

**Added Prompts for Technical Interview & Skill Gap Coach**

To improve the technical interview and skill gap coaching, the following added prompts will be used:

1. **Requirements (Functional + Non-functional)**: Define the functional and non-functional requirements of the system, including but not limited to:
	* Functional requirements: What are the system's primary functions? What data will it handle?
	* Non-functional requirements: What are the system's performance, scalability, and security requirements?
2. **High-Level Architecture**: Sketch a high-level architecture of the system, including:
	* System components (e.g., frontend, backend, database)
	* Data flows between components
	* Any notable technologies or libraries used
3. **Database Design**: Describe the database design, including:
	* Database schema (e.g., tables, relationships, data types)
	* Data modeling (e.g., entity-relationship diagrams)
	* Query optimization strategies
4. **Scaling Strategy**: Outline a scaling strategy for the system, including:
	* Horizontal scaling (e.g., adding more machines)
	* Vertical scaling (e.g., increasing machine resources)
	* Load balancing and distribution strategies
5. **Bottlenecks**: Identify potential bottlenecks in the system, including:
	* Performance bottlenecks (e.g., slow database queries)
	* Scalability bottlenecks (e.g., resource limitations)
	* Security bottlenecks (e.g., vulnerabilities)
6. **Trade-offs**: Discuss trade-offs in the system design, including:
	* Performance vs. scalability
	* Security vs. usability
	* Cost vs. functionality

**Explain Code / System Design Clearly**

To explain code and system design clearly, follow the first principle of system design:

**The First Principle of System Design: "Separation of Concerns"**

The first principle of system design is to separate system components into distinct modules, each responsible for a specific concern or functionality. This principle helps to:

1. **Reduce complexity**: By separating concerns, the system becomes easier to understand and maintain.
2. **Improve scalability**: Each module can be scaled independently, without affecting the entire system.
3. **Enhance maintainability**: Changes to one module do not impact other modules, making it easier to update and modify the system.

When explaining code or system design, break it down into smaller, independent components, and describe each component's responsibilities and interactions.

**Example:**

Suppose we're designing a simple e-commerce system. We can separate the system into distinct modules:

1. **User Module**: Responsible for user authentication, authorization, and profile management.
2. **Product Module**: Handles product information, inventory management, and pricing.
3. **Order Module**: Manages orders, including processing payments and shipping.
4. **Database Module**: Stores and retrieves data from the database.

When explaining the system design, we can describe each module's responsibilities and interactions:

* "The User Module uses the Database Module to retrieve user information and updates user profiles."
* "The Product Module communicates with the Database Module to retrieve product information and updates inventory levels."

By following the first principle of system design and explaining code and system design clearly, you can effectively communicate complex system designs and improve collaboration with team members and stakeholders.

**Learning Links:**

* "The First Principle of System Design" by Martin Fowler: [https://martinfowler.com/bliki/FirstPrinciple.html](https://martinfowler.com/bliki/FirstPrinciple.html)
* "Separation of Concerns" by Wikipedia: [https://en.wikipedia.org/wiki/Separation_of_concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)
* "System Design Principles" by Amazon Web Services (AWS): [https://aws.amazon.com/blogs/architecture/system-design-principles/](https://aws.amazon.com/blogs/architecture/system-design-principles/)