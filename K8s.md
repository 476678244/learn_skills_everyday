## Docker

[Docker与k8s的恩怨情仇（一）—成为PaaS前浪的Cloud Foundry](https://www.cnblogs.com/powertoolsteam/p/14889081.html)
>Docker成功的关键，在于Docker镜像几乎完美地解决了Cloud Foundry在打包方面的软肋。

[Docker与k8s的恩怨情仇（二）—用最简单的技术实现“容器”](https://www.cnblogs.com/powertoolsteam/p/14922152.html)
>只有Linux中运行的容器是通过对进程进行限制模拟出来的结果，Windows和Mac下的容器，都是通过Docker Desktop等容器软件，操作虚拟机模拟出来的“真实”的虚拟容器。

## 入门K8s
>几年来，随着以 Docker 为代表的容器技术的出现，终结了之前 DevOps 中交付和部署环节因环境、配置及程序本身的不同而造成的动辄几种甚至几十种部署配置的困境，将它们统一在容器镜像上。但 Docker 更适用于管理单个容器，一旦开始使用越来越多的容器封装和运行应用程序，必将会导致其管理和编排变得越来越困难。最终，用户不得不对容器实施分组，以便跨所有容器提供网络、安全、监控等服务。于是，以 Kubernetes 为代表的容器编排系统应运而生。
[图解 K8s 核心概念和术语](https://xie.infoq.cn/article/09cbb998e6e24953c9542d7c3)

[Kubenetes 之新手入门篇](http://matt33.com/2020/08/02/kubernetes-start/)

[快速了解和上手容器编排工具k8s](https://www.youtube.com/watch?v=HsvAVGjlN9k&ab_channel=FreeCoder)

[Kubernetes介绍篇：是什么? 为什么要用它？](https://my.oschina.net/xcbeyond/blog/5048401)

[面向 Kubernetes 编程： Kubernetes 是下一代操作系统](https://github.com/answer1991/articles/blob/master/Kubernetes-is-the-next-generation-os.md)
>在未来不久的某一天，也许云厂商只卖 Kubernetes “虚拟机”了：阿里云不单独卖 ecs 了，亚马逊AWS，微软云，Google 云等各种云厂商都不卖 Linux 虚拟机了。如果你想买单机版的 Linux 虚拟机，他们都会一脸惊讶的问你，你买那么底层的、功能那么薄弱的计算机干什么？就像你现在从云厂商那里买不到一个还没有安装 Linux 的虚拟机一样。以后，云厂商交付的 “虚拟机” 必定是 “集群级别的虚拟机” ，而 “集群级别的虚拟机” 的操作系统就是 Kubernetes。

[带你全景俯瞰云原生与 kubernetes](https://zhuanlan.zhihu.com/p/382608092)

[Borg与K8s](https://www.cnblogs.com/linuxprobe/p/5658749.html)
>那么对于我们来说，比较详细一点，就是说在我们软件开发当中碰到的情况是这样的。从我们的软件设计到开发到测试、生产都经过非常多，非常反复的过程。同时在大部分的集群系统当中，我们也非常难以调度它。那么我觉得对于我们来说，就是后面要解决几个方面的问题。我觉得这是我们一个大的方向。我们以后的产品是不是可以减少语言、程序、框架不同带来的复杂性，能不能把流程进行简化，把语言进行简化，把网络和服务依赖进行简化，这是我提的另一个问题。


![](https://img-blog.csdnimg.cn/20201026154555648.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3hjYmV5b25k,size_16,color_FFFFFF,t_70#pic_center)

![Kubernetes 的发展历程如下图所示](http://matt33.com/images/k8s/k8s-history.png)

## 论文

[《Large-scale cluster management at Google with Borg》](https://dl.acm.org/doi/pdf/10.1145/2741948.2741964)

## 搭建

[本地运行 Kubernetes 的 4 种方法](https://linux.cn/article-12825-1.html)

## 理解

[Demystifying Kubernetes service discovery](https://nigelpoulton.com/demystifying-kubernetes-service-discovery/)

## Books

[Kubernetes权威指南：从Docker到Kubernetes实践全接触](https://book.douban.com/subject/35458432/)
