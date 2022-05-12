## Scala

[写点什么-有关jvm,scala与后端架构](https://hongjiang.info/scala/)

[Add a variable to a class instance at runtime](https://rosettacode.org/wiki/Add_a_variable_to_a_class_instance_at_runtime#Python)

[泛函数据类型－Monoid](https://www.cnblogs.com/tiger-xc/p/4442953.html)

[图解 Monad](http://www.ruanyifeng.com/blog/2015/07/monad.html)
>你只要提供下一步运算所需的函数，整个运算就会自动进行下去。

[Testing with ScalaMock](https://scalamock.org/quick-start/)

[Use List instead of Stack](https://stackoverflow.com/questions/43866787/scala-2-12-tells-me-stack-is-deprecated-how-to-replace-it-exactly-and-why-i-do)
>var a = new List ; a = XXX +: a ; a = a.tail

## Async

[异步编程的几种方式 ](https://ericfu.me/several-ways-to-aync/)

[Java异步编程指南](http://javakk.com/225.html)
>在我们做rpc远程调用，redis，数据库访问等比较耗时的网络请求时经常要面对这样的问题，这种业务场景我们可以引入异步的编程思想，即主流程不需要阻塞等待接口返回数据，而是继续往下执行，当真正需要这个接口返回结果时再通过回调或阻塞的方式获取，此时我们的主流程和异步任务是并行执行的。

[一文带你彻底了解Java异步编程](http://javakk.com/563.html)
>以同步的方式编码，达到异步的效果与性能,兼顾可维护性与可伸缩性。

## Sbt plugins
[sbt-scoverage](https://github.com/scoverage/sbt-scoverage)
>[Code Coverage for Scala using scoverage and sbt](https://www.youtube.com/watch?v=oz_HcHvbp7Y)

[sbt-assembly](https://github.com/sbt/sbt-assembly)

## Java

[CAS和AQS](https://blog.csdn.net/u010862794/article/details/72892300)
>CAS(Compare And Swap)，即比较并交换。是解决多线程并行情况下使用锁造成性能损耗的一种机制，CAS操作包含三个操作数——内存位置（V）、预期原值（A）和新值(B)。如果内存位置的值与预期原值相匹配，那么处理器会自动将该位置值更新为新值。否则，处理器不做任何操作。无论哪种情况，它都会在CAS指令之前返回该位置的值。CAS有效地说明了“我认为位置V应该包含值A；如果包含该值，则将B放到这个位置；否则，不要更改该位置，只告诉我这个位置现在的值即可。

[CAS视频讲解](https://www.bilibili.com/video/BV1ff4y1q7we?spm_id_from=333.337.search-card.all.click)

<img src="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-user-assets/2018/5/3/163260cff7cb847c~tplv-t2oaga2asx-watermark.image" width="400"/>

[可重入性，公平锁与非公平锁](https://blog.csdn.net/weixin_33969116/article/details/87948635?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link)
- 公平锁每次获取到锁为同步队列中的第一个节点，保证请求资源时间上的绝对顺序，而非公平锁有可能刚释放锁的线程下次继续获取该锁，则有可能导致其他线程永远无法获取到锁，造成“饥饿”现象。
- 公平锁为了保证时间上的绝对顺序，需要频繁的上下文切换，而非公平锁会降低一定的上下文切换，降低性能开销。因此，ReentrantLock默认选择的是非公平锁，则是为了减少一部分上下文切换，保证了系统更大的吞吐量。
