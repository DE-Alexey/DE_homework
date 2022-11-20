[cloudera@quickstart ~]$ hdfs dfs -copyFrromLocal /home/cloudera/Desktop/vim1.txt /user/cloudera
-copyFrromLocal: Unknown command
[cloudera@quickstart ~]$ hdfs dfs -copyFromLocal /home/cloudera/Desktop/vim1.txt /user/cloudera
[cloudera@quickstart ~]$ hdfs dfs -chmod 764 vim1.txt
[cloudera@quickstart ~]$ hdfs dfs -copyFromLocal /home/cloudera/Desktop/vim2.txt /user/cloudera
[cloudera@quickstart ~]$ hdfs dfs -copyFromLocal /home/cloudera/Desktop/vim3.txt /user/cloudera
[cloudera@quickstart ~]$ hdfs dfs -copyFromLocal /home/cloudera/Desktop/vim4.txt /user/cloudera
[cloudera@quickstart ~]$ hdfs dfs -chmod 764 vim2.txt
[cloudera@quickstart ~]$ hdfs dfs -chmod 764 vim3.txt
[cloudera@quickstart ~]$ hdfs dfs -chmod 764 vim4.txt
[cloudera@quickstart ~]$ hdfs dfs -du -h  vim1.txt
719.3 K  719.3 K  vim1.txt
[cloudera@quickstart ~]$ hdfs dfs -ls
Found 4 items
-rwxrw-r--   1 cloudera cloudera     736519 2022-11-20 08:29 vim1.txt
-rwxrw-r--   1 cloudera cloudera     770324 2022-11-20 11:40 vim2.txt
-rwxrw-r--   1 cloudera cloudera     843205 2022-11-20 11:40 vim3.txt
-rwxrw-r--   1 cloudera cloudera     697960 2022-11-20 11:40 vim4.txt
[cloudera@quickstart ~]$ hdfs dfs -setrep 2 /
[cloudera@quickstart ~]$ hdfs dfs -cat vim1.txt | wc -l 
3392