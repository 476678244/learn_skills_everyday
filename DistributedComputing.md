## MPP

[MPP架构](https://blog.csdn.net/ioteye/article/details/113452551)

[MPP vs. sql on hadoop](https://www.zhihu.com/question/27589901)
>MPP数据库适合存储高密度价值数据，并且是长期存储和多次使用，所以MPP并行数据库会花大量经历在Load阶段，把数据处理成适合分析格式。带来的优点是查询速度快，通常在秒计甚至毫秒级以内就可以返回查询结果。

[MPP之Amazon Redshift数据库](https://www.cnblogs.com/FengGeBlog/p/9816144.html)
>Amazon Redshift基于企业级PostgreSQL数据库，有大规模并行处理（MPP）结构，MPP可以通过将数据分布到各个计算节点来解决海量数据的处理难题。在Redshift中，每个集群有一个管理节点和多个计算节点。集群内部使用私有、高速、 低延时的网络连接。每个计算节点都有单独的CPU，内存和附加存储，并且每个计算节点有多个分区，您的数据被分布保存在计算节点的多个分区内，因此每个分区的数据量大大减少，您的查询会在多个分区并行执行，大大的增加了查询的效率。

## 分布式事务

[事务及其ACID特性](https://jiang-hao.com/articles/2019/backend-transactions-acid.html)

[分布式事务，这一篇就够了](https://xiaomi-info.github.io/2020/01/02/distributed-transaction/)

[聊聊分布式事务，再说说解决方案](https://www.cnblogs.com/savorboard/p/distributed-system-transaction-consistency.html)
>我们无法做到强一致，但每个应用都可以根据自身的业务特点，采用适当的方式来使系统达到最终一致性（Eventual consistency）

## 云原生
[CNCF 全景图](https://raw.githubusercontent.com/cncf/trailmap/master/CNCF_TrailMap_latest.png)
