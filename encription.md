## Git

[使用 SSH 连接到 GitHub](https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh)

## Encription

[非对称加密形象解释](https://www.cnblogs.com/mujian/p/7665952.html)
>Bob先发给保险柜（Bob公钥）给Alice，接着Alice把自己的保险柜（Alice公钥）放到Bob的保险柜(即使用Bob的公钥加密Alice的公钥)里边发还给Bob，接着Bob拿到Alice的数据包后，用自己的私钥解开了外层保险柜(Bob的公钥)，拿到了里边Alice保险柜(Alice的公钥)。此时Alice跟Bob都有了各自的公钥(并且都有他们自己的私钥)，接着只要保证每次互相传递数据的时候，把数据放在对方的保险柜里边即可(即每次都用对方的公钥加密数据)，这样无论如何，H都无法解开保险柜（因为只有各自的私钥才能解开各自的保险柜）

[数学小魔术](https://www.zhihu.com/question/33645891/answer/192604856)
>任何人都可以按照我公布的方法加密一个数，但是只有我才知道怎么把所得的密文变回去。
