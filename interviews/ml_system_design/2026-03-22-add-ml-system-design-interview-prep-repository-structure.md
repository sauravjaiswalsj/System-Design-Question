# Add ML system design interview prep repository structure

Category: ml_system_design
Date: 2026-03-22

**Add ML System Design Interview Prep Repository Structure**

**1. Requirements (Functional + Non-functional)**

* Functional Requirements:
	+ Users can upload images and labels for training an ML model.
	+ Users can query the trained ML model to get predictions for new images.
	+ Users can view the model's performance metrics (accuracy, precision, recall, F1 score).
* Non-functional Requirements:
	+ High availability: the system should be able to handle a large number of concurrent requests.
	+ Scalability: the system should be able to handle increasing amounts of data and traffic.
	+ Data persistence: the system should be able to store and retrieve data efficiently.
	+ Security: the system should protect sensitive user data.

**2. High-Level Architecture**

* **Data Ingestion Layer**:
	+ Use a message broker (e.g., Apache Kafka) to handle incoming image and label data.
	+ Use a data ingestion service (e.g., Apache NiFi) to preprocess and store data in a database.
* **Model Training Layer**:
	+ Use a ML framework (e.g., TensorFlow, PyTorch) to train the ML model on the ingested data.
	+ Use a distributed training service (e.g., Horovod) to scale model training.
* **Model Serving Layer**:
	+ Use a containerization platform (e.g., Docker) to deploy the trained model.
	+ Use a model serving service (e.g., TensorFlow Serving) to handle incoming prediction requests.

**3. Database Design**

* Use a relational database (e.g., PostgreSQL) to store metadata about the images and labels.
* Use a NoSQL database (e.g., MongoDB) to store the actual image data.
* Use a database with a high-availability and replication mechanism (e.g., Galera Cluster) to ensure data persistence.

**4. Scaling Strategy**

* **Horizontal Scaling**:
	+ Use a load balancer (e.g., HAProxy) to distribute incoming requests across multiple instances.
	+ Use a container orchestration platform (e.g., Kubernetes) to manage and scale containerized services.
* **Vertical Scaling**:
	+ Use a cloud provider's auto-scaling feature to scale instances up or down based on demand.
	+ Use a caching layer (e.g., Redis) to reduce database queries and improve performance.

**5. Bottlenecks**

* **Data Ingestion**:
	+ Bottleneck: handling high volumes of incoming image and label data.
	+ Solution: use a message broker and data ingestion service to preprocess and store data efficiently.
* **Model Training**:
	+ Bottleneck: training the ML model on large datasets.
	+ Solution: use a distributed training service and scale model training horizontally.
* **Model Serving**:
	+ Bottleneck: handling high volumes of incoming prediction requests.
	+ Solution: use a model serving service and a containerization platform to deploy and scale model serving instances.

**6. Trade-offs**

* **Scalability vs. Cost**:
	+ Trade-off: horizontal scaling (more instances) vs. vertical scaling (larger instances).
	+ Solution: use a combination of both methods to balance scalability and cost.
* **Performance vs. Data Persistence**:
	+ Trade-off: using a relational database for high-performance queries vs. using a NoSQL database for data persistence.
	+ Solution: use a combination of both databases to balance performance and data persistence.

**Solution using the First Principle of System Design**

The first principle of system design is to **divide the system into smaller, independent components**.

In this case, we can break down the Add ML system into the following components:

* Data Ingestion Layer
* Model Training Layer
* Model Serving Layer

Each component has its own set of requirements, architecture, and scalability strategy. By dividing the system into smaller components, we can:

* Reduce complexity and improve maintainability
* Improve scalability and fault tolerance
* Balance competing requirements (e.g., scalability vs. cost)

**Learning Links:**

* Apache Kafka: <https://kafka.apache.org/>
* Apache NiFi: <https://nifi.apache.org/>
* TensorFlow: <https://www.tensorflow.org/>
* Horovod: <https://github.com/horovod/horovod>
* TensorFlow Serving: <https://www.tensorflow.org/serving>
* PostgreSQL: <https://www.postgresql.org/>
* MongoDB: <https://www.mongodb.com/>
* Galera Cluster: <https://galeracluster.com/>
* HAProxy: <https://www.haproxy.org/>
* Kubernetes: <https://kubernetes.io/>
* Redis: <https://redis.io/>