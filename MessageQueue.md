## RabbitMQ

[When to use RabbitMQ or Apache Kafka](https://www.cloudamqp.com/blog/when-to-use-rabbitmq-or-apache-kafka.html)

## Kafka

女朋友看了也懂的Kafka[（上篇）](https://www.cnblogs.com/liangzilx/p/14855278.html)[（下篇）](https://www.cnblogs.com/liangzilx/p/14868874.html)

[Java工程师的进阶之路 Kafka篇（一）](https://juejin.cn/post/6953903023454158879)

[一文快速了解Kafka](https://jishuin.proginn.com/p/763bfbd57884)

[Kafka基本架构和概述](https://donggeitnote.com/2021/11/09/kafka-architecture/)
>多个consumer还可以组成一个consumer group，他们可以共同订阅一个topics的消息，但是一个partition只能被consumer group中的一个consumer来进行处理，当这个consumer group中的某个consumer出现了问题之后，可以让consumer group中别的consumer来继续处理出问题的consumer所对应的partition

[Visualizing Kafka](https://timothystepro.medium.com/visualizing-kafka-20bc384803e7)

[Kafka 会不会丢消息？ ](https://juejin.cn/post/6975066050287288327)

[Three simple ideas to make your life easier with Kafka](https://www.galiglobal.com/blog/2021/20210430-Three-Kafka-good-practices.html)

[重磅开源 KSQL：用于 Apache Kafka 的流数据 SQL 引擎](https://www.infoq.cn/article/2017/08/ksql-open-source-apache-kafka)

## Pulsa

[Apache BookKeeper 简介](https://segmentfault.com/a/1190000023086314)

[Apache Pulsar简介](https://www.cnblogs.com/hzmark/p/pulsar.html)

[我为什么放弃Kafka，选择Pulsar？](https://www.modb.pro/db/44555)

[Apache Kafka and KSQL in Action : Let’s Build a Streaming Data Pipeline!](https://talks.rmoff.net/pZC6Za/apache-kafka-and-ksql-in-action-lets-build-a-streaming-data-pipeline)

[比拼 Kafka, 大数据分析新秀Pulsar到底好在哪-InfoQ](https://mp.weixin.qq.com/s?__biz=MzUyMDA4OTY3MQ==&mid=2247496190&idx=1&sn=5171d7c9620c66ad2406e20cb74a6392&chksm=f9ed08d6ce9a81c02632fd812aa4ff2396d2e9e7efe2d89f0f0623f1ad62f60aeface0f5b12b#rd)
>Apache Pulsar 还提供了一组兼容 Kafka 的 API，用户可以通过简单地更新依赖关系并将客户端指向 Pulsar 集群来迁移现有的 Kafka 应用程序，这样现有的 Kafka 应用程序可以立即与 Apache Pulsar 一起使用，无需更改任何代码。

[重新思考流计算时代的分布式存储](http://storage.it168.com/a2018/1224/5134/000005134474.shtml)

## Books

[Kafka权威指南](https://book.douban.com/subject/27665114/)
- 使用推送和拉取模型解耦生产者和消费者；
- 为消息传递系统中的消息提供数据持久化，以便支持多个消费者；
- 通过系统优化实现高吞吐量；
- 系统可以随着数据流的增长进行横向扩展。
