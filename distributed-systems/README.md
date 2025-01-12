# Distributed Systems
A reference to various open-source distributed systems, their implementations and source code, etc.

## ClickHouse
* https://clickhouse.tech/
* https://github.com/ClickHouse/ClickHouse
* Syntax: ClickHouse SQL
* Replication: m (replicas per shard) * n (shards), table level replication (instead of node level), ClickHouse Keepr (NuRaft) or Zookeeper,
* Storage: Log Sttructed MergeTree, Supports remote storage vs local storage, data migration between storage systems, batch/lazy updates and deletes, multiple different compression algorithms (LZ4 is default).
* Key Feature: Insert triggers (materialized views), summing and aggregating MergeTrees. Supports different configurations due to modular design (separation of compute and storage)
* Inserts: Batch inserts are ideal but also supports buffer tables and async inserts. Allows for both local inserts and (hashed) distributed inserts.

## Elasticsearch
* https://www.elastic.co/
* https://github.com/elastic/elasticsearch


## Kafka
* https://kafka.apache.org/11/documentation/streams/architecture
* https://docs.confluent.io/kafka/design/index.html
*

----
