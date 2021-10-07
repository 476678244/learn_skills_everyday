## 缓存
[缓存穿透、缓存击穿、缓存雪崩](https://www.damon8.cn/2020/07/27/mq-01/)

## Data Warehouse
[数仓架构发展史](https://www.cnblogs.com/data-magnifier/p/14128335.html)

[深入理解大数据之——Lambda架构](https://jiang-hao.com/articles/2019/big-data-lambda-architecture.html)
>Marz在Twitter工作期间开发了著名的实时大数据处理框架Storm，Lambda架构是其根据多年进行分布式大数据系统的经验总结提炼而成。Lambda架构的目标是设计出一个能满足实时大数据系统关键特性的架构，包括有：高容错、低延时和可扩展等。Lambda架构整合离线计算和实时计算，融合不可变性（Immunability），读写分离和复杂性隔离等一系列架构原则，可集成Hadoop，Kafka，Storm，Spark，Hbase等各类大数据组件。


## 列存储 vs. 行存储

[什么是列式存储数据库？](https://blog.csdn.net/NIeson2012/article/details/79551337)
>列式的另一大优势是压缩。因为列的天然凝聚性（比如上面的两个Jones就可以压缩成一个）大大强与行，所以列式储存可以有很高的压缩比，这个进一步使使用的磁盘的数量减少，因为使用的磁盘块少，进一步减少了需要扫描的次数。这方面很利于加快查找速度，但是因为解压缩也是耗时耗内存的过程，所以压缩的控制也是需要一个定平衡点。

[列存储格式Parquet浅析](https://www.jianshu.com/p/47b39ae336d5)

## Database

[数据库基础](DB_fundamental.md)

[MongoDB](MongoDB.md)

