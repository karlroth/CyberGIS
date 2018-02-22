Last login: Tue Dec 12 13:06:59 on ttys000
wirelessprv-10-195-24-138:~ karoth$ ssh karoth4@roger-login.ncsa.illinois.edu
ROGER is in production

karoth4@roger-login.ncsa.illinois.edu's password: 
Permission denied, please try again.
karoth4@roger-login.ncsa.illinois.edu's password: 
Last login: Tue Dec 12 18:33:34 2017 from 10.195.24.138
Welcome to ROGER! Please report problems to help+ROGER@ncsa.illinois.edu

ROGER User Guide: 
https://wiki.ncsa.illinois.edu/display/ROGER/ROGER+User+Guide

ROGER Batch system constraints (for job submission):
   32 nodes  (max job size 26 nodes)
   640 cpus  (max cpus 520)

ROGER Queue Summary:
batch: 48 hr limit: all job types 
devel: 10 Mins default, 1 hr  limit: interactive jobs only (M-F 0800-1700)

For more information about ROGER's queues check the ROGER User Guide 
**********************************************************************

=-=-=-=-=-=-=-=-=-=-=-= ANNOUNCEMENT =-=-=-=-=-=-=-=-=-=-=-=

It is with regret that NCSA announces that ROGER will be shut down
on December 16, 2017. All users must move their data and work to
another system or have a plan approved by NCSA for moving the data
off of ROGER before that date; any data not moved by that date will
be lost.
 
The ROGER system reached the end of its original grant at the end
of September 2017, and funds to continue to run ROGER are exhausted.
As a service to the community, NCSA has continued to fund and operate
ROGER. Unfortunately, there is no funding to continue to operate ROGER
after the current software licenses expire on December 16, 2017, and
no agreement has been reached on a plan to continue to operate ROGER. 

To assist the users of ROGER, NCSA is making available time on the
campus cluster for 6 months (January 1, 2018 through June 30, 2018)
for all authorized ROGER users. Further information on this resource
will be sent in a separate email. In addition, users may apply for
time on Blue Waters through the Illinois allocation process
(announcement expected early in 2018) and for time through XSEDE at
https://portal.xsede.org/allocations/announcements.

William Gropp
Director and Chief Scientist, NCSA
Thomas M. Siebel Chair in Computer Science
University of Illinois Urbana-Champaign

=-=-=-=-=-=-=-=-=-=-=-= ANNOUNCEMENT =-=-=-=-=-=-=-=-=-=-=-=

Please report any issues to help+ROGER@ncsa.illinois.edu.

[karoth4@cg-gpu01 ~]$ cd final/problem3/
[karoth4@cg-gpu01 problem3]$ ls
average.py  heatmap.pig  ny_taxi_1.csv
[karoth4@cg-gpu01 problem3]$ vim heatmap.pig 
[karoth4@cg-gpu01 problem3]$ cd 
[karoth4@cg-gpu01 ~]$ cd lab11/problem3/
[karoth4@cg-gpu01 problem3]$ ls
311_data.csv  kmeans311.pig  kmeans311.py
[karoth4@cg-gpu01 problem3]$ cd ../
[karoth4@cg-gpu01 lab11]$ cd problem2
[karoth4@cg-gpu01 problem2]$ ls
average.py  heatmap.pig  radiation.csv
[karoth4@cg-gpu01 problem2]$ vim heatmap.pig 
[karoth4@cg-gpu01 problem2]$ cd 
[karoth4@cg-gpu01 ~]$ cd final/problem3
[karoth4@cg-gpu01 problem3]$ ls
average.py  heatmap.pig  ny_taxi_1.csv
[karoth4@cg-gpu01 problem3]$ vim heatmap.pig 
[karoth4@cg-gpu01 problem3]$ ls
average.py  heatmap.pig  ny_taxi_1.csv
[karoth4@cg-gpu01 problem3]$ vim average.py 
[karoth4@cg-gpu01 problem3]$ vim heatmap.pig 
[karoth4@cg-gpu01 problem3]$ cd 
[karoth4@cg-gpu01 ~]$ cd lab10/
[karoth4@cg-gpu01 lab10]$ ls
ny_taxi  word_count_hadoop
[karoth4@cg-gpu01 lab10]$ cd ny_taxi/
[karoth4@cg-gpu01 ny_taxi]$ ls
mapper.py      plotTaxi.sh  reducer.py  taxiImage_roth.asc  write2Grid.py
ny_taxi_1.csv  program.sh   result.txt  taxi.png
[karoth4@cg-gpu01 ny_taxi]$ vim write2Grid.py 
[karoth4@cg-gpu01 ny_taxi]$ cd 
[karoth4@cg-gpu01 ~]$ ls
counts.txt  heatmap_output  lab11  pig_1511542287047.log  pig_1513128184776.log  result_keywords.txt  tmp
data        kmeans_output   lab12  pig_1511543999795.log  pig_1513128194867.log  result.txt           ~tmp1
final       lab10           lab2   pig_1513128166298.log  pig_1513128538573.log  taxi.png
[karoth4@cg-gpu01 ~]$ cd lab12
[karoth4@cg-gpu01 lab12]$ ls
const.txt  myGrid.asc  plotTaxi  radque_raster.txt  spark_taxiQuery.py  taxi.png  trip_data_1.csv
[karoth4@cg-gpu01 lab12]$ vim spark_taxiQuery.py 
[karoth4@cg-gpu01 lab12]$ cp spark_taxiQuery.py ~/final/problem4/
[karoth4@cg-gpu01 lab12]$ cd 
[karoth4@cg-gpu01 ~]$ cd final/problem4/
[karoth4@cg-gpu01 problem4]$ ls
311_data.csv  spark_taxiQuery.py
[karoth4@cg-gpu01 problem4]$ vim 311_data.csv 
[karoth4@cg-gpu01 problem4]$ cd 
[karoth4@cg-gpu01 ~]$ cd lab11/problem3/
[karoth4@cg-gpu01 problem3]$ ls
311_data.csv  kmeans311.pig  kmeans311.py
[karoth4@cg-gpu01 problem3]$ vim kmeans311.pig 
[karoth4@cg-gpu01 problem3]$ cd 
[karoth4@cg-gpu01 ~]$ cd final/problem4/
[karoth4@cg-gpu01 problem4]$ vim spark_taxiQuery.py 
[karoth4@cg-gpu01 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g
-bash: spark-submit: command not found
[karoth4@cg-gpu01 problem4]$ spark_taxiQuery.py 2013-01-01 2013-02-01 40.479636 40.930724 -74.402322 -
-bash: spark_taxiQuery.py: command not found
[karoth4@cg-gpu01 problem4]$ vim spark_taxiQuery.py 
[karoth4@cg-gpu01 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 40.479636 40.930724 -74.402322 -73.630027 0.005
-bash: spark-submit: command not found
[karoth4@cg-gpu01 problem4]$ module load anaconda
[karoth4@cg-gpu01 problem4]$ ssh cg-hm08
Last login: Tue Dec 12 19:22:32 2017 from cg-gpu01.ncsa.illinois.edu
=-=-=-=-=-=-=-=-=-=-=-= ANNOUNCEMENT =-=-=-=-=-=-=-=-=-=-=-=

It is with regret that NCSA announces that ROGER will be shut down
on December 16, 2017. All users must move their data and work to
another system or have a plan approved by NCSA for moving the data
off of ROGER before that date; any data not moved by that date will
be lost.
 
The ROGER system reached the end of its original grant at the end
of September 2017, and funds to continue to run ROGER are exhausted.
As a service to the community, NCSA has continued to fund and operate
ROGER. Unfortunately, there is no funding to continue to operate ROGER
after the current software licenses expire on December 16, 2017, and
no agreement has been reached on a plan to continue to operate ROGER. 

To assist the users of ROGER, NCSA is making available time on the
campus cluster for 6 months (January 1, 2018 through June 30, 2018)
for all authorized ROGER users. Further information on this resource
will be sent in a separate email. In addition, users may apply for
time on Blue Waters through the Illinois allocation process
(announcement expected early in 2018) and for time through XSEDE at
https://portal.xsede.org/allocations/announcements.

William Gropp
Director and Chief Scientist, NCSA
Thomas M. Siebel Chair in Computer Science
University of Illinois Urbana-Champaign

=-=-=-=-=-=-=-=-=-=-=-= ANNOUNCEMENT =-=-=-=-=-=-=-=-=-=-=-=

Welcome to ROGER! Please report problems to help+ROGER@ncsa.illinois.edu
[karoth4@cg-hm08 ~]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 40.479636 40.930724 -74.402322 -73.630027 0.005
python: can't open file '/gpfs/smallblockFS/home/karoth4/spark_taxiQuery.py': [Errno 2] No such file or directory
[karoth4@cg-hm08 ~]$ module load anaconda
[karoth4@cg-hm08 ~]$ module load anaconda
[karoth4@cg-hm08 ~]$ ls
counts.txt  heatmap_output  lab11  pig_1511542287047.log  pig_1513128184776.log  result_keywords.txt  tmp
data        kmeans_output   lab12  pig_1511543999795.log  pig_1513128194867.log  result.txt           ~tmp1
final       lab10           lab2   pig_1513128166298.log  pig_1513128538573.log  taxi.png
[karoth4@cg-hm08 ~]$ cd final/problem4/
[karoth4@cg-hm08 problem4]$ ls
311_data.csv  spark_taxiQuery.py
[karoth4@cg-hm08 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 40.479636 40.930724 -74.402322 -73.630027 0.005




17/12/12 20:47:19 INFO SparkContext: Running Spark version 1.3.1
17/12/12 20:47:20 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/12/12 20:47:20 INFO SecurityManager: Changing view acls to: karoth4
17/12/12 20:47:20 INFO SecurityManager: Changing modify acls to: karoth4
17/12/12 20:47:20 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(karoth4); users with modify permissions: Set(karoth4)
17/12/12 20:47:20 INFO Slf4jLogger: Slf4jLogger started
17/12/12 20:47:20 INFO Remoting: Starting remoting
17/12/12 20:47:20 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:43107]
17/12/12 20:47:20 INFO Utils: Successfully started service 'sparkDriver' on port 43107.
17/12/12 20:47:20 INFO SparkEnv: Registering MapOutputTracker
17/12/12 20:47:20 INFO SparkEnv: Registering BlockManagerMaster
17/12/12 20:47:20 INFO DiskBlockManager: Created local directory at /tmp/spark-44fe4da4-8654-439a-99ad-224caf7b186b/blockmgr-efdb7170-4c8b-472a-b3ca-f6124ba29284
17/12/12 20:47:20 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
17/12/12 20:47:20 INFO HttpFileServer: HTTP File server directory is /tmp/spark-092ae7dc-064f-472b-bd54-2c9b1fb6929c/httpd-2bca58fa-c666-4b76-bf3a-e873ee7208e4
17/12/12 20:47:20 INFO HttpServer: Starting HTTP Server
17/12/12 20:47:20 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:47:20 INFO AbstractConnector: Started SocketConnector@0.0.0.0:38510
17/12/12 20:47:20 INFO Utils: Successfully started service 'HTTP file server' on port 38510.
17/12/12 20:47:20 INFO SparkEnv: Registering OutputCommitCoordinator
17/12/12 20:47:20 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:47:20 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
17/12/12 20:47:20 INFO Utils: Successfully started service 'SparkUI' on port 4040.
17/12/12 20:47:20 INFO SparkUI: Started SparkUI at http://cg-hm08.ncsa.illinois.edu:4040
17/12/12 20:47:20 INFO Utils: Copying /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py to /tmp/spark-ddb57c09-3065-4434-93f4-4df4c94bf5a8/userFiles-2003f5f2-328e-4fe5-8928-92451868dc8f/spark_taxiQuery.py
17/12/12 20:47:20 INFO SparkContext: Added file file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py at file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133240888
17/12/12 20:47:20 INFO Executor: Starting executor ID <driver> on host localhost
17/12/12 20:47:20 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:43107/user/HeartbeatReceiver
17/12/12 20:47:21 INFO NettyBlockTransferService: Server created on 42867
17/12/12 20:47:21 INFO BlockManagerMaster: Trying to register BlockManager
17/12/12 20:47:21 INFO BlockManagerMasterActor: Registering block manager localhost:42867 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 42867)
17/12/12 20:47:21 INFO BlockManagerMaster: Registered BlockManager
17/12/12 20:47:21 INFO MemoryStore: ensureFreeSpace(314268) called with curMem=0, maxMem=278019440
17/12/12 20:47:21 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 306.9 KB, free 264.8 MB)
17/12/12 20:47:21 INFO MemoryStore: ensureFreeSpace(46158) called with curMem=314268, maxMem=278019440
17/12/12 20:47:21 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 45.1 KB, free 264.8 MB)
17/12/12 20:47:21 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:42867 (size: 45.1 KB, free: 265.1 MB)
17/12/12 20:47:21 INFO BlockManagerMaster: Updated info of block broadcast_0_piece0
17/12/12 20:47:21 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:-2
17/12/12 20:47:21 WARN DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
Traceback (most recent call last):
  File "/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py", line 91, in <module>
    result = dataset.flatMap(makeIndex).reduceByKey(lambda a,b: a+b).sortByKey()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1482, in reduceByKey
    return self.combineByKey(lambda x: x, func, func, numPartitions)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1693, in combineByKey
    numPartitions = self._defaultReducePartitions()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2076, in _defaultReducePartitions
    return self.getNumPartitions()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 321, in getNumPartitions
    return self._jrdd.partitions().size()
  File "/usr/hdp/2.3.2.0-2602/spark/python/lib/py4j-0.8.2.1-src.zip/py4j/java_gateway.py", line 538, in __call__
  File "/usr/hdp/2.3.2.0-2602/spark/python/lib/py4j-0.8.2.1-src.zip/py4j/protocol.py", line 300, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling o49.partitions.
: org.apache.hadoop.mapred.InvalidInputException: Input path does not exist: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv
	at org.apache.hadoop.mapred.FileInputFormat.singleThreadedListStatus(FileInputFormat.java:287)
	at org.apache.hadoop.mapred.FileInputFormat.listStatus(FileInputFormat.java:229)
	at org.apache.hadoop.mapred.FileInputFormat.getSplits(FileInputFormat.java:315)
	at org.apache.spark.rdd.HadoopRDD.getPartitions(HadoopRDD.scala:203)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:219)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:217)
	at scala.Option.getOrElse(Option.scala:120)
	at org.apache.spark.rdd.RDD.partitions(RDD.scala:217)
	at org.apache.spark.rdd.MapPartitionsRDD.getPartitions(MapPartitionsRDD.scala:32)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:219)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:217)
	at scala.Option.getOrElse(Option.scala:120)
	at org.apache.spark.rdd.RDD.partitions(RDD.scala:217)
	at org.apache.spark.api.python.PythonRDD.getPartitions(PythonRDD.scala:57)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:219)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:217)
	at scala.Option.getOrElse(Option.scala:120)
	at org.apache.spark.rdd.RDD.partitions(RDD.scala:217)
	at org.apache.spark.api.python.PythonRDD.getPartitions(PythonRDD.scala:57)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:219)
	at org.apache.spark.rdd.RDD$$anonfun$partitions$2.apply(RDD.scala:217)
	at scala.Option.getOrElse(Option.scala:120)
	at org.apache.spark.rdd.RDD.partitions(RDD.scala:217)
	at org.apache.spark.api.java.JavaRDDLike$class.partitions(JavaRDDLike.scala:64)
	at org.apache.spark.api.java.AbstractJavaRDDLike.partitions(JavaRDDLike.scala:46)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:497)
	at py4j.reflection.MethodInvoker.invoke(MethodInvoker.java:231)
	at py4j.reflection.ReflectionEngine.invoke(ReflectionEngine.java:379)
	at py4j.Gateway.invoke(Gateway.java:259)
	at py4j.commands.AbstractCommand.invokeMethod(AbstractCommand.java:133)
	at py4j.commands.CallCommand.execute(CallCommand.java:79)
	at py4j.GatewayConnection.run(GatewayConnection.java:207)
	at java.lang.Thread.run(Thread.java:745)

