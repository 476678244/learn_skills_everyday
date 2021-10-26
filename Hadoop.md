[大数据技术栈](https://github.com/heibaiying/BigData-Notes/blob/master/notes/%E5%A4%A7%E6%95%B0%E6%8D%AE%E6%8A%80%E6%9C%AF%E6%A0%88%E6%80%9D%E7%BB%B4%E5%AF%BC%E5%9B%BE.md)

## 入门

[Difference between HUE, YARN and OOZIE](https://stackoverflow.com/questions/34934606/what-is-the-difference-between-hue-yarn-and-oozie)

[Hadoop分布式文件系统——HDFS](https://github.com/heibaiying/BigData-Notes/blob/master/notes/Hadoop-HDFS.md)

[Hive介绍](https://www.cnblogs.com/sharpxiajun/archive/2013/06/02/3114180.html)
>hive不支持对某个具体行的操作，hive对数据的操作只支持覆盖原数据和追加数据。Hive也不支持事务和索引。更新、事务和索引都是关系数据库的特征，这些hive都不支持，也不打算支持，原因是hive的设计是海量数据进行处理，全数据的扫描时常态，针对某些具体数据进行操作的效率是很差的，对于更新操作，hive是通过查询将原表的数据进行转化最后存储在新表里，这和传统数据库的更新操作有很大不同。
