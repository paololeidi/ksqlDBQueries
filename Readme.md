# ksqlDB Queries

### 1. Open terminal in this directory and run:
docker-compose up

### 2. In another terminal, run the kafka container:
docker exec -it broker /bin/bash

#### To create a topic:
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic name

#### To start a consumer:
kafka-console-consumer --bootstrap-server localhost:9092 --topic name

#### To see topic list:
kafka-topics --list --bootstrap-server localhost:9092

### 3. In another terminal, open the ksqlDB CLI:
docker exec -it ksqldb-cli ksql http://ksqldb-server:8088

#### 3.1. Start executing queries in the CLI

#### 3.2. Write output on a file by executing the statement:
SPOOL filename.txt;

SPOOL OFF to disable
#### 4. Parse filename.txt with output-parser.py