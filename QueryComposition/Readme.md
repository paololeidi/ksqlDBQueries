# ksqlDB Queries

### 1. Run Zookeeper and Kafka on this device
And create all the needed topics: stress, output, output2

### 2. Open terminal in this directory and run:
docker compose up

### 3. In another terminal, open the ksqlDB CLI:
docker exec -it ksqldb-cli-2 ksql http://ksqldb-server:8088

#### 3.1. In the CLI, create the Output stream if id doesn't exist
CREATE STREAM outputStream (
windowOpen VARCHAR,
windowClose VARCHAR,
id INT,
maxStress INT
) WITH (
KAFKA_TOPIC='output2',
VALUE_FORMAT='JSON',
timestamp = 'windowClose',
timestamp_format = 'yyyy-MM-dd HH:mm:ss'
);

#### 3.2. Write output on a file by executing the statement:
SPOOL filename.txt;

SPOOL OFF to disable

#### 3.3. Start executing third level queries

### 4. Run the other systems and the StreamGenerator class

### 5. Download the file with the output to the project folder (files/input)
The file is saved in the Docker container files (use Visual Studio code to get it easily)
Containers/querycomposition/ksqldb-cli/Files/home/appuser

### 6. Parse filename.txt with output-parser.py