[karoth4@cg-hm08 problem4]$ ls
311_data.csv  spark_taxiQuery.py
[karoth4@cg-hm08 problem4]$ hdfs dfs -copyFromLocal ~/final/problem4/ final/problem4
[karoth4@cg-hm08 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 40.479636 40.930724 -74.402322 -73.630027 0.005
17/12/12 20:48:55 INFO SparkContext: Running Spark version 1.3.1
17/12/12 20:48:55 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/12/12 20:48:55 INFO SecurityManager: Changing view acls to: karoth4
17/12/12 20:48:55 INFO SecurityManager: Changing modify acls to: karoth4
17/12/12 20:48:55 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(karoth4); users with modify permissions: Set(karoth4)
17/12/12 20:48:56 INFO Slf4jLogger: Slf4jLogger started
17/12/12 20:48:56 INFO Remoting: Starting remoting
17/12/12 20:48:56 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:36432]
17/12/12 20:48:56 INFO Utils: Successfully started service 'sparkDriver' on port 36432.
17/12/12 20:48:56 INFO SparkEnv: Registering MapOutputTracker
17/12/12 20:48:56 INFO SparkEnv: Registering BlockManagerMaster
17/12/12 20:48:56 INFO DiskBlockManager: Created local directory at /tmp/spark-26516b28-424b-40d5-861a-4aa25de14820/blockmgr-be4f1992-9282-4bce-b696-e076be806b90
17/12/12 20:48:56 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
17/12/12 20:48:56 INFO HttpFileServer: HTTP File server directory is /tmp/spark-3de64fff-0ccf-4302-bacc-3cc32382d32a/httpd-4eb6f7d4-e475-4a00-86ef-1785fcb4e64b
17/12/12 20:48:56 INFO HttpServer: Starting HTTP Server
17/12/12 20:48:56 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:48:56 INFO AbstractConnector: Started SocketConnector@0.0.0.0:33220
17/12/12 20:48:56 INFO Utils: Successfully started service 'HTTP file server' on port 33220.
17/12/12 20:48:56 INFO SparkEnv: Registering OutputCommitCoordinator
17/12/12 20:48:56 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:48:56 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
17/12/12 20:48:56 INFO Utils: Successfully started service 'SparkUI' on port 4040.
17/12/12 20:48:56 INFO SparkUI: Started SparkUI at http://cg-hm08.ncsa.illinois.edu:4040
17/12/12 20:48:56 INFO Utils: Copying /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py to /tmp/spark-514bf6fc-c206-40b5-a689-fa7554d8326f/userFiles-b52560af-501d-4d5b-ba41-7a15338c81e5/spark_taxiQuery.py
17/12/12 20:48:56 INFO SparkContext: Added file file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py at file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133336614
17/12/12 20:48:56 INFO Executor: Starting executor ID <driver> on host localhost
17/12/12 20:48:56 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:36432/user/HeartbeatReceiver
17/12/12 20:48:56 INFO NettyBlockTransferService: Server created on 40387
17/12/12 20:48:56 INFO BlockManagerMaster: Trying to register BlockManager
17/12/12 20:48:56 INFO BlockManagerMasterActor: Registering block manager localhost:40387 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 40387)
17/12/12 20:48:56 INFO BlockManagerMaster: Registered BlockManager
17/12/12 20:48:57 INFO MemoryStore: ensureFreeSpace(314268) called with curMem=0, maxMem=278019440
17/12/12 20:48:57 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 306.9 KB, free 264.8 MB)
17/12/12 20:48:57 INFO MemoryStore: ensureFreeSpace(46158) called with curMem=314268, maxMem=278019440
17/12/12 20:48:57 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 45.1 KB, free 264.8 MB)
17/12/12 20:48:57 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:40387 (size: 45.1 KB, free: 265.1 MB)
17/12/12 20:48:57 INFO BlockManagerMaster: Updated info of block broadcast_0_piece0
17/12/12 20:48:57 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:-2
17/12/12 20:48:57 WARN DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
17/12/12 20:48:57 INFO FileInputFormat: Total input paths to process : 1
17/12/12 20:48:57 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91
17/12/12 20:48:57 INFO DAGScheduler: Registering RDD 5 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:48:57 INFO DAGScheduler: Got job 0 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) with 2 output partitions (allowLocal=false)
17/12/12 20:48:57 INFO DAGScheduler: Final stage: Stage 1(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:48:57 INFO DAGScheduler: Parents of final stage: List(Stage 0)
17/12/12 20:48:57 INFO DAGScheduler: Missing parents: List(Stage 0)
17/12/12 20:48:57 INFO DAGScheduler: Submitting Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:48:57 INFO MemoryStore: ensureFreeSpace(9464) called with curMem=360426, maxMem=278019440
17/12/12 20:48:57 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 9.2 KB, free 264.8 MB)
17/12/12 20:48:57 INFO MemoryStore: ensureFreeSpace(7371) called with curMem=369890, maxMem=278019440
17/12/12 20:48:57 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 7.2 KB, free 264.8 MB)
17/12/12 20:48:57 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on localhost:40387 (size: 7.2 KB, free: 265.1 MB)
17/12/12 20:48:57 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 20:48:57 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:839
17/12/12 20:48:57 INFO DAGScheduler: Submitting 2 missing tasks from Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:48:57 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks
17/12/12 20:48:57 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, ANY, 1406 bytes)
17/12/12 20:48:57 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1, localhost, ANY, 1406 bytes)
17/12/12 20:48:57 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
17/12/12 20:48:57 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
17/12/12 20:48:57 INFO Executor: Fetching file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133336614
17/12/12 20:48:57 INFO Utils: /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py has been previously copied to /tmp/spark-514bf6fc-c206-40b5-a689-fa7554d8326f/userFiles-b52560af-501d-4d5b-ba41-7a15338c81e5/spark_taxiQuery.py
17/12/12 20:49:04 INFO CacheManager: Partition rdd_2_1 not found, computing it
17/12/12 20:49:04 INFO CacheManager: Partition rdd_2_0 not found, computing it
17/12/12 20:49:04 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:8619300+8619301
17/12/12 20:49:04 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:0+8619300
17/12/12 20:49:04 INFO deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/12/12 20:49:04 INFO deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/12/12 20:49:04 INFO deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/12/12 20:49:04 INFO deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/12/12 20:49:04 INFO deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/12/12 20:49:04 INFO PythonRDD: Times: total = 425, boot = 6, init = 97, finish = 322
17/12/12 20:49:04 INFO PythonRDD: Times: total = 442, boot = 3, init = 99, finish = 340
17/12/12 20:49:04 INFO MemoryStore: ensureFreeSpace(5090891) called with curMem=377261, maxMem=278019440
17/12/12 20:49:04 INFO MemoryStore: Block rdd_2_0 stored as bytes in memory (estimated size 4.9 MB, free 259.9 MB)
17/12/12 20:49:04 INFO BlockManagerInfo: Added rdd_2_0 in memory on localhost:40387 (size: 4.9 MB, free: 260.2 MB)
17/12/12 20:49:04 INFO BlockManagerMaster: Updated info of block rdd_2_0
17/12/12 20:49:04 INFO MemoryStore: ensureFreeSpace(5114468) called with curMem=5468152, maxMem=278019440
17/12/12 20:49:04 INFO MemoryStore: Block rdd_2_1 stored as bytes in memory (estimated size 4.9 MB, free 255.0 MB)
17/12/12 20:49:04 INFO BlockManagerInfo: Added rdd_2_1 in memory on localhost:40387 (size: 4.9 MB, free: 255.4 MB)
17/12/12 20:49:04 INFO BlockManagerMaster: Updated info of block rdd_2_1
17/12/12 20:49:05 INFO PythonRDD: Times: total = 7680, boot = 6747, init = 489, finish = 444
17/12/12 20:49:05 INFO PythonRDD: Times: total = 7667, boot = 6750, init = 499, finish = 418
17/12/12 20:49:05 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 2635 bytes result sent to driver
17/12/12 20:49:05 INFO Executor: Finished task 1.0 in stage 0.0 (TID 1). 2635 bytes result sent to driver
17/12/12 20:49:05 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 7755 ms on localhost (1/2)
17/12/12 20:49:05 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 7764 ms on localhost (2/2)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
17/12/12 20:49:05 INFO DAGScheduler: Stage 0 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 7.774 s
17/12/12 20:49:05 INFO DAGScheduler: looking for newly runnable stages
17/12/12 20:49:05 INFO DAGScheduler: running: Set()
17/12/12 20:49:05 INFO DAGScheduler: waiting: Set(Stage 1)
17/12/12 20:49:05 INFO DAGScheduler: failed: Set()
17/12/12 20:49:05 INFO DAGScheduler: Missing parents for Stage 1: List()
17/12/12 20:49:05 INFO DAGScheduler: Submitting Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which is now runnable
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(6064) called with curMem=10582620, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(4484) called with curMem=10588684, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 4.4 KB, free 255.0 MB)
17/12/12 20:49:05 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on localhost:40387 (size: 4.4 KB, free: 255.4 MB)
17/12/12 20:49:05 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 20:49:05 INFO SparkContext: Created broadcast 2 from broadcast at DAGScheduler.scala:839
17/12/12 20:49:05 INFO DAGScheduler: Submitting 2 missing tasks from Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Adding task set 1.0 with 2 tasks
17/12/12 20:49:05 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 2, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:49:05 INFO TaskSetManager: Starting task 1.0 in stage 1.0 (TID 3, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:49:05 INFO Executor: Running task 0.0 in stage 1.0 (TID 2)
17/12/12 20:49:05 INFO Executor: Running task 1.0 in stage 1.0 (TID 3)
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 20:49:05 INFO PythonRDD: Times: total = 44, boot = -524, init = 565, finish = 3
17/12/12 20:49:05 INFO PythonRDD: Times: total = 43, boot = -509, init = 549, finish = 3
17/12/12 20:49:05 INFO Executor: Finished task 0.0 in stage 1.0 (TID 2). 965 bytes result sent to driver
17/12/12 20:49:05 INFO Executor: Finished task 1.0 in stage 1.0 (TID 3). 965 bytes result sent to driver
17/12/12 20:49:05 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 2) in 51 ms on localhost (1/2)
17/12/12 20:49:05 INFO TaskSetManager: Finished task 1.0 in stage 1.0 (TID 3) in 51 ms on localhost (2/2)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
17/12/12 20:49:05 INFO DAGScheduler: Stage 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.053 s
17/12/12 20:49:05 INFO DAGScheduler: Job 0 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91, took 7.893277 s
17/12/12 20:49:05 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91
17/12/12 20:49:05 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 20:49:05 INFO DAGScheduler: Got job 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) with 2 output partitions (allowLocal=false)
17/12/12 20:49:05 INFO DAGScheduler: Final stage: Stage 3(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:49:05 INFO DAGScheduler: Parents of final stage: List(Stage 2)
17/12/12 20:49:05 INFO DAGScheduler: Missing parents: List()
17/12/12 20:49:05 INFO DAGScheduler: Submitting Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(6080) called with curMem=10593168, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(4575) called with curMem=10599248, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 4.5 KB, free 255.0 MB)
17/12/12 20:49:05 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on localhost:40387 (size: 4.5 KB, free: 255.3 MB)
17/12/12 20:49:05 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 20:49:05 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:839
17/12/12 20:49:05 INFO DAGScheduler: Submitting 2 missing tasks from Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Adding task set 3.0 with 2 tasks
17/12/12 20:49:05 INFO TaskSetManager: Starting task 0.0 in stage 3.0 (TID 4, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:49:05 INFO TaskSetManager: Starting task 1.0 in stage 3.0 (TID 5, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:49:05 INFO Executor: Running task 1.0 in stage 3.0 (TID 5)
17/12/12 20:49:05 INFO Executor: Running task 0.0 in stage 3.0 (TID 4)
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:49:05 INFO PythonRDD: Times: total = 5, boot = -97, init = 99, finish = 3
17/12/12 20:49:05 INFO Executor: Finished task 1.0 in stage 3.0 (TID 5). 1294 bytes result sent to driver
17/12/12 20:49:05 INFO TaskSetManager: Finished task 1.0 in stage 3.0 (TID 5) in 9 ms on localhost (1/2)
17/12/12 20:49:05 INFO PythonRDD: Times: total = 44, boot = -114, init = 155, finish = 3
17/12/12 20:49:05 INFO Executor: Finished task 0.0 in stage 3.0 (TID 4). 1217 bytes result sent to driver
17/12/12 20:49:05 INFO TaskSetManager: Finished task 0.0 in stage 3.0 (TID 4) in 48 ms on localhost (2/2)
17/12/12 20:49:05 INFO DAGScheduler: Stage 3 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.049 s
17/12/12 20:49:05 INFO TaskSchedulerImpl: Removed TaskSet 3.0, whose tasks have all completed, from pool 
17/12/12 20:49:05 INFO DAGScheduler: Job 1 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91, took 0.061276 s
17/12/12 20:49:05 INFO SparkContext: Starting job: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92
17/12/12 20:49:05 INFO DAGScheduler: Registering RDD 12 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:49:05 INFO DAGScheduler: Got job 2 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92) with 2 output partitions (allowLocal=false)
17/12/12 20:49:05 INFO DAGScheduler: Final stage: Stage 6(collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92)
17/12/12 20:49:05 INFO DAGScheduler: Parents of final stage: List(Stage 5)
17/12/12 20:49:05 INFO DAGScheduler: Missing parents: List(Stage 5)
17/12/12 20:49:05 INFO DAGScheduler: Submitting Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(7008) called with curMem=10603823, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_4 stored as values in memory (estimated size 6.8 KB, free 255.0 MB)
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(5359) called with curMem=10610831, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_4_piece0 stored as bytes in memory (estimated size 5.2 KB, free 255.0 MB)
17/12/12 20:49:05 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on localhost:40387 (size: 5.2 KB, free: 255.3 MB)
17/12/12 20:49:05 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 20:49:05 INFO SparkContext: Created broadcast 4 from broadcast at DAGScheduler.scala:839
17/12/12 20:49:05 INFO DAGScheduler: Submitting 2 missing tasks from Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Adding task set 5.0 with 2 tasks
17/12/12 20:49:05 INFO TaskSetManager: Starting task 0.0 in stage 5.0 (TID 6, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 20:49:05 INFO TaskSetManager: Starting task 1.0 in stage 5.0 (TID 7, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 20:49:05 INFO Executor: Running task 0.0 in stage 5.0 (TID 6)
17/12/12 20:49:05 INFO Executor: Running task 1.0 in stage 5.0 (TID 7)
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:49:05 INFO PythonRDD: Times: total = 45, boot = -82, init = 123, finish = 4
17/12/12 20:49:05 INFO PythonRDD: Times: total = 46, boot = -83, init = 124, finish = 5
17/12/12 20:49:05 INFO Executor: Finished task 0.0 in stage 5.0 (TID 6). 1160 bytes result sent to driver
17/12/12 20:49:05 INFO Executor: Finished task 1.0 in stage 5.0 (TID 7). 1160 bytes result sent to driver
17/12/12 20:49:05 INFO TaskSetManager: Finished task 0.0 in stage 5.0 (TID 6) in 51 ms on localhost (1/2)
17/12/12 20:49:05 INFO TaskSetManager: Finished task 1.0 in stage 5.0 (TID 7) in 52 ms on localhost (2/2)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Removed TaskSet 5.0, whose tasks have all completed, from pool 
17/12/12 20:49:05 INFO DAGScheduler: Stage 5 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.053 s
17/12/12 20:49:05 INFO DAGScheduler: looking for newly runnable stages
17/12/12 20:49:05 INFO DAGScheduler: running: Set()
17/12/12 20:49:05 INFO DAGScheduler: waiting: Set(Stage 6)
17/12/12 20:49:05 INFO DAGScheduler: failed: Set()
17/12/12 20:49:05 INFO DAGScheduler: Missing parents for Stage 6: List()
17/12/12 20:49:05 INFO DAGScheduler: Submitting Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92), which is now runnable
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(4816) called with curMem=10616190, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_5 stored as values in memory (estimated size 4.7 KB, free 255.0 MB)
17/12/12 20:49:05 INFO MemoryStore: ensureFreeSpace(3507) called with curMem=10621006, maxMem=278019440
17/12/12 20:49:05 INFO MemoryStore: Block broadcast_5_piece0 stored as bytes in memory (estimated size 3.4 KB, free 255.0 MB)
17/12/12 20:49:05 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on localhost:40387 (size: 3.4 KB, free: 255.3 MB)
17/12/12 20:49:05 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 20:49:05 INFO SparkContext: Created broadcast 5 from broadcast at DAGScheduler.scala:839
17/12/12 20:49:05 INFO DAGScheduler: Submitting 2 missing tasks from Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Adding task set 6.0 with 2 tasks
17/12/12 20:49:05 INFO TaskSetManager: Starting task 0.0 in stage 6.0 (TID 8, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:49:05 INFO TaskSetManager: Starting task 1.0 in stage 6.0 (TID 9, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:49:05 INFO Executor: Running task 0.0 in stage 6.0 (TID 8)
17/12/12 20:49:05 INFO Executor: Running task 1.0 in stage 6.0 (TID 9)
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:49:05 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:49:05 INFO PythonRDD: Times: total = 43, boot = -67, init = 107, finish = 3
17/12/12 20:49:05 INFO PythonRDD: Times: total = 44, boot = -105, init = 146, finish = 3
17/12/12 20:49:05 INFO Executor: Finished task 1.0 in stage 6.0 (TID 9). 20473 bytes result sent to driver
17/12/12 20:49:05 INFO Executor: Finished task 0.0 in stage 6.0 (TID 8). 17054 bytes result sent to driver
17/12/12 20:49:05 INFO TaskSetManager: Finished task 1.0 in stage 6.0 (TID 9) in 48 ms on localhost (1/2)
17/12/12 20:49:05 INFO TaskSetManager: Finished task 0.0 in stage 6.0 (TID 8) in 48 ms on localhost (2/2)
17/12/12 20:49:05 INFO TaskSchedulerImpl: Removed TaskSet 6.0, whose tasks have all completed, from pool 
17/12/12 20:49:05 INFO DAGScheduler: Stage 6 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92) finished in 0.049 s
17/12/12 20:49:05 INFO DAGScheduler: Job 2 finished: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92, took 0.114273 s
Traceback (most recent call last):
  File "/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py", line 94, in <module>
    write_to_grid(ww)
  File "/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py", line 61, in write_to_grid
    myArray[ele[0][0], ele[0][1]] = float(ele[1]) 
IndexError: index 232 is out of bounds for axis 0 with size 91
[karoth4@cg-hm08 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 40.479636 40.930724 -74.402322 -73.630027 0.005
17/12/12 20:57:14 INFO SparkContext: Running Spark version 1.3.1
17/12/12 20:57:14 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/12/12 20:57:14 INFO SecurityManager: Changing view acls to: karoth4
17/12/12 20:57:14 INFO SecurityManager: Changing modify acls to: karoth4
17/12/12 20:57:14 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(karoth4); users with modify permissions: Set(karoth4)
17/12/12 20:57:14 INFO Slf4jLogger: Slf4jLogger started
17/12/12 20:57:14 INFO Remoting: Starting remoting
17/12/12 20:57:14 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:34901]
17/12/12 20:57:14 INFO Utils: Successfully started service 'sparkDriver' on port 34901.
17/12/12 20:57:14 INFO SparkEnv: Registering MapOutputTracker
17/12/12 20:57:14 INFO SparkEnv: Registering BlockManagerMaster
17/12/12 20:57:14 INFO DiskBlockManager: Created local directory at /tmp/spark-f1bf3b9e-c463-49b4-8779-b54ff2c5deab/blockmgr-3b5cbe78-42e4-46bf-a4cc-9bbca4399b44
17/12/12 20:57:14 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
17/12/12 20:57:14 INFO HttpFileServer: HTTP File server directory is /tmp/spark-63474752-803c-48f6-a98c-debcf42d26a0/httpd-89d2a317-8cc9-478f-9829-f133b97ae559
17/12/12 20:57:14 INFO HttpServer: Starting HTTP Server
17/12/12 20:57:14 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:57:14 INFO AbstractConnector: Started SocketConnector@0.0.0.0:40442
17/12/12 20:57:14 INFO Utils: Successfully started service 'HTTP file server' on port 40442.
17/12/12 20:57:14 INFO SparkEnv: Registering OutputCommitCoordinator
17/12/12 20:57:14 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:57:14 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
17/12/12 20:57:14 INFO Utils: Successfully started service 'SparkUI' on port 4040.
17/12/12 20:57:14 INFO SparkUI: Started SparkUI at http://cg-hm08.ncsa.illinois.edu:4040
17/12/12 20:57:15 INFO Utils: Copying /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py to /tmp/spark-21826e41-ed16-4b49-b631-5a029d8ad5f0/userFiles-cb7a8024-6714-4364-8049-82e0b291529f/spark_taxiQuery.py
17/12/12 20:57:15 INFO SparkContext: Added file file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py at file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133835053
17/12/12 20:57:15 INFO Executor: Starting executor ID <driver> on host localhost
17/12/12 20:57:15 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:34901/user/HeartbeatReceiver
17/12/12 20:57:15 INFO NettyBlockTransferService: Server created on 41309
17/12/12 20:57:15 INFO BlockManagerMaster: Trying to register BlockManager
17/12/12 20:57:15 INFO BlockManagerMasterActor: Registering block manager localhost:41309 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 41309)
17/12/12 20:57:15 INFO BlockManagerMaster: Registered BlockManager
17/12/12 20:57:15 INFO MemoryStore: ensureFreeSpace(314268) called with curMem=0, maxMem=278019440
17/12/12 20:57:15 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 306.9 KB, free 264.8 MB)
17/12/12 20:57:15 INFO MemoryStore: ensureFreeSpace(46158) called with curMem=314268, maxMem=278019440
17/12/12 20:57:15 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 45.1 KB, free 264.8 MB)
17/12/12 20:57:15 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:41309 (size: 45.1 KB, free: 265.1 MB)
17/12/12 20:57:15 INFO BlockManagerMaster: Updated info of block broadcast_0_piece0
17/12/12 20:57:15 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:-2
17/12/12 20:57:15 WARN DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
17/12/12 20:57:16 INFO FileInputFormat: Total input paths to process : 1
17/12/12 20:57:16 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91
17/12/12 20:57:16 INFO DAGScheduler: Registering RDD 5 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:16 INFO DAGScheduler: Got job 0 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) with 2 output partitions (allowLocal=false)
17/12/12 20:57:16 INFO DAGScheduler: Final stage: Stage 1(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:16 INFO DAGScheduler: Parents of final stage: List(Stage 0)
17/12/12 20:57:16 INFO DAGScheduler: Missing parents: List(Stage 0)
17/12/12 20:57:16 INFO DAGScheduler: Submitting Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:57:16 INFO MemoryStore: ensureFreeSpace(9464) called with curMem=360426, maxMem=278019440
17/12/12 20:57:16 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 9.2 KB, free 264.8 MB)
17/12/12 20:57:16 INFO MemoryStore: ensureFreeSpace(7370) called with curMem=369890, maxMem=278019440
17/12/12 20:57:16 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 7.2 KB, free 264.8 MB)
17/12/12 20:57:16 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on localhost:41309 (size: 7.2 KB, free: 265.1 MB)
17/12/12 20:57:16 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 20:57:16 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:839
17/12/12 20:57:16 INFO DAGScheduler: Submitting 2 missing tasks from Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:16 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks
17/12/12 20:57:16 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, ANY, 1406 bytes)
17/12/12 20:57:16 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1, localhost, ANY, 1406 bytes)
17/12/12 20:57:16 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
17/12/12 20:57:16 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
17/12/12 20:57:16 INFO Executor: Fetching file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133835053
17/12/12 20:57:16 INFO Utils: /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py has been previously copied to /tmp/spark-21826e41-ed16-4b49-b631-5a029d8ad5f0/userFiles-cb7a8024-6714-4364-8049-82e0b291529f/spark_taxiQuery.py
17/12/12 20:57:23 INFO CacheManager: Partition rdd_2_1 not found, computing it
17/12/12 20:57:23 INFO CacheManager: Partition rdd_2_0 not found, computing it
17/12/12 20:57:23 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:8619300+8619301
17/12/12 20:57:23 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:0+8619300
17/12/12 20:57:23 INFO deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/12/12 20:57:23 INFO deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/12/12 20:57:23 INFO deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/12/12 20:57:23 INFO deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/12/12 20:57:23 INFO deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/12/12 20:57:23 INFO PythonRDD: Times: total = 483, boot = 4, init = 145, finish = 334
17/12/12 20:57:23 INFO PythonRDD: Times: total = 491, boot = 7, init = 142, finish = 342
17/12/12 20:57:23 INFO MemoryStore: ensureFreeSpace(5114468) called with curMem=377260, maxMem=278019440
17/12/12 20:57:23 INFO MemoryStore: Block rdd_2_1 stored as bytes in memory (estimated size 4.9 MB, free 259.9 MB)
17/12/12 20:57:23 INFO BlockManagerInfo: Added rdd_2_1 in memory on localhost:41309 (size: 4.9 MB, free: 260.2 MB)
17/12/12 20:57:23 INFO BlockManagerMaster: Updated info of block rdd_2_1
17/12/12 20:57:23 INFO MemoryStore: ensureFreeSpace(5090891) called with curMem=5491728, maxMem=278019440
17/12/12 20:57:23 INFO MemoryStore: Block rdd_2_0 stored as bytes in memory (estimated size 4.9 MB, free 255.0 MB)
17/12/12 20:57:23 INFO BlockManagerInfo: Added rdd_2_0 in memory on localhost:41309 (size: 4.9 MB, free: 255.4 MB)
17/12/12 20:57:23 INFO BlockManagerMaster: Updated info of block rdd_2_0
17/12/12 20:57:24 INFO PythonRDD: Times: total = 7970, boot = 6996, init = 553, finish = 421
17/12/12 20:57:24 INFO PythonRDD: Times: total = 7981, boot = 7000, init = 544, finish = 437
17/12/12 20:57:24 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 2635 bytes result sent to driver
17/12/12 20:57:24 INFO Executor: Finished task 1.0 in stage 0.0 (TID 1). 2635 bytes result sent to driver
17/12/12 20:57:24 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 8067 ms on localhost (1/2)
17/12/12 20:57:24 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 8062 ms on localhost (2/2)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
17/12/12 20:57:24 INFO DAGScheduler: Stage 0 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 8.080 s
17/12/12 20:57:24 INFO DAGScheduler: looking for newly runnable stages
17/12/12 20:57:24 INFO DAGScheduler: running: Set()
17/12/12 20:57:24 INFO DAGScheduler: waiting: Set(Stage 1)
17/12/12 20:57:24 INFO DAGScheduler: failed: Set()
17/12/12 20:57:24 INFO DAGScheduler: Missing parents for Stage 1: List()
17/12/12 20:57:24 INFO DAGScheduler: Submitting Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which is now runnable
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(6064) called with curMem=10582619, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(4484) called with curMem=10588683, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 4.4 KB, free 255.0 MB)
17/12/12 20:57:24 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on localhost:41309 (size: 4.4 KB, free: 255.4 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 20:57:24 INFO SparkContext: Created broadcast 2 from broadcast at DAGScheduler.scala:839
17/12/12 20:57:24 INFO DAGScheduler: Submitting 2 missing tasks from Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Adding task set 1.0 with 2 tasks
17/12/12 20:57:24 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 2, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO TaskSetManager: Starting task 1.0 in stage 1.0 (TID 3, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO Executor: Running task 1.0 in stage 1.0 (TID 3)
17/12/12 20:57:24 INFO Executor: Running task 0.0 in stage 1.0 (TID 2)
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 20:57:24 INFO PythonRDD: Times: total = 43, boot = -517, init = 557, finish = 3
17/12/12 20:57:24 INFO PythonRDD: Times: total = 43, boot = -510, init = 550, finish = 3
17/12/12 20:57:24 INFO Executor: Finished task 1.0 in stage 1.0 (TID 3). 965 bytes result sent to driver
17/12/12 20:57:24 INFO Executor: Finished task 0.0 in stage 1.0 (TID 2). 965 bytes result sent to driver
17/12/12 20:57:24 INFO TaskSetManager: Finished task 1.0 in stage 1.0 (TID 3) in 50 ms on localhost (1/2)
17/12/12 20:57:24 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 2) in 51 ms on localhost (2/2)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
17/12/12 20:57:24 INFO DAGScheduler: Stage 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.052 s
17/12/12 20:57:24 INFO DAGScheduler: Job 0 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91, took 8.199636 s
17/12/12 20:57:24 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91
17/12/12 20:57:24 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 20:57:24 INFO DAGScheduler: Got job 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) with 2 output partitions (allowLocal=false)
17/12/12 20:57:24 INFO DAGScheduler: Final stage: Stage 3(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:24 INFO DAGScheduler: Parents of final stage: List(Stage 2)
17/12/12 20:57:24 INFO DAGScheduler: Missing parents: List()
17/12/12 20:57:24 INFO DAGScheduler: Submitting Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(6080) called with curMem=10593167, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(4575) called with curMem=10599247, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 4.5 KB, free 255.0 MB)
17/12/12 20:57:24 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on localhost:41309 (size: 4.5 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 20:57:24 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:839
17/12/12 20:57:24 INFO DAGScheduler: Submitting 2 missing tasks from Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Adding task set 3.0 with 2 tasks
17/12/12 20:57:24 INFO TaskSetManager: Starting task 0.0 in stage 3.0 (TID 4, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO TaskSetManager: Starting task 1.0 in stage 3.0 (TID 5, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO Executor: Running task 1.0 in stage 3.0 (TID 5)
17/12/12 20:57:24 INFO Executor: Running task 0.0 in stage 3.0 (TID 4)
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:57:24 INFO PythonRDD: Times: total = 5, boot = -114, init = 117, finish = 2
17/12/12 20:57:24 INFO Executor: Finished task 1.0 in stage 3.0 (TID 5). 1294 bytes result sent to driver
17/12/12 20:57:24 INFO TaskSetManager: Finished task 1.0 in stage 3.0 (TID 5) in 9 ms on localhost (1/2)
17/12/12 20:57:24 INFO PythonRDD: Times: total = 8, boot = -130, init = 133, finish = 5
17/12/12 20:57:24 INFO Executor: Finished task 0.0 in stage 3.0 (TID 4). 1217 bytes result sent to driver
17/12/12 20:57:24 INFO TaskSetManager: Finished task 0.0 in stage 3.0 (TID 4) in 11 ms on localhost (2/2)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Removed TaskSet 3.0, whose tasks have all completed, from pool 
17/12/12 20:57:24 INFO DAGScheduler: Stage 3 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.011 s
17/12/12 20:57:24 INFO DAGScheduler: Job 1 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91, took 0.020786 s
17/12/12 20:57:24 INFO SparkContext: Starting job: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92
17/12/12 20:57:24 INFO DAGScheduler: Registering RDD 12 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:24 INFO DAGScheduler: Got job 2 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92) with 2 output partitions (allowLocal=false)
17/12/12 20:57:24 INFO DAGScheduler: Final stage: Stage 6(collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92)
17/12/12 20:57:24 INFO DAGScheduler: Parents of final stage: List(Stage 5)
17/12/12 20:57:24 INFO DAGScheduler: Missing parents: List(Stage 5)
17/12/12 20:57:24 INFO DAGScheduler: Submitting Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(7008) called with curMem=10603822, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_4 stored as values in memory (estimated size 6.8 KB, free 255.0 MB)
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(5359) called with curMem=10610830, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_4_piece0 stored as bytes in memory (estimated size 5.2 KB, free 255.0 MB)
17/12/12 20:57:24 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on localhost:41309 (size: 5.2 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 20:57:24 INFO SparkContext: Created broadcast 4 from broadcast at DAGScheduler.scala:839
17/12/12 20:57:24 INFO DAGScheduler: Submitting 2 missing tasks from Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Adding task set 5.0 with 2 tasks
17/12/12 20:57:24 INFO TaskSetManager: Starting task 0.0 in stage 5.0 (TID 6, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 20:57:24 INFO TaskSetManager: Starting task 1.0 in stage 5.0 (TID 7, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 20:57:24 INFO Executor: Running task 1.0 in stage 5.0 (TID 7)
17/12/12 20:57:24 INFO Executor: Running task 0.0 in stage 5.0 (TID 6)
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
17/12/12 20:57:24 INFO PythonRDD: Times: total = 44, boot = -62, init = 102, finish = 4
17/12/12 20:57:24 INFO PythonRDD: Times: total = 45, boot = -62, init = 103, finish = 4
17/12/12 20:57:24 INFO Executor: Finished task 0.0 in stage 5.0 (TID 6). 1160 bytes result sent to driver
17/12/12 20:57:24 INFO Executor: Finished task 1.0 in stage 5.0 (TID 7). 1160 bytes result sent to driver
17/12/12 20:57:24 INFO TaskSetManager: Finished task 0.0 in stage 5.0 (TID 6) in 50 ms on localhost (1/2)
17/12/12 20:57:24 INFO TaskSetManager: Finished task 1.0 in stage 5.0 (TID 7) in 51 ms on localhost (2/2)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Removed TaskSet 5.0, whose tasks have all completed, from pool 
17/12/12 20:57:24 INFO DAGScheduler: Stage 5 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.051 s
17/12/12 20:57:24 INFO DAGScheduler: looking for newly runnable stages
17/12/12 20:57:24 INFO DAGScheduler: running: Set()
17/12/12 20:57:24 INFO DAGScheduler: waiting: Set(Stage 6)
17/12/12 20:57:24 INFO DAGScheduler: failed: Set()
17/12/12 20:57:24 INFO DAGScheduler: Missing parents for Stage 6: List()
17/12/12 20:57:24 INFO DAGScheduler: Submitting Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92), which is now runnable
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(4816) called with curMem=10616189, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_5 stored as values in memory (estimated size 4.7 KB, free 255.0 MB)
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(3507) called with curMem=10621005, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_5_piece0 stored as bytes in memory (estimated size 3.4 KB, free 255.0 MB)
17/12/12 20:57:24 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on localhost:41309 (size: 3.4 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 20:57:24 INFO SparkContext: Created broadcast 5 from broadcast at DAGScheduler.scala:839
17/12/12 20:57:24 INFO DAGScheduler: Submitting 2 missing tasks from Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Adding task set 6.0 with 2 tasks
17/12/12 20:57:24 INFO TaskSetManager: Starting task 0.0 in stage 6.0 (TID 8, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO TaskSetManager: Starting task 1.0 in stage 6.0 (TID 9, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO Executor: Running task 1.0 in stage 6.0 (TID 9)
17/12/12 20:57:24 INFO Executor: Running task 0.0 in stage 6.0 (TID 8)
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:57:24 INFO PythonRDD: Times: total = 42, boot = -66, init = 106, finish = 2
17/12/12 20:57:24 INFO PythonRDD: Times: total = 43, boot = -61, init = 101, finish = 3
17/12/12 20:57:24 INFO Executor: Finished task 0.0 in stage 6.0 (TID 8). 17054 bytes result sent to driver
17/12/12 20:57:24 INFO Executor: Finished task 1.0 in stage 6.0 (TID 9). 20473 bytes result sent to driver
17/12/12 20:57:24 INFO TaskSetManager: Finished task 0.0 in stage 6.0 (TID 8) in 47 ms on localhost (1/2)
17/12/12 20:57:24 INFO TaskSetManager: Finished task 1.0 in stage 6.0 (TID 9) in 47 ms on localhost (2/2)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Removed TaskSet 6.0, whose tasks have all completed, from pool 
17/12/12 20:57:24 INFO DAGScheduler: Stage 6 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92) finished in 0.048 s
17/12/12 20:57:24 INFO DAGScheduler: Job 2 finished: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92, took 0.111222 s
17/12/12 20:57:24 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 20:57:24 INFO SparkContext: Starting job: saveAsTextFile at NativeMethodAccessorImpl.java:-2
17/12/12 20:57:24 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 20:57:24 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 1 is 154 bytes
17/12/12 20:57:24 INFO DAGScheduler: Got job 3 (saveAsTextFile at NativeMethodAccessorImpl.java:-2) with 2 output partitions (allowLocal=false)
17/12/12 20:57:24 INFO DAGScheduler: Final stage: Stage 9(saveAsTextFile at NativeMethodAccessorImpl.java:-2)
17/12/12 20:57:24 INFO DAGScheduler: Parents of final stage: List(Stage 8)
17/12/12 20:57:24 INFO DAGScheduler: Missing parents: List()
17/12/12 20:57:24 INFO DAGScheduler: Submitting Stage 9 (MapPartitionsRDD[18] at saveAsTextFile at NativeMethodAccessorImpl.java:-2), which has no missing parents
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(154736) called with curMem=10624512, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_6 stored as values in memory (estimated size 151.1 KB, free 254.9 MB)
17/12/12 20:57:24 INFO MemoryStore: ensureFreeSpace(99304) called with curMem=10779248, maxMem=278019440
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_6_piece0 stored as bytes in memory (estimated size 97.0 KB, free 254.8 MB)
17/12/12 20:57:24 INFO BlockManagerInfo: Added broadcast_6_piece0 in memory on localhost:41309 (size: 97.0 KB, free: 255.2 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_6_piece0
17/12/12 20:57:24 INFO SparkContext: Created broadcast 6 from broadcast at DAGScheduler.scala:839
17/12/12 20:57:24 INFO DAGScheduler: Submitting 2 missing tasks from Stage 9 (MapPartitionsRDD[18] at saveAsTextFile at NativeMethodAccessorImpl.java:-2)
17/12/12 20:57:24 INFO TaskSchedulerImpl: Adding task set 9.0 with 2 tasks
17/12/12 20:57:24 INFO TaskSetManager: Starting task 0.0 in stage 9.0 (TID 10, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO TaskSetManager: Starting task 1.0 in stage 9.0 (TID 11, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:57:24 INFO Executor: Running task 1.0 in stage 9.0 (TID 11)
17/12/12 20:57:24 INFO Executor: Running task 0.0 in stage 9.0 (TID 10)
17/12/12 20:57:24 INFO BlockManager: Removing broadcast 5
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_5_piece0
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_5_piece0 of size 3507 dropped from memory (free 267144395)
17/12/12 20:57:24 INFO BlockManagerInfo: Removed broadcast_5_piece0 on localhost:41309 in memory (size: 3.4 KB, free: 255.2 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_5
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_5 of size 4816 dropped from memory (free 267149211)
17/12/12 20:57:24 INFO ContextCleaner: Cleaned broadcast 5
17/12/12 20:57:24 INFO BlockManager: Removing broadcast 4
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_4_piece0
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_4_piece0 of size 5359 dropped from memory (free 267154570)
17/12/12 20:57:24 INFO BlockManagerInfo: Removed broadcast_4_piece0 on localhost:41309 in memory (size: 5.2 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_4
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_4 of size 7008 dropped from memory (free 267161578)
17/12/12 20:57:24 INFO ContextCleaner: Cleaned broadcast 4
17/12/12 20:57:24 INFO BlockManager: Removing broadcast 3
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_3_piece0
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_3_piece0 of size 4575 dropped from memory (free 267166153)
17/12/12 20:57:24 INFO BlockManagerInfo: Removed broadcast_3_piece0 on localhost:41309 in memory (size: 4.5 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_3
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_3 of size 6080 dropped from memory (free 267172233)
17/12/12 20:57:24 INFO ContextCleaner: Cleaned broadcast 3
17/12/12 20:57:24 INFO BlockManager: Removing broadcast 2
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_2_piece0
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_2_piece0 of size 4484 dropped from memory (free 267176717)
17/12/12 20:57:24 INFO BlockManagerInfo: Removed broadcast_2_piece0 on localhost:41309 in memory (size: 4.4 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_2
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_2 of size 6064 dropped from memory (free 267182781)
17/12/12 20:57:24 INFO ContextCleaner: Cleaned broadcast 2
17/12/12 20:57:24 INFO BlockManager: Removing broadcast 1
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_1_piece0
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_1_piece0 of size 7370 dropped from memory (free 267190151)
17/12/12 20:57:24 INFO BlockManagerInfo: Removed broadcast_1_piece0 on localhost:41309 in memory (size: 7.2 KB, free: 255.3 MB)
17/12/12 20:57:24 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 20:57:24 INFO BlockManager: Removing block broadcast_1
17/12/12 20:57:24 INFO MemoryStore: Block broadcast_1 of size 9464 dropped from memory (free 267199615)
17/12/12 20:57:24 INFO ContextCleaner: Cleaned broadcast 1
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:57:24 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
17/12/12 20:57:24 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 20:57:24 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 20:57:24 INFO PythonRDD: Times: total = 49, boot = -241, init = 281, finish = 9
17/12/12 20:57:24 INFO PythonRDD: Times: total = 51, boot = -238, init = 278, finish = 11
17/12/12 20:57:25 INFO FileOutputCommitter: Saved output of task 'attempt_201712122057_0009_m_000001_11' to hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/lab12/radque_raster_1513133844.63.txt/_temporary/0/task_201712122057_0009_m_000001
17/12/12 20:57:25 INFO SparkHadoopMapRedUtil: attempt_201712122057_0009_m_000001_11: Committed
17/12/12 20:57:25 INFO FileOutputCommitter: Saved output of task 'attempt_201712122057_0009_m_000000_10' to hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/lab12/radque_raster_1513133844.63.txt/_temporary/0/task_201712122057_0009_m_000000
17/12/12 20:57:25 INFO SparkHadoopMapRedUtil: attempt_201712122057_0009_m_000000_10: Committed
17/12/12 20:57:25 INFO Executor: Finished task 0.0 in stage 9.0 (TID 10). 1890 bytes result sent to driver
17/12/12 20:57:25 INFO Executor: Finished task 1.0 in stage 9.0 (TID 11). 1890 bytes result sent to driver
17/12/12 20:57:25 INFO TaskSetManager: Finished task 0.0 in stage 9.0 (TID 10) in 257 ms on localhost (1/2)
17/12/12 20:57:25 INFO TaskSetManager: Finished task 1.0 in stage 9.0 (TID 11) in 258 ms on localhost (2/2)
17/12/12 20:57:25 INFO TaskSchedulerImpl: Removed TaskSet 9.0, whose tasks have all completed, from pool 
17/12/12 20:57:25 INFO DAGScheduler: Stage 9 (saveAsTextFile at NativeMethodAccessorImpl.java:-2) finished in 0.259 s
17/12/12 20:57:25 INFO DAGScheduler: Job 3 finished: saveAsTextFile at NativeMethodAccessorImpl.java:-2, took 0.331474 s
[Done]!!!!!
[karoth4@cg-hm08 problem4]$ hdfs dfs -ls
Found 10 items
drwx------   - karoth4 hdfs          0 2017-12-12 19:42 .Trash
drwx------   - karoth4 hdfs          0 2017-12-12 19:49 .staging
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 20:48 final
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 19:49 heatmap_output
drwxr-xr-x   - karoth4 hdfs          0 2017-11-29 13:29 kmeans_output
drwxr-xr-x   - karoth4 hdfs          0 2017-11-24 10:50 lab11
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 20:57 lab12
-rw-r--r--   3 karoth4 hdfs 2781761974 2017-11-14 15:49 ny_taxi_1.csv
drwxr-xr-x   - karoth4 hdfs          0 2017-11-24 11:08 result.txt
drwxr-xr-x   - karoth4 hdfs          0 2017-11-24 11:17 result_keywords.txt
[karoth4@cg-hm08 problem4]$ hdfs dfs -ls lab12
Found 6 items
drwxr-xr-x   - karoth4 hdfs          0 2017-12-04 12:11 lab12/const.counts
-rw-r--r--   3 karoth4 hdfs      44841 2017-12-04 11:45 lab12/const.txt
drwxr-xr-x   - karoth4 hdfs          0 2017-12-04 12:21 lab12/const2.counts
drwxr-xr-x   - karoth4 hdfs          0 2017-12-05 10:52 lab12/radque_raster_1512492723.09.txt
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 20:57 lab12/radque_raster_1513133844.63.txt
-rw-r--r--   3 karoth4 hdfs 2459600651 2017-12-04 11:46 lab12/trip_data_1.csv
[karoth4@cg-hm08 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 40.479636 40.930724 -74.402322 -73.630027 0.005
17/12/12 20:59:31 INFO SparkContext: Running Spark version 1.3.1
17/12/12 20:59:31 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/12/12 20:59:31 INFO SecurityManager: Changing view acls to: karoth4
17/12/12 20:59:31 INFO SecurityManager: Changing modify acls to: karoth4
17/12/12 20:59:31 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(karoth4); users with modify permissions: Set(karoth4)
17/12/12 20:59:31 INFO Slf4jLogger: Slf4jLogger started
17/12/12 20:59:31 INFO Remoting: Starting remoting
17/12/12 20:59:31 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:42449]
17/12/12 20:59:31 INFO Utils: Successfully started service 'sparkDriver' on port 42449.
17/12/12 20:59:31 INFO SparkEnv: Registering MapOutputTracker
17/12/12 20:59:31 INFO SparkEnv: Registering BlockManagerMaster
17/12/12 20:59:31 INFO DiskBlockManager: Created local directory at /tmp/spark-0fc24b33-d1c7-4593-b46d-de53cf803f9f/blockmgr-b20d4744-f89f-4efc-ac11-2f08d1acb966
17/12/12 20:59:31 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
17/12/12 20:59:31 INFO HttpFileServer: HTTP File server directory is /tmp/spark-2573f73d-2899-4729-beca-f930f84c491a/httpd-53c5c285-569a-447b-9aff-02c8489b7686
17/12/12 20:59:31 INFO HttpServer: Starting HTTP Server
17/12/12 20:59:31 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:59:31 INFO AbstractConnector: Started SocketConnector@0.0.0.0:33429
17/12/12 20:59:31 INFO Utils: Successfully started service 'HTTP file server' on port 33429.
17/12/12 20:59:31 INFO SparkEnv: Registering OutputCommitCoordinator
17/12/12 20:59:32 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 20:59:32 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
17/12/12 20:59:32 INFO Utils: Successfully started service 'SparkUI' on port 4040.
17/12/12 20:59:32 INFO SparkUI: Started SparkUI at http://cg-hm08.ncsa.illinois.edu:4040
17/12/12 20:59:32 INFO Utils: Copying /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py to /tmp/spark-66359bad-c2b7-4ad0-9819-d7ae2926281c/userFiles-60c3b2cc-4394-459e-80fd-6ac81bf68486/spark_taxiQuery.py
17/12/12 20:59:32 INFO SparkContext: Added file file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py at file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133972091
17/12/12 20:59:32 INFO Executor: Starting executor ID <driver> on host localhost
17/12/12 20:59:32 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:42449/user/HeartbeatReceiver
17/12/12 20:59:32 INFO NettyBlockTransferService: Server created on 41520
17/12/12 20:59:32 INFO BlockManagerMaster: Trying to register BlockManager
17/12/12 20:59:32 INFO BlockManagerMasterActor: Registering block manager localhost:41520 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 41520)
17/12/12 20:59:32 INFO BlockManagerMaster: Registered BlockManager
17/12/12 20:59:32 INFO MemoryStore: ensureFreeSpace(314268) called with curMem=0, maxMem=278019440
17/12/12 20:59:32 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 306.9 KB, free 264.8 MB)
17/12/12 20:59:32 INFO MemoryStore: ensureFreeSpace(46158) called with curMem=314268, maxMem=278019440
17/12/12 20:59:32 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 45.1 KB, free 264.8 MB)
17/12/12 20:59:32 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:41520 (size: 45.1 KB, free: 265.1 MB)
17/12/12 20:59:32 INFO BlockManagerMaster: Updated info of block broadcast_0_piece0
17/12/12 20:59:32 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:-2
17/12/12 20:59:32 WARN DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
17/12/12 20:59:32 INFO FileInputFormat: Total input paths to process : 1
17/12/12 20:59:33 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91
17/12/12 20:59:33 INFO DAGScheduler: Registering RDD 5 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:33 INFO DAGScheduler: Got job 0 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) with 2 output partitions (allowLocal=false)
17/12/12 20:59:33 INFO DAGScheduler: Final stage: Stage 1(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:33 INFO DAGScheduler: Parents of final stage: List(Stage 0)
17/12/12 20:59:33 INFO DAGScheduler: Missing parents: List(Stage 0)
17/12/12 20:59:33 INFO DAGScheduler: Submitting Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:59:33 INFO MemoryStore: ensureFreeSpace(9464) called with curMem=360426, maxMem=278019440
17/12/12 20:59:33 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 9.2 KB, free 264.8 MB)
17/12/12 20:59:33 INFO MemoryStore: ensureFreeSpace(7370) called with curMem=369890, maxMem=278019440
17/12/12 20:59:33 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 7.2 KB, free 264.8 MB)
17/12/12 20:59:33 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on localhost:41520 (size: 7.2 KB, free: 265.1 MB)
17/12/12 20:59:33 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 20:59:33 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:839
17/12/12 20:59:33 INFO DAGScheduler: Submitting 2 missing tasks from Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:33 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks
17/12/12 20:59:33 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, ANY, 1406 bytes)
17/12/12 20:59:33 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1, localhost, ANY, 1406 bytes)
17/12/12 20:59:33 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
17/12/12 20:59:33 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
17/12/12 20:59:33 INFO Executor: Fetching file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513133972091
17/12/12 20:59:33 INFO Utils: /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py has been previously copied to /tmp/spark-66359bad-c2b7-4ad0-9819-d7ae2926281c/userFiles-60c3b2cc-4394-459e-80fd-6ac81bf68486/spark_taxiQuery.py
17/12/12 20:59:38 INFO CacheManager: Partition rdd_2_1 not found, computing it
17/12/12 20:59:38 INFO CacheManager: Partition rdd_2_0 not found, computing it
17/12/12 20:59:38 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:8619300+8619301
17/12/12 20:59:38 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:0+8619300
17/12/12 20:59:38 INFO deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/12/12 20:59:38 INFO deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/12/12 20:59:38 INFO deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/12/12 20:59:38 INFO deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/12/12 20:59:38 INFO deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/12/12 20:59:39 INFO PythonRDD: Times: total = 490, boot = 5, init = 138, finish = 347
17/12/12 20:59:39 INFO PythonRDD: Times: total = 504, boot = 3, init = 139, finish = 362
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(5090891) called with curMem=377260, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block rdd_2_0 stored as bytes in memory (estimated size 4.9 MB, free 259.9 MB)
17/12/12 20:59:39 INFO BlockManagerInfo: Added rdd_2_0 in memory on localhost:41520 (size: 4.9 MB, free: 260.2 MB)
17/12/12 20:59:39 INFO BlockManagerMaster: Updated info of block rdd_2_0
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(5114468) called with curMem=5468151, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block rdd_2_1 stored as bytes in memory (estimated size 4.9 MB, free 255.0 MB)
17/12/12 20:59:39 INFO BlockManagerInfo: Added rdd_2_1 in memory on localhost:41520 (size: 4.9 MB, free: 255.4 MB)
17/12/12 20:59:39 INFO BlockManagerMaster: Updated info of block rdd_2_1
17/12/12 20:59:39 INFO PythonRDD: Times: total = 6470, boot = 5494, init = 561, finish = 415
17/12/12 20:59:39 INFO PythonRDD: Times: total = 6469, boot = 5489, init = 556, finish = 424
17/12/12 20:59:39 INFO Executor: Finished task 1.0 in stage 0.0 (TID 1). 2635 bytes result sent to driver
17/12/12 20:59:39 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 2635 bytes result sent to driver
17/12/12 20:59:39 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 6557 ms on localhost (1/2)
17/12/12 20:59:39 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 6566 ms on localhost (2/2)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
17/12/12 20:59:39 INFO DAGScheduler: Stage 0 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 6.576 s
17/12/12 20:59:39 INFO DAGScheduler: looking for newly runnable stages
17/12/12 20:59:39 INFO DAGScheduler: running: Set()
17/12/12 20:59:39 INFO DAGScheduler: waiting: Set(Stage 1)
17/12/12 20:59:39 INFO DAGScheduler: failed: Set()
17/12/12 20:59:39 INFO DAGScheduler: Missing parents for Stage 1: List()
17/12/12 20:59:39 INFO DAGScheduler: Submitting Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which is now runnable
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(6064) called with curMem=10582619, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(4484) called with curMem=10588683, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 4.4 KB, free 255.0 MB)
17/12/12 20:59:39 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on localhost:41520 (size: 4.4 KB, free: 255.4 MB)
17/12/12 20:59:39 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 20:59:39 INFO SparkContext: Created broadcast 2 from broadcast at DAGScheduler.scala:839
17/12/12 20:59:39 INFO DAGScheduler: Submitting 2 missing tasks from Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Adding task set 1.0 with 2 tasks
17/12/12 20:59:39 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 2, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:39 INFO TaskSetManager: Starting task 1.0 in stage 1.0 (TID 3, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:39 INFO Executor: Running task 0.0 in stage 1.0 (TID 2)
17/12/12 20:59:39 INFO Executor: Running task 1.0 in stage 1.0 (TID 3)
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 20:59:39 INFO PythonRDD: Times: total = 43, boot = -501, init = 541, finish = 3
17/12/12 20:59:39 INFO PythonRDD: Times: total = 44, boot = -517, init = 558, finish = 3
17/12/12 20:59:39 INFO Executor: Finished task 0.0 in stage 1.0 (TID 2). 965 bytes result sent to driver
17/12/12 20:59:39 INFO Executor: Finished task 1.0 in stage 1.0 (TID 3). 965 bytes result sent to driver
17/12/12 20:59:39 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 2) in 51 ms on localhost (1/2)
17/12/12 20:59:39 INFO TaskSetManager: Finished task 1.0 in stage 1.0 (TID 3) in 50 ms on localhost (2/2)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
17/12/12 20:59:39 INFO DAGScheduler: Stage 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.051 s
17/12/12 20:59:39 INFO DAGScheduler: Job 0 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91, took 6.691540 s
17/12/12 20:59:39 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91
17/12/12 20:59:39 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 20:59:39 INFO DAGScheduler: Got job 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) with 2 output partitions (allowLocal=false)
17/12/12 20:59:39 INFO DAGScheduler: Final stage: Stage 3(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:39 INFO DAGScheduler: Parents of final stage: List(Stage 2)
17/12/12 20:59:39 INFO DAGScheduler: Missing parents: List()
17/12/12 20:59:39 INFO DAGScheduler: Submitting Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(6080) called with curMem=10593167, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(4575) called with curMem=10599247, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 4.5 KB, free 255.0 MB)
17/12/12 20:59:39 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on localhost:41520 (size: 4.5 KB, free: 255.3 MB)
17/12/12 20:59:39 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 20:59:39 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:839
17/12/12 20:59:39 INFO DAGScheduler: Submitting 2 missing tasks from Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Adding task set 3.0 with 2 tasks
17/12/12 20:59:39 INFO TaskSetManager: Starting task 0.0 in stage 3.0 (TID 4, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:39 INFO TaskSetManager: Starting task 1.0 in stage 3.0 (TID 5, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:39 INFO Executor: Running task 1.0 in stage 3.0 (TID 5)
17/12/12 20:59:39 INFO Executor: Running task 0.0 in stage 3.0 (TID 4)
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:39 INFO PythonRDD: Times: total = 4, boot = -108, init = 110, finish = 2
17/12/12 20:59:39 INFO Executor: Finished task 1.0 in stage 3.0 (TID 5). 1294 bytes result sent to driver
17/12/12 20:59:39 INFO TaskSetManager: Finished task 1.0 in stage 3.0 (TID 5) in 9 ms on localhost (1/2)
17/12/12 20:59:39 INFO PythonRDD: Times: total = 43, boot = -107, init = 148, finish = 2
17/12/12 20:59:39 INFO Executor: Finished task 0.0 in stage 3.0 (TID 4). 1217 bytes result sent to driver
17/12/12 20:59:39 INFO TaskSetManager: Finished task 0.0 in stage 3.0 (TID 4) in 47 ms on localhost (2/2)
17/12/12 20:59:39 INFO DAGScheduler: Stage 3 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.047 s
17/12/12 20:59:39 INFO TaskSchedulerImpl: Removed TaskSet 3.0, whose tasks have all completed, from pool 
17/12/12 20:59:39 INFO DAGScheduler: Job 1 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91, took 0.056223 s
17/12/12 20:59:39 INFO SparkContext: Starting job: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92
17/12/12 20:59:39 INFO DAGScheduler: Registering RDD 12 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:39 INFO DAGScheduler: Got job 2 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92) with 2 output partitions (allowLocal=false)
17/12/12 20:59:39 INFO DAGScheduler: Final stage: Stage 6(collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92)
17/12/12 20:59:39 INFO DAGScheduler: Parents of final stage: List(Stage 5)
17/12/12 20:59:39 INFO DAGScheduler: Missing parents: List(Stage 5)
17/12/12 20:59:39 INFO DAGScheduler: Submitting Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91), which has no missing parents
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(7008) called with curMem=10603822, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_4 stored as values in memory (estimated size 6.8 KB, free 255.0 MB)
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(5357) called with curMem=10610830, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_4_piece0 stored as bytes in memory (estimated size 5.2 KB, free 255.0 MB)
17/12/12 20:59:39 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on localhost:41520 (size: 5.2 KB, free: 255.3 MB)
17/12/12 20:59:39 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 20:59:39 INFO SparkContext: Created broadcast 4 from broadcast at DAGScheduler.scala:839
17/12/12 20:59:39 INFO DAGScheduler: Submitting 2 missing tasks from Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Adding task set 5.0 with 2 tasks
17/12/12 20:59:39 INFO TaskSetManager: Starting task 0.0 in stage 5.0 (TID 6, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 20:59:39 INFO TaskSetManager: Starting task 1.0 in stage 5.0 (TID 7, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 20:59:39 INFO Executor: Running task 0.0 in stage 5.0 (TID 6)
17/12/12 20:59:39 INFO Executor: Running task 1.0 in stage 5.0 (TID 7)
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
17/12/12 20:59:39 INFO PythonRDD: Times: total = 44, boot = -79, init = 119, finish = 4
17/12/12 20:59:39 INFO PythonRDD: Times: total = 44, boot = -79, init = 119, finish = 4
17/12/12 20:59:39 INFO Executor: Finished task 1.0 in stage 5.0 (TID 7). 1160 bytes result sent to driver
17/12/12 20:59:39 INFO Executor: Finished task 0.0 in stage 5.0 (TID 6). 1160 bytes result sent to driver
17/12/12 20:59:39 INFO TaskSetManager: Finished task 1.0 in stage 5.0 (TID 7) in 51 ms on localhost (1/2)
17/12/12 20:59:39 INFO TaskSetManager: Finished task 0.0 in stage 5.0 (TID 6) in 52 ms on localhost (2/2)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Removed TaskSet 5.0, whose tasks have all completed, from pool 
17/12/12 20:59:39 INFO DAGScheduler: Stage 5 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:91) finished in 0.052 s
17/12/12 20:59:39 INFO DAGScheduler: looking for newly runnable stages
17/12/12 20:59:39 INFO DAGScheduler: running: Set()
17/12/12 20:59:39 INFO DAGScheduler: waiting: Set(Stage 6)
17/12/12 20:59:39 INFO DAGScheduler: failed: Set()
17/12/12 20:59:39 INFO DAGScheduler: Missing parents for Stage 6: List()
17/12/12 20:59:39 INFO DAGScheduler: Submitting Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92), which is now runnable
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(4816) called with curMem=10616187, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_5 stored as values in memory (estimated size 4.7 KB, free 255.0 MB)
17/12/12 20:59:39 INFO MemoryStore: ensureFreeSpace(3507) called with curMem=10621003, maxMem=278019440
17/12/12 20:59:39 INFO MemoryStore: Block broadcast_5_piece0 stored as bytes in memory (estimated size 3.4 KB, free 255.0 MB)
17/12/12 20:59:39 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on localhost:41520 (size: 3.4 KB, free: 255.3 MB)
17/12/12 20:59:39 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 20:59:39 INFO SparkContext: Created broadcast 5 from broadcast at DAGScheduler.scala:839
17/12/12 20:59:39 INFO DAGScheduler: Submitting 2 missing tasks from Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Adding task set 6.0 with 2 tasks
17/12/12 20:59:39 INFO TaskSetManager: Starting task 0.0 in stage 6.0 (TID 8, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:39 INFO TaskSetManager: Starting task 1.0 in stage 6.0 (TID 9, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:39 INFO Executor: Running task 1.0 in stage 6.0 (TID 9)
17/12/12 20:59:39 INFO Executor: Running task 0.0 in stage 6.0 (TID 8)
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:39 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:39 INFO PythonRDD: Times: total = 43, boot = -67, init = 108, finish = 2
17/12/12 20:59:39 INFO PythonRDD: Times: total = 44, boot = -104, init = 145, finish = 3
17/12/12 20:59:39 INFO Executor: Finished task 1.0 in stage 6.0 (TID 9). 20473 bytes result sent to driver
17/12/12 20:59:39 INFO Executor: Finished task 0.0 in stage 6.0 (TID 8). 17054 bytes result sent to driver
17/12/12 20:59:39 INFO TaskSetManager: Finished task 1.0 in stage 6.0 (TID 9) in 47 ms on localhost (1/2)
17/12/12 20:59:39 INFO TaskSetManager: Finished task 0.0 in stage 6.0 (TID 8) in 48 ms on localhost (2/2)
17/12/12 20:59:39 INFO TaskSchedulerImpl: Removed TaskSet 6.0, whose tasks have all completed, from pool 
17/12/12 20:59:39 INFO DAGScheduler: Stage 6 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92) finished in 0.048 s
17/12/12 20:59:39 INFO DAGScheduler: Job 2 finished: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:92, took 0.114108 s
17/12/12 20:59:39 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 20:59:39 INFO SparkContext: Starting job: saveAsTextFile at NativeMethodAccessorImpl.java:-2
17/12/12 20:59:39 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 20:59:39 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 1 is 154 bytes
17/12/12 20:59:39 INFO DAGScheduler: Got job 3 (saveAsTextFile at NativeMethodAccessorImpl.java:-2) with 2 output partitions (allowLocal=false)
17/12/12 20:59:39 INFO DAGScheduler: Final stage: Stage 9(saveAsTextFile at NativeMethodAccessorImpl.java:-2)
17/12/12 20:59:39 INFO DAGScheduler: Parents of final stage: List(Stage 8)
17/12/12 20:59:39 INFO DAGScheduler: Missing parents: List()
17/12/12 20:59:39 INFO DAGScheduler: Submitting Stage 9 (MapPartitionsRDD[18] at saveAsTextFile at NativeMethodAccessorImpl.java:-2), which has no missing parents
17/12/12 20:59:40 INFO MemoryStore: ensureFreeSpace(154752) called with curMem=10624510, maxMem=278019440
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_6 stored as values in memory (estimated size 151.1 KB, free 254.9 MB)
17/12/12 20:59:40 INFO MemoryStore: ensureFreeSpace(99253) called with curMem=10779262, maxMem=278019440
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_6_piece0 stored as bytes in memory (estimated size 96.9 KB, free 254.8 MB)
17/12/12 20:59:40 INFO BlockManagerInfo: Added broadcast_6_piece0 in memory on localhost:41520 (size: 96.9 KB, free: 255.2 MB)
17/12/12 20:59:40 INFO BlockManagerMaster: Updated info of block broadcast_6_piece0
17/12/12 20:59:40 INFO SparkContext: Created broadcast 6 from broadcast at DAGScheduler.scala:839
17/12/12 20:59:40 INFO DAGScheduler: Submitting 2 missing tasks from Stage 9 (MapPartitionsRDD[18] at saveAsTextFile at NativeMethodAccessorImpl.java:-2)
17/12/12 20:59:40 INFO TaskSchedulerImpl: Adding task set 9.0 with 2 tasks
17/12/12 20:59:40 INFO TaskSetManager: Starting task 0.0 in stage 9.0 (TID 10, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:40 INFO TaskSetManager: Starting task 1.0 in stage 9.0 (TID 11, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 20:59:40 INFO Executor: Running task 0.0 in stage 9.0 (TID 10)
17/12/12 20:59:40 INFO Executor: Running task 1.0 in stage 9.0 (TID 11)
17/12/12 20:59:40 INFO BlockManager: Removing broadcast 2
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_2_piece0
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_2_piece0 of size 4484 dropped from memory (free 267145409)
17/12/12 20:59:40 INFO BlockManagerInfo: Removed broadcast_2_piece0 on localhost:41520 in memory (size: 4.4 KB, free: 255.2 MB)
17/12/12 20:59:40 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_2
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_2 of size 6064 dropped from memory (free 267151473)
17/12/12 20:59:40 INFO ContextCleaner: Cleaned broadcast 2
17/12/12 20:59:40 INFO BlockManager: Removing broadcast 1
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_1_piece0
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_1_piece0 of size 7370 dropped from memory (free 267158843)
17/12/12 20:59:40 INFO BlockManagerInfo: Removed broadcast_1_piece0 on localhost:41520 in memory (size: 7.2 KB, free: 255.3 MB)
17/12/12 20:59:40 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_1
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_1 of size 9464 dropped from memory (free 267168307)
17/12/12 20:59:40 INFO ContextCleaner: Cleaned broadcast 1
17/12/12 20:59:40 INFO BlockManager: Removing broadcast 3
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_3_piece0
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_3_piece0 of size 4575 dropped from memory (free 267172882)
17/12/12 20:59:40 INFO BlockManagerInfo: Removed broadcast_3_piece0 on localhost:41520 in memory (size: 4.5 KB, free: 255.3 MB)
17/12/12 20:59:40 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_3
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_3 of size 6080 dropped from memory (free 267178962)
17/12/12 20:59:40 INFO ContextCleaner: Cleaned broadcast 3
17/12/12 20:59:40 INFO BlockManager: Removing broadcast 4
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_4_piece0
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_4_piece0 of size 5357 dropped from memory (free 267184319)
17/12/12 20:59:40 INFO BlockManagerInfo: Removed broadcast_4_piece0 on localhost:41520 in memory (size: 5.2 KB, free: 255.3 MB)
17/12/12 20:59:40 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_4
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_4 of size 7008 dropped from memory (free 267191327)
17/12/12 20:59:40 INFO ContextCleaner: Cleaned broadcast 4
17/12/12 20:59:40 INFO BlockManager: Removing broadcast 5
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_5_piece0
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_5_piece0 of size 3507 dropped from memory (free 267194834)
17/12/12 20:59:40 INFO BlockManagerInfo: Removed broadcast_5_piece0 on localhost:41520 in memory (size: 3.4 KB, free: 255.3 MB)
17/12/12 20:59:40 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 20:59:40 INFO BlockManager: Removing block broadcast_5
17/12/12 20:59:40 INFO MemoryStore: Block broadcast_5 of size 4816 dropped from memory (free 267199650)
17/12/12 20:59:40 INFO ContextCleaner: Cleaned broadcast 5
17/12/12 20:59:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:40 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 20:59:40 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 20:59:40 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 20:59:40 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 20:59:40 INFO PythonRDD: Times: total = 47, boot = -252, init = 293, finish = 6
17/12/12 20:59:40 INFO PythonRDD: Times: total = 46, boot = -246, init = 286, finish = 6
17/12/12 20:59:40 INFO FileOutputCommitter: Saved output of task 'attempt_201712122059_0009_m_000001_11' to hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/radque_raster_1513133979.93.txt/_temporary/0/task_201712122059_0009_m_000001
17/12/12 20:59:40 INFO SparkHadoopMapRedUtil: attempt_201712122059_0009_m_000001_11: Committed
17/12/12 20:59:40 INFO FileOutputCommitter: Saved output of task 'attempt_201712122059_0009_m_000000_10' to hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/radque_raster_1513133979.93.txt/_temporary/0/task_201712122059_0009_m_000000
17/12/12 20:59:40 INFO SparkHadoopMapRedUtil: attempt_201712122059_0009_m_000000_10: Committed
17/12/12 20:59:40 INFO Executor: Finished task 1.0 in stage 9.0 (TID 11). 1890 bytes result sent to driver
17/12/12 20:59:40 INFO Executor: Finished task 0.0 in stage 9.0 (TID 10). 1890 bytes result sent to driver
17/12/12 20:59:40 INFO TaskSetManager: Finished task 1.0 in stage 9.0 (TID 11) in 248 ms on localhost (1/2)
17/12/12 20:59:40 INFO TaskSetManager: Finished task 0.0 in stage 9.0 (TID 10) in 249 ms on localhost (2/2)
17/12/12 20:59:40 INFO TaskSchedulerImpl: Removed TaskSet 9.0, whose tasks have all completed, from pool 
17/12/12 20:59:40 INFO DAGScheduler: Stage 9 (saveAsTextFile at NativeMethodAccessorImpl.java:-2) finished in 0.249 s
17/12/12 20:59:40 INFO DAGScheduler: Job 3 finished: saveAsTextFile at NativeMethodAccessorImpl.java:-2, took 0.316017 s
[Done]!!!!!
[karoth4@cg-hm08 problem4]$ hdfs dfs -ls final/problem4/
Found 3 items
-rw-r--r--   3 karoth4 hdfs   17238601 2017-12-12 20:48 final/problem4/311_data.csv
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 20:59 final/problem4/radque_raster_1513133979.93.txt
-rw-r--r--   3 karoth4 hdfs       2656 2017-12-12 20:48 final/problem4/spark_taxiQuery.py
[karoth4@cg-hm08 problem4]$ hdfs dfs -getmerge final/problem4/radque_raster_%.txt ~/final/problem4/result.txt
getmerge: `final/problem4/radque_raster_%.txt': No such file or directory
[karoth4@cg-hm08 problem4]$ hdfs dfs -getmerge final/problem4/radque_raster_1513133979.93.txt ~/final/problem4/result.txt
[karoth4@cg-hm08 problem4]$ ls
311_data.csv  result.txt  spark_taxiQuery.py
[karoth4@cg-hm08 problem4]$ vim result.txt 
[karoth4@cg-hm08 problem4]$ vim spark_taxiQuery.py 
[karoth4@cg-hm08 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 41.64 42.03 -87.91 -87.52 0.005
17/12/12 21:07:40 INFO SparkContext: Running Spark version 1.3.1
17/12/12 21:07:40 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/12/12 21:07:40 INFO SecurityManager: Changing view acls to: karoth4
17/12/12 21:07:40 INFO SecurityManager: Changing modify acls to: karoth4
17/12/12 21:07:40 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(karoth4); users with modify permissions: Set(karoth4)
17/12/12 21:07:40 INFO Slf4jLogger: Slf4jLogger started
17/12/12 21:07:40 INFO Remoting: Starting remoting
17/12/12 21:07:40 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:37964]
17/12/12 21:07:40 INFO Utils: Successfully started service 'sparkDriver' on port 37964.
17/12/12 21:07:40 INFO SparkEnv: Registering MapOutputTracker
17/12/12 21:07:40 INFO SparkEnv: Registering BlockManagerMaster
17/12/12 21:07:40 INFO DiskBlockManager: Created local directory at /tmp/spark-3e6531bd-87ef-49e5-8efa-b857253c0912/blockmgr-ea930e01-62f1-4289-92d0-45b2fd647c1c
17/12/12 21:07:40 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
17/12/12 21:07:40 INFO HttpFileServer: HTTP File server directory is /tmp/spark-ff942c43-a0ee-4364-948c-8dae38accd8f/httpd-723be880-2641-406a-8a61-b60411c1c67c
17/12/12 21:07:40 INFO HttpServer: Starting HTTP Server
17/12/12 21:07:40 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 21:07:40 INFO AbstractConnector: Started SocketConnector@0.0.0.0:32819
17/12/12 21:07:40 INFO Utils: Successfully started service 'HTTP file server' on port 32819.
17/12/12 21:07:40 INFO SparkEnv: Registering OutputCommitCoordinator
17/12/12 21:07:40 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 21:07:40 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
17/12/12 21:07:40 INFO Utils: Successfully started service 'SparkUI' on port 4040.
17/12/12 21:07:40 INFO SparkUI: Started SparkUI at http://cg-hm08.ncsa.illinois.edu:4040
17/12/12 21:07:41 INFO Utils: Copying /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py to /tmp/spark-7ed5f09a-ac10-4543-a9c3-52080fc37245/userFiles-c7493582-7f0e-4605-82e6-3a4b4c93057a/spark_taxiQuery.py
17/12/12 21:07:41 INFO SparkContext: Added file file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py at file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513134461061
17/12/12 21:07:41 INFO Executor: Starting executor ID <driver> on host localhost
17/12/12 21:07:41 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:37964/user/HeartbeatReceiver
17/12/12 21:07:41 INFO NettyBlockTransferService: Server created on 36715
17/12/12 21:07:41 INFO BlockManagerMaster: Trying to register BlockManager
17/12/12 21:07:41 INFO BlockManagerMasterActor: Registering block manager localhost:36715 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 36715)
17/12/12 21:07:41 INFO BlockManagerMaster: Registered BlockManager
17/12/12 21:07:41 INFO MemoryStore: ensureFreeSpace(314268) called with curMem=0, maxMem=278019440
17/12/12 21:07:41 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 306.9 KB, free 264.8 MB)
17/12/12 21:07:41 INFO MemoryStore: ensureFreeSpace(46158) called with curMem=314268, maxMem=278019440
17/12/12 21:07:41 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 45.1 KB, free 264.8 MB)
17/12/12 21:07:41 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:36715 (size: 45.1 KB, free: 265.1 MB)
17/12/12 21:07:41 INFO BlockManagerMaster: Updated info of block broadcast_0_piece0
17/12/12 21:07:41 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:-2
17/12/12 21:07:41 WARN DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
17/12/12 21:07:42 INFO FileInputFormat: Total input paths to process : 1
17/12/12 21:07:42 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97
17/12/12 21:07:42 INFO DAGScheduler: Registering RDD 5 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:42 INFO DAGScheduler: Got job 0 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) with 2 output partitions (allowLocal=false)
17/12/12 21:07:42 INFO DAGScheduler: Final stage: Stage 1(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:42 INFO DAGScheduler: Parents of final stage: List(Stage 0)
17/12/12 21:07:42 INFO DAGScheduler: Missing parents: List(Stage 0)
17/12/12 21:07:42 INFO DAGScheduler: Submitting Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97), which has no missing parents
17/12/12 21:07:42 INFO MemoryStore: ensureFreeSpace(9576) called with curMem=360426, maxMem=278019440
17/12/12 21:07:42 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 9.4 KB, free 264.8 MB)
17/12/12 21:07:42 INFO MemoryStore: ensureFreeSpace(7476) called with curMem=370002, maxMem=278019440
17/12/12 21:07:42 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 7.3 KB, free 264.8 MB)
17/12/12 21:07:42 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on localhost:36715 (size: 7.3 KB, free: 265.1 MB)
17/12/12 21:07:42 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 21:07:42 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:839
17/12/12 21:07:42 INFO DAGScheduler: Submitting 2 missing tasks from Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:42 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks
17/12/12 21:07:42 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, ANY, 1406 bytes)
17/12/12 21:07:42 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1, localhost, ANY, 1406 bytes)
17/12/12 21:07:42 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
17/12/12 21:07:42 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
17/12/12 21:07:42 INFO Executor: Fetching file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513134461061
17/12/12 21:07:42 INFO Utils: /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py has been previously copied to /tmp/spark-7ed5f09a-ac10-4543-a9c3-52080fc37245/userFiles-c7493582-7f0e-4605-82e6-3a4b4c93057a/spark_taxiQuery.py
17/12/12 21:07:47 INFO CacheManager: Partition rdd_2_0 not found, computing it
17/12/12 21:07:47 INFO CacheManager: Partition rdd_2_1 not found, computing it
17/12/12 21:07:47 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:0+8619300
17/12/12 21:07:47 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:8619300+8619301
17/12/12 21:07:47 INFO deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/12/12 21:07:47 INFO deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/12/12 21:07:47 INFO deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/12/12 21:07:47 INFO deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/12/12 21:07:47 INFO deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/12/12 21:07:47 INFO PythonRDD: Times: total = 512, boot = 3, init = 186, finish = 323
17/12/12 21:07:47 INFO PythonRDD: Times: total = 517, boot = 6, init = 183, finish = 328
17/12/12 21:07:47 INFO MemoryStore: ensureFreeSpace(5090891) called with curMem=377478, maxMem=278019440
17/12/12 21:07:47 INFO MemoryStore: Block rdd_2_0 stored as bytes in memory (estimated size 4.9 MB, free 259.9 MB)
17/12/12 21:07:47 INFO BlockManagerInfo: Added rdd_2_0 in memory on localhost:36715 (size: 4.9 MB, free: 260.2 MB)
17/12/12 21:07:47 INFO BlockManagerMaster: Updated info of block rdd_2_0
17/12/12 21:07:47 INFO MemoryStore: ensureFreeSpace(5114468) called with curMem=5468369, maxMem=278019440
17/12/12 21:07:47 INFO MemoryStore: Block rdd_2_1 stored as bytes in memory (estimated size 4.9 MB, free 255.0 MB)
17/12/12 21:07:47 INFO BlockManagerInfo: Added rdd_2_1 in memory on localhost:36715 (size: 4.9 MB, free: 255.4 MB)
17/12/12 21:07:47 INFO BlockManagerMaster: Updated info of block rdd_2_1
17/12/12 21:07:48 INFO PythonRDD: Times: total = 5886, boot = 4863, init = 581, finish = 442
17/12/12 21:07:48 INFO PythonRDD: Times: total = 5881, boot = 4867, init = 571, finish = 443
17/12/12 21:07:48 INFO Executor: Finished task 1.0 in stage 0.0 (TID 1). 2635 bytes result sent to driver
17/12/12 21:07:48 INFO Executor: Finished task 0.0 in stage 0.0 (TID 0). 2635 bytes result sent to driver
17/12/12 21:07:48 INFO TaskSetManager: Finished task 0.0 in stage 0.0 (TID 0) in 5975 ms on localhost (1/2)
17/12/12 21:07:48 INFO TaskSetManager: Finished task 1.0 in stage 0.0 (TID 1) in 5970 ms on localhost (2/2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
17/12/12 21:07:48 INFO DAGScheduler: Stage 0 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) finished in 5.989 s
17/12/12 21:07:48 INFO DAGScheduler: looking for newly runnable stages
17/12/12 21:07:48 INFO DAGScheduler: running: Set()
17/12/12 21:07:48 INFO DAGScheduler: waiting: Set(Stage 1)
17/12/12 21:07:48 INFO DAGScheduler: failed: Set()
17/12/12 21:07:48 INFO DAGScheduler: Missing parents for Stage 1: List()
17/12/12 21:07:48 INFO DAGScheduler: Submitting Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97), which is now runnable
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(6064) called with curMem=10582837, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_2 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(4484) called with curMem=10588901, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_2_piece0 stored as bytes in memory (estimated size 4.4 KB, free 255.0 MB)
17/12/12 21:07:48 INFO BlockManagerInfo: Added broadcast_2_piece0 in memory on localhost:36715 (size: 4.4 KB, free: 255.4 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 21:07:48 INFO SparkContext: Created broadcast 2 from broadcast at DAGScheduler.scala:839
17/12/12 21:07:48 INFO DAGScheduler: Submitting 2 missing tasks from Stage 1 (PythonRDD[9] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Adding task set 1.0 with 2 tasks
17/12/12 21:07:48 INFO TaskSetManager: Starting task 0.0 in stage 1.0 (TID 2, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO TaskSetManager: Starting task 1.0 in stage 1.0 (TID 3, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO Executor: Running task 0.0 in stage 1.0 (TID 2)
17/12/12 21:07:48 INFO Executor: Running task 1.0 in stage 1.0 (TID 3)
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 3 ms
17/12/12 21:07:48 INFO PythonRDD: Times: total = 43, boot = -525, init = 565, finish = 3
17/12/12 21:07:48 INFO PythonRDD: Times: total = 44, boot = -529, init = 570, finish = 3
17/12/12 21:07:48 INFO Executor: Finished task 0.0 in stage 1.0 (TID 2). 965 bytes result sent to driver
17/12/12 21:07:48 INFO Executor: Finished task 1.0 in stage 1.0 (TID 3). 965 bytes result sent to driver
17/12/12 21:07:48 INFO TaskSetManager: Finished task 0.0 in stage 1.0 (TID 2) in 52 ms on localhost (1/2)
17/12/12 21:07:48 INFO TaskSetManager: Finished task 1.0 in stage 1.0 (TID 3) in 51 ms on localhost (2/2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Removed TaskSet 1.0, whose tasks have all completed, from pool 
17/12/12 21:07:48 INFO DAGScheduler: Stage 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) finished in 0.054 s
17/12/12 21:07:48 INFO DAGScheduler: Job 0 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97, took 6.105763 s
17/12/12 21:07:48 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97
17/12/12 21:07:48 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 21:07:48 INFO DAGScheduler: Got job 1 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) with 2 output partitions (allowLocal=false)
17/12/12 21:07:48 INFO DAGScheduler: Final stage: Stage 3(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:48 INFO DAGScheduler: Parents of final stage: List(Stage 2)
17/12/12 21:07:48 INFO DAGScheduler: Missing parents: List()
17/12/12 21:07:48 INFO DAGScheduler: Submitting Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97), which has no missing parents
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(6080) called with curMem=10593385, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_3 stored as values in memory (estimated size 5.9 KB, free 255.0 MB)
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(4575) called with curMem=10599465, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_3_piece0 stored as bytes in memory (estimated size 4.5 KB, free 255.0 MB)
17/12/12 21:07:48 INFO BlockManagerInfo: Added broadcast_3_piece0 in memory on localhost:36715 (size: 4.5 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 21:07:48 INFO SparkContext: Created broadcast 3 from broadcast at DAGScheduler.scala:839
17/12/12 21:07:48 INFO DAGScheduler: Submitting 2 missing tasks from Stage 3 (PythonRDD[10] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Adding task set 3.0 with 2 tasks
17/12/12 21:07:48 INFO TaskSetManager: Starting task 0.0 in stage 3.0 (TID 4, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO TaskSetManager: Starting task 1.0 in stage 3.0 (TID 5, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO Executor: Running task 1.0 in stage 3.0 (TID 5)
17/12/12 21:07:48 INFO Executor: Running task 0.0 in stage 3.0 (TID 4)
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 21:07:48 INFO PythonRDD: Times: total = 5, boot = -104, init = 106, finish = 3
17/12/12 21:07:48 INFO Executor: Finished task 1.0 in stage 3.0 (TID 5). 1205 bytes result sent to driver
17/12/12 21:07:48 INFO PythonRDD: Times: total = 5, boot = -103, init = 106, finish = 2
17/12/12 21:07:48 INFO Executor: Finished task 0.0 in stage 3.0 (TID 4). 1156 bytes result sent to driver
17/12/12 21:07:48 INFO TaskSetManager: Finished task 1.0 in stage 3.0 (TID 5) in 9 ms on localhost (1/2)
17/12/12 21:07:48 INFO TaskSetManager: Finished task 0.0 in stage 3.0 (TID 4) in 9 ms on localhost (2/2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Removed TaskSet 3.0, whose tasks have all completed, from pool 
17/12/12 21:07:48 INFO DAGScheduler: Stage 3 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) finished in 0.010 s
17/12/12 21:07:48 INFO DAGScheduler: Job 1 finished: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97, took 0.017976 s
17/12/12 21:07:48 INFO SparkContext: Starting job: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98
17/12/12 21:07:48 INFO DAGScheduler: Registering RDD 12 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:48 INFO DAGScheduler: Got job 2 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98) with 2 output partitions (allowLocal=false)
17/12/12 21:07:48 INFO DAGScheduler: Final stage: Stage 6(collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98)
17/12/12 21:07:48 INFO DAGScheduler: Parents of final stage: List(Stage 5)
17/12/12 21:07:48 INFO DAGScheduler: Missing parents: List(Stage 5)
17/12/12 21:07:48 INFO DAGScheduler: Submitting Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97), which has no missing parents
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(7008) called with curMem=10604040, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_4 stored as values in memory (estimated size 6.8 KB, free 255.0 MB)
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(5345) called with curMem=10611048, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_4_piece0 stored as bytes in memory (estimated size 5.2 KB, free 255.0 MB)
17/12/12 21:07:48 INFO BlockManagerInfo: Added broadcast_4_piece0 in memory on localhost:36715 (size: 5.2 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 21:07:48 INFO SparkContext: Created broadcast 4 from broadcast at DAGScheduler.scala:839
17/12/12 21:07:48 INFO DAGScheduler: Submitting 2 missing tasks from Stage 5 (PairwiseRDD[12] at sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Adding task set 5.0 with 2 tasks
17/12/12 21:07:48 INFO TaskSetManager: Starting task 0.0 in stage 5.0 (TID 6, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 21:07:48 INFO TaskSetManager: Starting task 1.0 in stage 5.0 (TID 7, localhost, PROCESS_LOCAL, 1125 bytes)
17/12/12 21:07:48 INFO Executor: Running task 0.0 in stage 5.0 (TID 6)
17/12/12 21:07:48 INFO Executor: Running task 1.0 in stage 5.0 (TID 7)
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 21:07:48 INFO PythonRDD: Times: total = 45, boot = -40, init = 81, finish = 4
17/12/12 21:07:48 INFO PythonRDD: Times: total = 45, boot = -40, init = 81, finish = 4
17/12/12 21:07:48 INFO Executor: Finished task 0.0 in stage 5.0 (TID 6). 1160 bytes result sent to driver
17/12/12 21:07:48 INFO Executor: Finished task 1.0 in stage 5.0 (TID 7). 1160 bytes result sent to driver
17/12/12 21:07:48 INFO TaskSetManager: Finished task 0.0 in stage 5.0 (TID 6) in 51 ms on localhost (1/2)
17/12/12 21:07:48 INFO TaskSetManager: Finished task 1.0 in stage 5.0 (TID 7) in 51 ms on localhost (2/2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Removed TaskSet 5.0, whose tasks have all completed, from pool 
17/12/12 21:07:48 INFO DAGScheduler: Stage 5 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) finished in 0.052 s
17/12/12 21:07:48 INFO DAGScheduler: looking for newly runnable stages
17/12/12 21:07:48 INFO DAGScheduler: running: Set()
17/12/12 21:07:48 INFO DAGScheduler: waiting: Set(Stage 6)
17/12/12 21:07:48 INFO DAGScheduler: failed: Set()
17/12/12 21:07:48 INFO DAGScheduler: Missing parents for Stage 6: List()
17/12/12 21:07:48 INFO DAGScheduler: Submitting Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98), which is now runnable
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(4816) called with curMem=10616393, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_5 stored as values in memory (estimated size 4.7 KB, free 255.0 MB)
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(3507) called with curMem=10621209, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_5_piece0 stored as bytes in memory (estimated size 3.4 KB, free 255.0 MB)
17/12/12 21:07:48 INFO BlockManagerInfo: Added broadcast_5_piece0 in memory on localhost:36715 (size: 3.4 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 21:07:48 INFO SparkContext: Created broadcast 5 from broadcast at DAGScheduler.scala:839
17/12/12 21:07:48 INFO DAGScheduler: Submitting 2 missing tasks from Stage 6 (PythonRDD[15] at collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Adding task set 6.0 with 2 tasks
17/12/12 21:07:48 INFO TaskSetManager: Starting task 0.0 in stage 6.0 (TID 8, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO TaskSetManager: Starting task 1.0 in stage 6.0 (TID 9, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO Executor: Running task 1.0 in stage 6.0 (TID 9)
17/12/12 21:07:48 INFO Executor: Running task 0.0 in stage 6.0 (TID 8)
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 1 ms
17/12/12 21:07:48 INFO PythonRDD: Times: total = 43, boot = -64, init = 104, finish = 3
17/12/12 21:07:48 INFO PythonRDD: Times: total = 43, boot = -64, init = 104, finish = 3
17/12/12 21:07:48 INFO Executor: Finished task 1.0 in stage 6.0 (TID 9). 12890 bytes result sent to driver
17/12/12 21:07:48 INFO Executor: Finished task 0.0 in stage 6.0 (TID 8). 15736 bytes result sent to driver
17/12/12 21:07:48 INFO TaskSetManager: Finished task 1.0 in stage 6.0 (TID 9) in 47 ms on localhost (1/2)
17/12/12 21:07:48 INFO TaskSetManager: Finished task 0.0 in stage 6.0 (TID 8) in 48 ms on localhost (2/2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Removed TaskSet 6.0, whose tasks have all completed, from pool 
17/12/12 21:07:48 INFO DAGScheduler: Stage 6 (collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98) finished in 0.048 s
17/12/12 21:07:48 INFO DAGScheduler: Job 2 finished: collect at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:98, took 0.111849 s
17/12/12 21:07:48 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 21:07:48 INFO SparkContext: Starting job: saveAsTextFile at NativeMethodAccessorImpl.java:-2
17/12/12 21:07:48 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 0 is 154 bytes
17/12/12 21:07:48 INFO MapOutputTrackerMaster: Size of output statuses for shuffle 1 is 154 bytes
17/12/12 21:07:48 INFO DAGScheduler: Got job 3 (saveAsTextFile at NativeMethodAccessorImpl.java:-2) with 2 output partitions (allowLocal=false)
17/12/12 21:07:48 INFO DAGScheduler: Final stage: Stage 9(saveAsTextFile at NativeMethodAccessorImpl.java:-2)
17/12/12 21:07:48 INFO DAGScheduler: Parents of final stage: List(Stage 8)
17/12/12 21:07:48 INFO DAGScheduler: Missing parents: List()
17/12/12 21:07:48 INFO DAGScheduler: Submitting Stage 9 (MapPartitionsRDD[18] at saveAsTextFile at NativeMethodAccessorImpl.java:-2), which has no missing parents
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(154752) called with curMem=10624716, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_6 stored as values in memory (estimated size 151.1 KB, free 254.9 MB)
17/12/12 21:07:48 INFO MemoryStore: ensureFreeSpace(99253) called with curMem=10779468, maxMem=278019440
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_6_piece0 stored as bytes in memory (estimated size 96.9 KB, free 254.8 MB)
17/12/12 21:07:48 INFO BlockManagerInfo: Added broadcast_6_piece0 in memory on localhost:36715 (size: 96.9 KB, free: 255.2 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_6_piece0
17/12/12 21:07:48 INFO SparkContext: Created broadcast 6 from broadcast at DAGScheduler.scala:839
17/12/12 21:07:48 INFO DAGScheduler: Submitting 2 missing tasks from Stage 9 (MapPartitionsRDD[18] at saveAsTextFile at NativeMethodAccessorImpl.java:-2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Adding task set 9.0 with 2 tasks
17/12/12 21:07:48 INFO TaskSetManager: Starting task 0.0 in stage 9.0 (TID 10, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO TaskSetManager: Starting task 1.0 in stage 9.0 (TID 11, localhost, PROCESS_LOCAL, 1136 bytes)
17/12/12 21:07:48 INFO Executor: Running task 0.0 in stage 9.0 (TID 10)
17/12/12 21:07:48 INFO Executor: Running task 1.0 in stage 9.0 (TID 11)
17/12/12 21:07:48 INFO BlockManager: Removing broadcast 5
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_5_piece0
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_5_piece0 of size 3507 dropped from memory (free 267144226)
17/12/12 21:07:48 INFO BlockManagerInfo: Removed broadcast_5_piece0 on localhost:36715 in memory (size: 3.4 KB, free: 255.2 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_5_piece0
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_5
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_5 of size 4816 dropped from memory (free 267149042)
17/12/12 21:07:48 INFO ContextCleaner: Cleaned broadcast 5
17/12/12 21:07:48 INFO BlockManager: Removing broadcast 4
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_4_piece0
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_4_piece0 of size 5345 dropped from memory (free 267154387)
17/12/12 21:07:48 INFO BlockManagerInfo: Removed broadcast_4_piece0 on localhost:36715 in memory (size: 5.2 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_4_piece0
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_4
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_4 of size 7008 dropped from memory (free 267161395)
17/12/12 21:07:48 INFO ContextCleaner: Cleaned broadcast 4
17/12/12 21:07:48 INFO BlockManager: Removing broadcast 3
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_3_piece0
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_3_piece0 of size 4575 dropped from memory (free 267165970)
17/12/12 21:07:48 INFO BlockManagerInfo: Removed broadcast_3_piece0 on localhost:36715 in memory (size: 4.5 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_3_piece0
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_3
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_3 of size 6080 dropped from memory (free 267172050)
17/12/12 21:07:48 INFO ContextCleaner: Cleaned broadcast 3
17/12/12 21:07:48 INFO BlockManager: Removing broadcast 2
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_2_piece0
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_2_piece0 of size 4484 dropped from memory (free 267176534)
17/12/12 21:07:48 INFO BlockManagerInfo: Removed broadcast_2_piece0 on localhost:36715 in memory (size: 4.4 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_2_piece0
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_2
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_2 of size 6064 dropped from memory (free 267182598)
17/12/12 21:07:48 INFO ContextCleaner: Cleaned broadcast 2
17/12/12 21:07:48 INFO BlockManager: Removing broadcast 1
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_1_piece0
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_1_piece0 of size 7476 dropped from memory (free 267190074)
17/12/12 21:07:48 INFO BlockManagerInfo: Removed broadcast_1_piece0 on localhost:36715 in memory (size: 7.3 KB, free: 255.3 MB)
17/12/12 21:07:48 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 21:07:48 INFO BlockManager: Removing block broadcast_1
17/12/12 21:07:48 INFO MemoryStore: Block broadcast_1 of size 9576 dropped from memory (free 267199650)
17/12/12 21:07:48 INFO ContextCleaner: Cleaned broadcast 1
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Getting 2 non-empty blocks out of 2 blocks
17/12/12 21:07:48 INFO ShuffleBlockFetcherIterator: Started 0 remote fetches in 0 ms
17/12/12 21:07:48 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 21:07:48 INFO FileOutputCommitter: File Output Committer Algorithm version is 1
17/12/12 21:07:48 INFO PythonRDD: Times: total = 46, boot = -253, init = 294, finish = 5
17/12/12 21:07:48 INFO PythonRDD: Times: total = 48, boot = -255, init = 296, finish = 7
17/12/12 21:07:48 INFO FileOutputCommitter: Saved output of task 'attempt_201712122107_0009_m_000001_11' to hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/radque_raster_1513134468.48.txt/_temporary/0/task_201712122107_0009_m_000001
17/12/12 21:07:48 INFO SparkHadoopMapRedUtil: attempt_201712122107_0009_m_000001_11: Committed
17/12/12 21:07:48 INFO FileOutputCommitter: Saved output of task 'attempt_201712122107_0009_m_000000_10' to hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/radque_raster_1513134468.48.txt/_temporary/0/task_201712122107_0009_m_000000
17/12/12 21:07:48 INFO SparkHadoopMapRedUtil: attempt_201712122107_0009_m_000000_10: Committed
17/12/12 21:07:48 INFO Executor: Finished task 0.0 in stage 9.0 (TID 10). 1890 bytes result sent to driver
17/12/12 21:07:48 INFO Executor: Finished task 1.0 in stage 9.0 (TID 11). 1890 bytes result sent to driver
17/12/12 21:07:48 INFO TaskSetManager: Finished task 0.0 in stage 9.0 (TID 10) in 272 ms on localhost (1/2)
17/12/12 21:07:48 INFO TaskSetManager: Finished task 1.0 in stage 9.0 (TID 11) in 272 ms on localhost (2/2)
17/12/12 21:07:48 INFO TaskSchedulerImpl: Removed TaskSet 9.0, whose tasks have all completed, from pool 
17/12/12 21:07:48 INFO DAGScheduler: Stage 9 (saveAsTextFile at NativeMethodAccessorImpl.java:-2) finished in 0.274 s
17/12/12 21:07:48 INFO DAGScheduler: Job 3 finished: saveAsTextFile at NativeMethodAccessorImpl.java:-2, took 0.343893 s
[Done]!!!!!
[karoth4@cg-hm08 problem4]$ ls
311_data.csv  myGrid.asc  result.txt  spark_taxiQuery.py
[karoth4@cg-hm08 problem4]$ rm result.txt 
[karoth4@cg-hm08 problem4]$ hdfs dfs -ls final/problem4/
Found 4 items
-rw-r--r--   3 karoth4 hdfs   17238601 2017-12-12 20:48 final/problem4/311_data.csv
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 20:59 final/problem4/radque_raster_1513133979.93.txt
drwxr-xr-x   - karoth4 hdfs          0 2017-12-12 21:07 final/problem4/radque_raster_1513134468.48.txt
-rw-r--r--   3 karoth4 hdfs       2656 2017-12-12 20:48 final/problem4/spark_taxiQuery.py
[karoth4@cg-hm08 problem4]$ hdfs dfs -getmerge final/problem4/radque_raster_1513134468.48.txt ~/final/problem4/result.txt
[karoth4@cg-hm08 problem4]$ vim result.txt 
[karoth4@cg-hm08 problem4]$ vim spark_taxiQuery.py 
[karoth4@cg-hm08 problem4]$ spark-submit --num-executors 18 --executor-cores 2 --executor-memory 4g spark_taxiQuery.py 2013-01-01 2013-12-01 41.64 42.03 -87.91 -87.52 0.005
17/12/12 21:11:23 INFO SparkContext: Running Spark version 1.3.1
17/12/12 21:11:23 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
17/12/12 21:11:23 INFO SecurityManager: Changing view acls to: karoth4
17/12/12 21:11:23 INFO SecurityManager: Changing modify acls to: karoth4
17/12/12 21:11:23 INFO SecurityManager: SecurityManager: authentication disabled; ui acls disabled; users with view permissions: Set(karoth4); users with modify permissions: Set(karoth4)
17/12/12 21:11:23 INFO Slf4jLogger: Slf4jLogger started
17/12/12 21:11:23 INFO Remoting: Starting remoting
17/12/12 21:11:24 INFO Remoting: Remoting started; listening on addresses :[akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:46795]
17/12/12 21:11:24 INFO Utils: Successfully started service 'sparkDriver' on port 46795.
17/12/12 21:11:24 INFO SparkEnv: Registering MapOutputTracker
17/12/12 21:11:24 INFO SparkEnv: Registering BlockManagerMaster
17/12/12 21:11:24 INFO DiskBlockManager: Created local directory at /tmp/spark-4b6c34cb-16c4-4d05-bffa-7de28e422c2d/blockmgr-8e4b3390-0e7b-4ddc-bc73-636cded3fa75
17/12/12 21:11:24 INFO MemoryStore: MemoryStore started with capacity 265.1 MB
17/12/12 21:11:24 INFO HttpFileServer: HTTP File server directory is /tmp/spark-8d9528a2-677d-443b-b2bc-6fc72134107c/httpd-4f1083af-af78-4bc0-8ba6-b746fe4a8817
17/12/12 21:11:24 INFO HttpServer: Starting HTTP Server
17/12/12 21:11:24 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 21:11:24 INFO AbstractConnector: Started SocketConnector@0.0.0.0:45427
17/12/12 21:11:24 INFO Utils: Successfully started service 'HTTP file server' on port 45427.
17/12/12 21:11:24 INFO SparkEnv: Registering OutputCommitCoordinator
17/12/12 21:11:24 INFO Server: jetty-8.y.z-SNAPSHOT
17/12/12 21:11:24 INFO AbstractConnector: Started SelectChannelConnector@0.0.0.0:4040
17/12/12 21:11:24 INFO Utils: Successfully started service 'SparkUI' on port 4040.
17/12/12 21:11:24 INFO SparkUI: Started SparkUI at http://cg-hm08.ncsa.illinois.edu:4040
17/12/12 21:11:24 INFO Utils: Copying /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py to /tmp/spark-e30f6c1b-c750-446e-aa79-1380372628f5/userFiles-1809e1bd-4997-4e27-b108-d02bd4de0ba7/spark_taxiQuery.py
17/12/12 21:11:24 INFO SparkContext: Added file file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py at file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513134684281
17/12/12 21:11:24 INFO Executor: Starting executor ID <driver> on host localhost
17/12/12 21:11:24 INFO AkkaUtils: Connecting to HeartbeatReceiver: akka.tcp://sparkDriver@cg-hm08.ncsa.illinois.edu:46795/user/HeartbeatReceiver
17/12/12 21:11:24 INFO NettyBlockTransferService: Server created on 40813
17/12/12 21:11:24 INFO BlockManagerMaster: Trying to register BlockManager
17/12/12 21:11:24 INFO BlockManagerMasterActor: Registering block manager localhost:40813 with 265.1 MB RAM, BlockManagerId(<driver>, localhost, 40813)
17/12/12 21:11:24 INFO BlockManagerMaster: Registered BlockManager
17/12/12 21:11:24 INFO MemoryStore: ensureFreeSpace(314268) called with curMem=0, maxMem=278019440
17/12/12 21:11:24 INFO MemoryStore: Block broadcast_0 stored as values in memory (estimated size 306.9 KB, free 264.8 MB)
17/12/12 21:11:24 INFO MemoryStore: ensureFreeSpace(46158) called with curMem=314268, maxMem=278019440
17/12/12 21:11:24 INFO MemoryStore: Block broadcast_0_piece0 stored as bytes in memory (estimated size 45.1 KB, free 264.8 MB)
17/12/12 21:11:24 INFO BlockManagerInfo: Added broadcast_0_piece0 in memory on localhost:40813 (size: 45.1 KB, free: 265.1 MB)
17/12/12 21:11:24 INFO BlockManagerMaster: Updated info of block broadcast_0_piece0
17/12/12 21:11:24 INFO SparkContext: Created broadcast 0 from textFile at NativeMethodAccessorImpl.java:-2
17/12/12 21:11:25 WARN DomainSocketFactory: The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
17/12/12 21:11:38 INFO FileInputFormat: Total input paths to process : 1
17/12/12 21:11:38 INFO SparkContext: Starting job: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97
17/12/12 21:11:38 INFO DAGScheduler: Registering RDD 5 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:11:38 INFO DAGScheduler: Got job 0 (sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) with 2 output partitions (allowLocal=false)
17/12/12 21:11:38 INFO DAGScheduler: Final stage: Stage 1(sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:11:38 INFO DAGScheduler: Parents of final stage: List(Stage 0)
17/12/12 21:11:38 INFO DAGScheduler: Missing parents: List(Stage 0)
17/12/12 21:11:38 INFO DAGScheduler: Submitting Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97), which has no missing parents
17/12/12 21:11:38 INFO MemoryStore: ensureFreeSpace(9576) called with curMem=360426, maxMem=278019440
17/12/12 21:11:38 INFO MemoryStore: Block broadcast_1 stored as values in memory (estimated size 9.4 KB, free 264.8 MB)
17/12/12 21:11:38 INFO MemoryStore: ensureFreeSpace(7474) called with curMem=370002, maxMem=278019440
17/12/12 21:11:38 INFO MemoryStore: Block broadcast_1_piece0 stored as bytes in memory (estimated size 7.3 KB, free 264.8 MB)
17/12/12 21:11:38 INFO BlockManagerInfo: Added broadcast_1_piece0 in memory on localhost:40813 (size: 7.3 KB, free: 265.1 MB)
17/12/12 21:11:38 INFO BlockManagerMaster: Updated info of block broadcast_1_piece0
17/12/12 21:11:38 INFO SparkContext: Created broadcast 1 from broadcast at DAGScheduler.scala:839
17/12/12 21:11:38 INFO DAGScheduler: Submitting 2 missing tasks from Stage 0 (PairwiseRDD[5] at reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97)
17/12/12 21:11:38 INFO TaskSchedulerImpl: Adding task set 0.0 with 2 tasks
17/12/12 21:11:38 INFO TaskSetManager: Starting task 0.0 in stage 0.0 (TID 0, localhost, ANY, 1406 bytes)
17/12/12 21:11:38 INFO TaskSetManager: Starting task 1.0 in stage 0.0 (TID 1, localhost, ANY, 1406 bytes)
17/12/12 21:11:38 INFO Executor: Running task 1.0 in stage 0.0 (TID 1)
17/12/12 21:11:38 INFO Executor: Running task 0.0 in stage 0.0 (TID 0)
17/12/12 21:11:38 INFO Executor: Fetching file:/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py with timestamp 1513134684281
17/12/12 21:11:38 INFO Utils: /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py has been previously copied to /tmp/spark-e30f6c1b-c750-446e-aa79-1380372628f5/userFiles-1809e1bd-4997-4e27-b108-d02bd4de0ba7/spark_taxiQuery.py
17/12/12 21:11:39 INFO CacheManager: Partition rdd_2_1 not found, computing it
17/12/12 21:11:39 INFO CacheManager: Partition rdd_2_0 not found, computing it
17/12/12 21:11:39 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:0+8619300
17/12/12 21:11:39 INFO HadoopRDD: Input split: hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv:8619300+8619301
17/12/12 21:11:39 INFO deprecation: mapred.tip.id is deprecated. Instead, use mapreduce.task.id
17/12/12 21:11:39 INFO deprecation: mapred.task.id is deprecated. Instead, use mapreduce.task.attempt.id
17/12/12 21:11:39 INFO deprecation: mapred.task.is.map is deprecated. Instead, use mapreduce.task.ismap
17/12/12 21:11:39 INFO deprecation: mapred.task.partition is deprecated. Instead, use mapreduce.task.partition
17/12/12 21:11:39 INFO deprecation: mapred.job.id is deprecated. Instead, use mapreduce.job.id
17/12/12 21:11:40 INFO PythonRDD: Times: total = 984, boot = 5, init = 398, finish = 581
17/12/12 21:11:40 INFO PythonRDD: Times: total = 1012, boot = 3, init = 400, finish = 609
17/12/12 21:11:40 INFO MemoryStore: ensureFreeSpace(5090891) called with curMem=377476, maxMem=278019440
17/12/12 21:11:40 INFO MemoryStore: Block rdd_2_0 stored as bytes in memory (estimated size 4.9 MB, free 259.9 MB)
17/12/12 21:11:40 INFO BlockManagerInfo: Added rdd_2_0 in memory on localhost:40813 (size: 4.9 MB, free: 260.2 MB)
17/12/12 21:11:40 INFO BlockManagerMaster: Updated info of block rdd_2_0
17/12/12 21:11:40 ERROR Executor: Exception in task 0.0 in stage 0.0 (TID 0)
org.apache.spark.api.python.PythonException: Traceback (most recent call last):
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 101, in main
    process()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 96, in process
    serializer.dump_stream(func(split_index, iterator), outfile)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 282, in func
    return f(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1705, in combineLocally
    merger.mergeValues(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/shuffle.py", line 252, in mergeValues
    for k, v in iterator:
TypeError: 'int' object is not iterable

	at org.apache.spark.api.python.PythonRDD$$anon$1.read(PythonRDD.scala:135)
	at org.apache.spark.api.python.PythonRDD$$anon$1.<init>(PythonRDD.scala:176)
	at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:94)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.api.python.PairwiseRDD.compute(PythonRDD.scala:311)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:68)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:41)
	at org.apache.spark.scheduler.Task.run(Task.scala:64)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:203)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
17/12/12 21:11:40 INFO MemoryStore: ensureFreeSpace(5114468) called with curMem=5468367, maxMem=278019440
17/12/12 21:11:40 INFO MemoryStore: Block rdd_2_1 stored as bytes in memory (estimated size 4.9 MB, free 255.0 MB)
17/12/12 21:11:40 INFO BlockManagerInfo: Added rdd_2_1 in memory on localhost:40813 (size: 4.9 MB, free: 255.4 MB)
17/12/12 21:11:40 INFO BlockManagerMaster: Updated info of block rdd_2_1
17/12/12 21:11:40 ERROR Executor: Exception in task 1.0 in stage 0.0 (TID 1)
org.apache.spark.api.python.PythonException: Traceback (most recent call last):
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 101, in main
    process()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 96, in process
    serializer.dump_stream(func(split_index, iterator), outfile)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 282, in func
    return f(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1705, in combineLocally
    merger.mergeValues(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/shuffle.py", line 252, in mergeValues
    for k, v in iterator:
TypeError: 'int' object is not iterable

	at org.apache.spark.api.python.PythonRDD$$anon$1.read(PythonRDD.scala:135)
	at org.apache.spark.api.python.PythonRDD$$anon$1.<init>(PythonRDD.scala:176)
	at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:94)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.api.python.PairwiseRDD.compute(PythonRDD.scala:311)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:68)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:41)
	at org.apache.spark.scheduler.Task.run(Task.scala:64)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:203)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)
17/12/12 21:11:40 WARN TaskSetManager: Lost task 0.0 in stage 0.0 (TID 0, localhost): org.apache.spark.api.python.PythonException: Traceback (most recent call last):
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 101, in main
    process()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 96, in process
    serializer.dump_stream(func(split_index, iterator), outfile)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 282, in func
    return f(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1705, in combineLocally
    merger.mergeValues(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/shuffle.py", line 252, in mergeValues
    for k, v in iterator:
TypeError: 'int' object is not iterable

	at org.apache.spark.api.python.PythonRDD$$anon$1.read(PythonRDD.scala:135)
	at org.apache.spark.api.python.PythonRDD$$anon$1.<init>(PythonRDD.scala:176)
	at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:94)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.api.python.PairwiseRDD.compute(PythonRDD.scala:311)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:68)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:41)
	at org.apache.spark.scheduler.Task.run(Task.scala:64)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:203)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

17/12/12 21:11:40 ERROR TaskSetManager: Task 0 in stage 0.0 failed 1 times; aborting job
17/12/12 21:11:40 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
17/12/12 21:11:40 INFO TaskSetManager: Lost task 1.0 in stage 0.0 (TID 1) on executor localhost: org.apache.spark.api.python.PythonException (Traceback (most recent call last):
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 101, in main
    process()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 96, in process
    serializer.dump_stream(func(split_index, iterator), outfile)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 282, in func
    return f(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1705, in combineLocally
    merger.mergeValues(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/shuffle.py", line 252, in mergeValues
    for k, v in iterator:
TypeError: 'int' object is not iterable
) [duplicate 1]
17/12/12 21:11:40 INFO TaskSchedulerImpl: Removed TaskSet 0.0, whose tasks have all completed, from pool 
17/12/12 21:11:40 INFO TaskSchedulerImpl: Cancelling stage 0
17/12/12 21:11:40 INFO DAGScheduler: Stage 0 (reduceByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97) failed in 2.202 s
17/12/12 21:11:40 INFO DAGScheduler: Job 0 failed: sortByKey at /gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py:97, took 2.256423 s
Traceback (most recent call last):
  File "/gpfs/smallblockFS/home/karoth4/final/problem4/spark_taxiQuery.py", line 97, in <module>
    result = dataset.flatMap(makeIndex).reduceByKey(lambda a,b: a+b).sortByKey()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 586, in sortByKey
    rddSize = self.count()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 932, in count
    return self.mapPartitions(lambda i: [sum(1 for _ in i)]).sum()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 923, in sum
    return self.mapPartitions(lambda x: [sum(x)]).reduce(operator.add)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 739, in reduce
    vals = self.mapPartitions(func).collect()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 713, in collect
    port = self.ctx._jvm.PythonRDD.collectAndServe(self._jrdd.rdd())
  File "/usr/hdp/2.3.2.0-2602/spark/python/lib/py4j-0.8.2.1-src.zip/py4j/java_gateway.py", line 538, in __call__
  File "/usr/hdp/2.3.2.0-2602/spark/python/lib/py4j-0.8.2.1-src.zip/py4j/protocol.py", line 300, in get_return_value
py4j.protocol.Py4JJavaError: An error occurred while calling z:org.apache.spark.api.python.PythonRDD.collectAndServe.
: org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 0.0 failed 1 times, most recent failure: Lost task 0.0 in stage 0.0 (TID 0, localhost): org.apache.spark.api.python.PythonException: Traceback (most recent call last):
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 101, in main
    process()
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/worker.py", line 96, in process
    serializer.dump_stream(func(split_index, iterator), outfile)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 2252, in pipeline_func
    return func(split, prev_func(split, iterator))
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 282, in func
    return f(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/rdd.py", line 1705, in combineLocally
    merger.mergeValues(iterator)
  File "/usr/hdp/2.3.2.0-2602/spark/python/pyspark/shuffle.py", line 252, in mergeValues
    for k, v in iterator:
TypeError: 'int' object is not iterable

	at org.apache.spark.api.python.PythonRDD$$anon$1.read(PythonRDD.scala:135)
	at org.apache.spark.api.python.PythonRDD$$anon$1.<init>(PythonRDD.scala:176)
	at org.apache.spark.api.python.PythonRDD.compute(PythonRDD.scala:94)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.api.python.PairwiseRDD.compute(PythonRDD.scala:311)
	at org.apache.spark.rdd.RDD.computeOrReadCheckpoint(RDD.scala:277)
	at org.apache.spark.rdd.RDD.iterator(RDD.scala:244)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:68)
	at org.apache.spark.scheduler.ShuffleMapTask.runTask(ShuffleMapTask.scala:41)
	at org.apache.spark.scheduler.Task.run(Task.scala:64)
	at org.apache.spark.executor.Executor$TaskRunner.run(Executor.scala:203)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
	at java.lang.Thread.run(Thread.java:745)

Driver stacktrace:
	at org.apache.spark.scheduler.DAGScheduler.org$apache$spark$scheduler$DAGScheduler$$failJobAndIndependentStages(DAGScheduler.scala:1204)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1193)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$abortStage$1.apply(DAGScheduler.scala:1192)
	at scala.collection.mutable.ResizableArray$class.foreach(ResizableArray.scala:59)
	at scala.collection.mutable.ArrayBuffer.foreach(ArrayBuffer.scala:47)
	at org.apache.spark.scheduler.DAGScheduler.abortStage(DAGScheduler.scala:1192)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:693)
	at org.apache.spark.scheduler.DAGScheduler$$anonfun$handleTaskSetFailed$1.apply(DAGScheduler.scala:693)
	at scala.Option.foreach(Option.scala:236)
	at org.apache.spark.scheduler.DAGScheduler.handleTaskSetFailed(DAGScheduler.scala:693)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1393)
	at org.apache.spark.scheduler.DAGSchedulerEventProcessLoop.onReceive(DAGScheduler.scala:1354)
	at org.apache.spark.util.EventLoop$$anon$1.run(EventLoop.scala:48)

[karoth4@cg-hm08 problem4]$ vim spark_taxiQuery.py 
[karoth4@cg-hm08 problem4]$ vim result.txt 
[karoth4@cg-hm08 problem4]$ packet_write_wait: Connection to 141.142.169.31 port 22: Broken pipe
wirelessprv-10-195-24-138:~ karoth$ ssh karoth4@roger-login.ncsa.illinois.edu
ROGER is in production

karoth4@roger-login.ncsa.illinois.edu's password: 
Last login: Tue Dec 12 19:24:38 2017 from 10.195.24.138
Welcome to ROGER! Please report problems to help+ROGER@ncsa.illinois.edu

ROGER User Guide: 
https://wiki.ncsa.illinois.edu/display/ROGER/ROGER+User+Guide

ROGER Batch system constraints (for job submission):
   32 nodes  (max job size 26 nodes)
   640 cpus  (max cpus 520)

ROGER Queue Summary:
batch: 48 hr limit: all job types 
devel: 10 Mins default, 1 hr  limit: interactive jobs only (M-F 0800-1700)

For more information about ROGER's queues check the ROGER User Guide 
**********************************************************************

=-=-=-=-=-=-=-=-=-=-=-= ANNOUNCEMENT =-=-=-=-=-=-=-=-=-=-=-=

It is with regret that NCSA announces that ROGER will be shut down
on December 16, 2017. All users must move their data and work to
another system or have a plan approved by NCSA for moving the data
off of ROGER before that date; any data not moved by that date will
be lost.
 
The ROGER system reached the end of its original grant at the end
of September 2017, and funds to continue to run ROGER are exhausted.
As a service to the community, NCSA has continued to fund and operate
ROGER. Unfortunately, there is no funding to continue to operate ROGER
after the current software licenses expire on December 16, 2017, and
no agreement has been reached on a plan to continue to operate ROGER. 

To assist the users of ROGER, NCSA is making available time on the
campus cluster for 6 months (January 1, 2018 through June 30, 2018)
for all authorized ROGER users. Further information on this resource
will be sent in a separate email. In addition, users may apply for
time on Blue Waters through the Illinois allocation process
(announcement expected early in 2018) and for time through XSEDE at
https://portal.xsede.org/allocations/announcements.

William Gropp
Director and Chief Scientist, NCSA
Thomas M. Siebel Chair in Computer Science
University of Illinois Urbana-Champaign

=-=-=-=-=-=-=-=-=-=-=-= ANNOUNCEMENT =-=-=-=-=-=-=-=-=-=-=-=

Please report any issues to help+ROGER@ncsa.illinois.edu.

[karoth4@cg-gpu01 ~]$ ls
counts.txt  heatmap_output  lab11  pig_1511542287047.log  pig_1513128184776.log  result_keywords.txt  tmp
data        kmeans_output   lab12  pig_1511543999795.log  pig_1513128194867.log  result.txt           ~tmp1
final       lab10           lab2   pig_1513128166298.log  pig_1513128538573.log  taxi.png
[karoth4@cg-gpu01 ~]$ cd final/
[karoth4@cg-gpu01 final]$ ls
problem2  problem3  problem4
[karoth4@cg-gpu01 final]$ cd problem3
[karoth4@cg-gpu01 problem3]$ vim
[karoth4@cg-gpu01 problem3]$ ls
average.py  heatmap.pig  heatmap.txt  ny_taxi_1.csv
[karoth4@cg-gpu01 problem3]$ vim average.py
[karoth4@cg-gpu01 problem3]$ vim heatmap.pig 
[karoth4@cg-gpu01 problem3]$ cd ../
[karoth4@cg-gpu01 final]$ cd problem4
[karoth4@cg-gpu01 problem4]$ ls
311_data.csv  myGrid.asc  result.txt  spark_taxiQuery.py
[karoth4@cg-gpu01 problem4]$ vim myGrid.asc 
[karoth4@cg-gpu01 problem4]$ vim result.txt 
[karoth4@cg-gpu01 problem4]$ vim myGrid.asc 
[karoth4@cg-gpu01 problem4]$ vim spark_taxiQuery.py 

import sys
import time
from pyspark import SparkContext
import math
import numpy as np

def makeIndex(record):
    '''filter and indexing target point records'''
    # Invalid Record Filter
    point_data = record.strip().split(",")
    if len(point_data) < 3:
        return []

    # Time Filter
    if point_data[1] == "":
        return []

    # Lat Filter
    if point_data[3] == "":
        return []

    lat = float(point_data[3])

    if lat < start_lat or lat > end_lat:
        return []

    # Lon Filter
    if point_data[4] == "":
        return []

    lon = float(point_data[4])

    if lon < start_lon or lon > end_lon:
        return []

    # Empty Value Filter
    if point_data[2] == "":
        return []

    row_index = int((lat - start_lat) / grid_size)
    col_index = int((lon - start_lon) / grid_size)
    #row_index = ?
    #col_index = ?

    return [((row_index, col_index), 1)]

def write_to_grid(result):
    nrows = int((end_lat - start_lat) / grid_size)+1
    ncols= int((end_lon - start_lon) / grid_size)+1
    xllcorner = start_lon
    yllcorner = start_lat
    cellsize = grid_size
    NODATA_value = -9999

    #print ncols, nrows

    myArray = np.arange(ncols * nrows).reshape(nrows,ncols)

    myArray.dtype =  np.float64

    for i in range(nrows):
        for j in range(ncols):
            myArray[i,j]= NODATA_value

    #((90, 130), 1.0)
    for ele in result:
        myArray[ele[0][0], ele[0][1]] = float(ele[1])

    header = "ncols     %s\n" % myArray.shape[1]
    header += "nrows    %s\n" % myArray.shape[0]
    header += "xllcorner %s\n" % xllcorner
    header += "yllcorner %s\n" % yllcorner
    header += "cellsize %s\n" % cellsize
    header += "NODATA_value -9999\n"

    f = open("myGrid.asc", "w")
    f.write(header)
    np.savetxt(f, myArray, fmt="%1.2f")
    f.close()



if __name__ == "__main__":
    sc = SparkContext(appName="ComplaintDesityMap")
    dataset = sc.textFile('hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/311_data.csv').filter(lambda x: True).cache()
    paras = sys.argv[-7:]

    start_time = paras[0]
    end_time = paras[1]
    start_lat = float(paras[2])
    end_lat = float(paras[3])
    start_lon = float(paras[4])
    end_lon = float(paras[5])
    grid_size = float(paras[6])

    #result = dataset.flatMap(??).reduceByKey(lambda a,b: (a[0]+b[0],a[1]+b[1])).map(lambda (key,value):(key,value[0]/(value[1]*1.0))).sortByKey()
    result = dataset.flatMap(makeIndex).reduceByKey(lambda a,b: a+b).sortByKey()
    ww = result.collect()
    ##print max([l[0][0] for l in ww]), max([k[0][1] for k in ww])
    write_to_grid(ww)

    result.saveAsTextFile('hdfs://cg-hm08.ncsa.illinois.edu/user/karoth4/final/problem4/radque_raster_%s.txt' %str(time.time()))
    print '[Done]!!!!!'
                                                     