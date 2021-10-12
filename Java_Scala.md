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

## Sbt plugins
[sbt-scoverage](https://github.com/scoverage/sbt-scoverage)
>[Code Coverage for Scala using scoverage and sbt](https://www.youtube.com/watch?v=oz_HcHvbp7Y)

[sbt-assembly](https://github.com/sbt/sbt-assembly)

## JVM

[CAS和AQS](https://blog.csdn.net/u010862794/article/details/72892300)
>CAS(Compare And Swap)，即比较并交换。是解决多线程并行情况下使用锁造成性能损耗的一种机制，CAS操作包含三个操作数——内存位置（V）、预期原值（A）和新值(B)。如果内存位置的值与预期原值相匹配，那么处理器会自动将该位置值更新为新值。否则，处理器不做任何操作。无论哪种情况，它都会在CAS指令之前返回该位置的值。CAS有效地说明了“我认为位置V应该包含值A；如果包含该值，则将B放到这个位置；否则，不要更改该位置，只告诉我这个位置现在的值即可。
