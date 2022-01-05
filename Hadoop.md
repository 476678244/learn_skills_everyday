## Overview

[大数据学习路线](https://github.com/heibaiying/BigData-Notes/blob/master/notes/%E5%A4%A7%E6%95%B0%E6%8D%AE%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF.md)
>这里说明一下，如果你的时间有限，不一定要学完 Scala 才去学习大数据框架。Scala 确实足够的精简和灵活，但其在语言复杂度上略大于 Java，例如隐式转换和隐式参数等概念在初次涉及时会比较难以理解，所以你可以在了解 Spark 后再去学习 Scala，因为类似隐式转换等概念在 Spark 源码中有大量的运用。

[Snowflake 如日中天是否代表 Hadoop 已死？大数据体系到底是什么？](https://zhuanlan.zhihu.com/p/396165293)
>随各种资源的解耦（例如，存储计算分离），调度算法可以在单一维度做更深度的优化，AI优化是关键方向（实际上，很多年前Google Borg就已经采用蒙特卡洛Simulation做新任务资源需求的预测了）

## Yarn

[Hadoop Yarn 一文搞懂 Yarn架构原理和工作机制 ](https://www.cnblogs.com/liangzilx/p/14837562.html)
>随着互联网的高速发展，基于数据密集型应用的计算框架不断出现，从支持离线处理 的 MapReduce，到支持在线处理的 Storm，从迭代式计算框架 Spark 到流式处理框架 S4，等等。各种框架有其应用的场景。而在实际互联网公司中，这几种框架不是选其一，而是根据场景有不同的选择共同构建整个计算框架。考虑成本、运维、数据共享等等因素，实际更希望的是将这些框架都部署到一个公共的集群中，共享集群资源，并对资源进行统一管理，同时采用某种资源隔离方案(如轻量级 cgroups)对各个任务进行隔离，这样便诞生了轻量级弹性计算平台。YARN 便是弹性计算平台的典型代表。

[Difference between HUE, YARN and OOZIE](https://stackoverflow.com/questions/34934606/what-is-the-difference-between-hue-yarn-and-oozie)

## HDFS

[Hadoop分布式文件系统——HDFS](https://github.com/heibaiying/BigData-Notes/blob/master/notes/Hadoop-HDFS.md)

[HDFS体系结构](https://www.cnblogs.com/liangzilx/p/14851367.html)
>没有NameNode，整个HDFS将无法使用。事实上，如果运行NameNode服务的及其损坏，文件系统上所有的文件将会丢失，因为我们不知道如何根据DataNode的块重建文件

## Hive

[Hive介绍](https://www.cnblogs.com/sharpxiajun/archive/2013/06/02/3114180.html)
>hive不支持对某个具体行的操作，hive对数据的操作只支持覆盖原数据和追加数据。Hive也不支持事务和索引。更新、事务和索引都是关系数据库的特征，这些hive都不支持，也不打算支持，原因是hive的设计是海量数据进行处理，全数据的扫描时常态，针对某些具体数据进行操作的效率是很差的，对于更新操作，hive是通过查询将原表的数据进行转化最后存储在新表里，这和传统数据库的更新操作有很大不同。
