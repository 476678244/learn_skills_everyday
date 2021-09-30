[零基础SQL教程](https://www.liaoxuefeng.com/wiki/1177760294764384)
>数据库索引对于用户和应用程序来说都是透明的。

[MySQL数据库的主键和外键详解](https://zhuanlan.zhihu.com/p/114834741)
>删除表时，应该先删子表，后删父表，除非使用casecade constraints 解除关联。

[超键、候选键](https://blog.csdn.net/jerry11112/article/details/78160771)
>就是用户从很多候选键选出来的一个键就是主键

[mysql为什么建议使用自增主键](https://zhuanlan.zhihu.com/p/71022670)
>所谓的索引其实就是一颗 B+ 树，一个表有多少个索引就会有多少颗 B+ 树，mysql 中的数据都是按顺序保存在 B+ 树上的

[数据库的最简单实现](http://www.ruanyifeng.com/blog/2014/07/database_implementation.html)
>B树是对二叉查找树的改进。它的设计思想是，将相关数据尽量集中在一起，以便一次读取多个数据，减少硬盘操作次数。这种数据结构，非常有利于减少读取硬盘的次数。假定一个节点可以容纳100个值，那么3层的B树可以容纳100万个数据，如果换成二叉查找树，则需要20层！假定操作系统一次读取一个节点，并且根节点保留在内存中，那么B树在100万个数据中查找目标值，只需要读取两次硬盘。
