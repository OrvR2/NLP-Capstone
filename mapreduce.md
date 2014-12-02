# Steps for MapReduce on Hadoop cluster
### Assuming all data is on the cluster

The following command will perform a MapReduce job on the Hadoop cluster. The following must be observed:
* the hadoop-streaming .jar file must be executable
* mapper.py is the mapper file
* reducer.py is the reducer file
* Both files are on the Hadoop file system
* outputDirectory is the folder that will contain all output
* nltk.mod is the file that can be downloaded from the GitHub
* input1.txt is a file passed to our mapper
* nltk_data.zip is a required file

```
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.2.0-mr1-cdh5.0.0-beta-1.jar -mapper mapper.py -reducer reducer.py -input input_files/ -output outputDirectory -file mapper.py -file reducer.py -file nltk.mod input1.txt -cacheArchive U3/nltk_data.zip#nltkData -cacheArchive U3/input_files.zip#input_files
```