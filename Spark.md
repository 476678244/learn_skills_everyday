## 深入浅出 Spark
[深入浅出 Spark（一）：内存计算的由来](https://www.infoq.cn/article/oPpQzsJIFopeBpzVcbx7)

[深入浅出 Spark（二）：血统（DAG）](https://www.infoq.cn/article/LBzKJPoaFAre5c0cI4ur)

[深入浅出 Spark（三）：Spark 调度系统之“权力的游戏”](https://www.infoq.cn/article/5aOHzQIaXX6NlHriLtSI)

[深入浅出 Spark（四）：存储系统](https://www.infoq.cn/article/civuder65orp1lyods8a)

## 入门

[带你深入浅出，彻底了解什么是Spark？](https://blog.51cto.com/u_15105906/2842768)

[The Spark Starter Guide](https://hadoopsters.com/spark/)

[Spark底层原理详细解析](https://www.cnblogs.com/itlz/p/14343315.html)

[大数据组件Presto，Spark SQL，Hive相互关系](https://blog.csdn.net/yilulvxing/article/details/86220888)

[Jupyter Notebook & Spark on Kubernetes](https://towardsdatascience.com/jupyter-notebook-spark-on-kubernetes-880af7e06351)

[为什么Spark比MapReduce快？](https://www.zhihu.com/question/31930662)

[一文了解 Apache Spark 3.0 动态分区裁剪（Dynamic Partition Pruning）](https://blog.csdn.net/wypblog/article/details/102908685)

[认识 Delta Lake](https://zhuanlan.zhihu.com/p/87744720)
>Parquet文件 + Meta 文件 + 一组操作的API = Delta Lake.

## 用法

[Spark Launcher Java API 提交 Spark 算法](https://xie.infoq.cn/article/3d84053a4e17c468f0b546ef5)

[行转列、列转行、Lateral View、排序](https://www.cnblogs.com/ljhdo/p/14263019.html)

[spill to disk and shuffle write are two different things](https://stackoverflow.com/questions/41661849/spill-to-disk-and-shuffle-write-spark)

[Spark 之 故障排除（一） ](https://juejin.cn/post/6972333997774864420)

[Spark 之 故障排除（二） ](https://juejin.cn/post/6972853997812056100)

## Performance Tuning

[Spark性能优化指南——基础篇](https://tech.meituan.com/2016/04/29/spark-tuning-basic.html)

[Spark性能优化指南——高级篇](https://tech.meituan.com/2016/05/12/spark-tuning-pro.html)

[超全spark性能优化总结](https://zhuanlan.zhihu.com/p/108454557)

[Spark 3.0 中七个必须知道的 SQL 性能优化](http://www.cxyzjd.com/article/w397090770/107241259)

[Caching Vs Checkpointing](http://www.lifeisafile.com/Apache-Spark-Caching-Vs-Checkpointing/)
>checkpointing is a sort of reuse of RDD partitions when failures occur during job execution

## 理解

[Spark程序的生命周期](https://www.cnblogs.com/zzq6032010/p/15516323.html)
>客户端将程序包（jar包或代码库）提交到集群管理器的驱动节点（即master节点），此时驱动节点会给Spark驱动器进程申请资源，并将其在某一个节点服务器上启动起来。程序包也发给Spark驱动器。

[Spark源码解析](https://juejin.cn/post/6968987830991192100)

[Spark-Listener](https://blog.csdn.net/asd491310/article/details/89210932)
>Spark-Core内部的事件框架实现了基于事件的异步化编程模式。它的最大好处是可以提升应用程序对物理资源的充分利用，能最大限度的压榨物理资源，提升应用程序的处理效率。缺点比较明显，降低了应用程序的可读性。

[Broadcast](https://blog.csdn.net/rlnlo2pnefx9c/article/details/120245372)
>Spark 设计了两种 broadcast 的方式，传统存在单点瓶颈问题的 HttpBroadcast，和类似 BT 方式的 TorrentBroadcast。HttpBroadcast 使用传统的 client-server 形式的 HttpServer 来传递真正的 data，而 TorrentBroadcast 使用 blockManager 自带的 NIO 通信方式来传递 data。TorrentBroadcast 存在的问题是慢启动和占内存，慢启动指的是刚开始 data 只在 driver 上有，要等 executors fetch 很多轮 data block 后，data server 才会变得可观，后面的 fetch 速度才会变快。

[统一内存管理](https://mp.weixin.qq.com/s?__biz=MzIwNDkwMjc1OQ==&mid=2247485817&idx=1&sn=acbb75d1b97d3ea40f4804f1c7367324&chksm=97385171a04fd867fca863d8018120e872a1788a489d1b49bd9063cff700f6e229850d869ca4#rd)
>统一内存管理对比静态内存管理最重要的改进是支持执行内存和存储内存之间的动态抢占，从而提升了内存使用率；同时，内存管理器还可以统一管理堆内内存和堆外内存，当配置了spark.memory.offHeap.enabled=true和spark.memory.offHeap.size参数时则可以使用堆外内存。

[Spark内存管理机制](https://juejin.cn/post/7051037707568414727)
>Spark在2.x之后，摒弃了之前版本的Tachyon，采用Java中常见的基于JDK Unsafe API来对堆外内存进行管理。此模式不在JVM中申请内存，而是直接操作系统内存，减少了JVM中内存空间切换的开销，降低了GC回收占用的消耗，实现对内存的精确管控。

## Books
[Spark海量数据处理：技术详解与平台实战](https://weread.qq.com/web/reader/483326b071a52591483e940kc81322c012c81e728d9d180)
