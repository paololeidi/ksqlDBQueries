# ksqlDB Queries

### 1. Open terminal in this directory and run:
docker compose up

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

#### 3.1. In the CLI, reate streams if they don't exist

#### 3.2. Write output on a file by executing the statement:
SPOOL filename.txt;

SPOOL OFF to disable

#### 3.3. Start executing queries

#### 3.4. Run JsonStreamGenerator class

### 4. Generate the stream with JsonStreamGenerator

### 5. Download the file with the output to the project folder (files/input)
The file is saved in the Docker container files (use Visual Studio code to get it easily)
Containers/ksqldbqueriescli/ksqldb-cli/Files/home/appuser

### 6. Parse filename.txt with output-parser.py