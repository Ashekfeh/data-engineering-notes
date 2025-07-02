# Why Distributed Database Architectures?

**Traditional Setup**: Single-server configurations
**Need for Distribution**: Critical or large-scale workloads requiring:
- High availability
- Scalability

**Distributed Architecture**: Clusters of machines interconnected through networks that distribute data processing and storage tasks

## Key Benefits
- Enhanced scalability
- Fault tolerance
- Overall performance improvements

# Types of Database Architecture

## 1. Shared Disk Architecture
**Structure**:
- Multiple database servers processing workloads in parallel
- Each server connects to shared storage
- Servers communicate via high-speed interconnection

**Benefits**:
- Effective workload distribution
- Scalability as processing demand grows
- High availability through server failover mechanisms
- Seamless client rerouting during server failures

## 2. Shared Nothing Architecture
**Approach**: Uses replication OR partitioning techniques

**Key Features**:
- Distributes client workloads across multiple nodes
- Enables parallel processing
- Efficient resource utilization
- Enhanced fault tolerance through alternative node routing

## 3. Combination and Specialized Architectures
**Hybrid Approach**:
- Combines shared disk and shared nothing techniques
- Integrates replication and partitioning
- Uses specialized hardware components
- Targets specific availability and scalability goals

# Data Management and Performance Optimization Techniques

## 1. Database Replication
**Definition**: Copying changes from one database server to one or more replicas

**Types of Replicas**:

### High Availability (HA) Replica
- Located in the same location as primary
- Handles failover for software/hardware issues
- Improves performance by distributing client workload

### Disaster Recovery Replica
- Geographically distributed locations
- Protects against complete data center outages
- Handles disasters: power loss, fire, earthquake, flood

## 2. Database Partitioning and Sharding
**Partitioning**: Dividing tables with substantial data into logical segments
- Each segment contains subset of overall data
- Example: sales records for different quarters

**Sharding**: Placing partitions on separate nodes in a cluster

### Shard Characteristics
- Each shard has its own compute resources:
  - Processing power
  - Memory
  - Storage
- Operates on specific subset of data

### Query Processing with Sharding
1. Client issues query
2. Query processed in parallel across multiple nodes/shards
3. Results from different nodes are synthesized
4. Combined results returned to client

### Scalability Benefits
- Additional shards and nodes can be seamlessly added
- Facilitates increased parallel processing
- Improves overall performance as data/query workloads increase

## Common Use Cases
Database partitioning and sharding are particularly effective for:
- Data warehousing workloads
- Business intelligence applications
- Scenarios involving extensive volumes of data

# Key Takeaways Summary

1. **RDBMSs provide distributed architectures** for critical and large-scale workloads
2. **Shared disk architecture** enables parallel processing with high availability mechanisms
3. **Shared nothing architecture** uses replication or partitioning for optimized performance
4. **Database replication** copies changes to multiple replicas for improved performance and availability
5. **Sharding** distributes partitions across separate nodes, enabling parallel processing and better performance