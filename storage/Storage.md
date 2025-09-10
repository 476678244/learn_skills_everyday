## 缓存
[缓存穿透、缓存击穿、缓存雪崩](https://www.damon8.cn/2020/07/27/mq-01/)

[Everything I know about good system design](https://www.seangoedecke.com/good-system-design/)

## Data Warehouse
[数仓架构发展史](https://www.cnblogs.com/data-magnifier/p/14128335.html)

[深入理解大数据之——Lambda架构](https://jiang-hao.com/articles/2019/big-data-lambda-architecture.html)
>Marz在Twitter工作期间开发了著名的实时大数据处理框架Storm，Lambda架构是其根据多年进行分布式大数据系统的经验总结提炼而成。Lambda架构的目标是设计出一个能满足实时大数据系统关键特性的架构，包括有：高容错、低延时和可扩展等。Lambda架构整合离线计算和实时计算，融合不可变性（Immunability），读写分离和复杂性隔离等一系列架构原则，可集成Hadoop，Kafka，Storm，Spark，Hbase等各类大数据组件。


## 列存储 vs. 行存储

[什么是列式存储数据库？](https://blog.csdn.net/NIeson2012/article/details/79551337)
>列式的另一大优势是压缩。因为列的天然凝聚性（比如上面的两个Jones就可以压缩成一个）大大强与行，所以列式储存可以有很高的压缩比，这个进一步使使用的磁盘的数量减少，因为使用的磁盘块少，进一步减少了需要扫描的次数。这方面很利于加快查找速度，但是因为解压缩也是耗时耗内存的过程，所以压缩的控制也是需要一个定平衡点。

[列存储格式Parquet浅析](https://www.jianshu.com/p/47b39ae336d5)

[Redshift列式存储](https://docs.amazonaws.cn/redshift/latest/dg/c_columnar_storage_disk_mem_mgmnt.html)
>实际上，通过使用具有大量列和行的表，可大幅提高效率。例如，假定一个表包含 100 个列。使用 5 个列的查询仅需读取表中 5% 的数据。对于大型数据库，可为数十亿或甚至数万亿记录实现此节省。相反，一个行式数据库将读取包含 95 个不需要的列的数据块。

## Database

[数据库基础](DB_fundamental.md)

[Apache Cassandra 简介](https://www.iteblog.com/archives/2530.html)
>在希腊神话里，Cassandra 是特洛伊国王 Priam 和 Hecuba 王后的女儿。Cassandra 非常美丽，以至于阿波罗给了她预见未来的能力。但当她拒绝阿波罗的爱慕的时候，遭到他的诅咒。从此，她依然可以精确地预知未来，但是不会有任何人相信她。Cassandra 预知了她的特洛伊城终将覆灭，但却无力阻止这一悲剧。Cassandra 分布式数据库就据此命名。

## No Sql

[MongoDB](MongoDB.md)

[图数据库以及简单入门](https://blog.csdn.net/xlgen157387/article/details/79085901)
图具有如下特征：
1. 包含节点和边；
2. 节点上有属性（键值对）；
3. 边有名字和方向，并总是有一个开始节点和一个结束节点；
4. 边也可以有属性。

## OLAP vs. OLTP

[主流OLAP系统对比总结](https://zhuanlan.zhihu.com/p/38767561)

[Kylin 在 eBay 的成长历程与实践](https://www.infoq.cn/article/56vdaS7pwu2iexe4ukv0)

[KYLIN、DRUID、CLICKHOUSE核心技术对比](http://www.jackywoo.cn/kylin-druid-clickhouse-comparing/)
