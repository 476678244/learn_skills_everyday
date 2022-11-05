## Encription

[非对称加密概述](https://blog.csdn.net/u011583927/article/details/81272265)
>使用其中一个密钥把明文加密后所得的密文，只能用相对应的另一个密钥才能解密得到原本的明文，甚至连最初用来加密的密钥也不能用作解密，这是非对称加密最重要的性质或者说特点。

[非对称加密形象解释](https://www.cnblogs.com/mujian/p/7665952.html)
>Bob先发给保险柜（Bob公钥）给Alice，接着Alice把自己的保险柜（Alice公钥）放到Bob的保险柜(即使用Bob的公钥加密Alice的公钥)里边发还给Bob，接着Bob拿到Alice的数据包后，用自己的私钥解开了外层保险柜(Bob的公钥)，拿到了里边Alice保险柜(Alice的公钥)。此时Alice跟Bob都有了各自的公钥(并且都有他们自己的私钥)，接着只要保证每次互相传递数据的时候，把数据放在对方的保险柜里边即可(即每次都用对方的公钥加密数据)，这样无论如何，H都无法解开保险柜（因为只有各自的私钥才能解开各自的保险柜）

[数学小魔术](https://www.zhihu.com/question/33645891/answer/192604856)
>任何人都可以按照我公布的方法加密一个数，但是只有我才知道怎么把所得的密文变回去。

[Digital Signature](http://www.youdzone.com/signature.html)
>Although these steps may sound complicated, they are all handled behind the scenes by Pat's user-friendly software. To verify a signature, Pat need only click on it.

# Security
[Securing your digital life](https://arstechnica.com/information-technology/2021/10/securing-your-digital-life-part-2/)
>Everything counts in multiple accounts

[HTTPS 是如何保护你的安全的](https://sspai.com/post/68040)
>对于支持 HTTPS 的网站，大部分都对 HTTP 进行了跳转。举例来说，当你访问少数派网站时，如果直接在浏览器中输入 sspai.com 就敲下回车键，那么浏览器会自动跳转到 http://sspai.com 而不是 HTTPS 站点。而少数派网站在收到 HTTP 请求后，会告诉你：我改地址了，请使用 HTTPS 访问。

[用户认证问题](https://qiankunli.github.io/2016/08/25/security.html)

[基于token的多平台身份认证架构设计](https://www.cnblogs.com/beer/p/6029861.html)

## Block Chain

[区块链入门](http://www.ruanyifeng.com/blog/2017/12/blockchain-tutorial.html)
>区块链的主要作用是储存信息。任何需要保存的信息，都可以写入区块链，也可以从里面读取，所以它是数据库。

[走进Web3](https://www.bmpi.dev/dev/glimpse-of-web3/)
>在Web3呼吸都要钱

## BTC

[比特币入门](https://www.ruanyifeng.com/blog/2018/01/bitcoin-tutorial.html)
>所有的交易数据都会传送到矿工那里。矿工负责把这些交易写入区块链。
