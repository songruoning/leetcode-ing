# 数据倾斜的解决方法

数据倾斜有三种形式得倾斜：
- 一是分区不均，某几个分区对应的key太多。多数情况都是这种倾斜。
- 二是单个key对应的数据量太多
- 三是单条记录数据太大（比如数组中的值太多）

> ## 2.1 加并行度

这是一种很简单的处理方案，将分区增多，数据打得更散，充分发挥分布式的优势。但是分区增量task也会增多，带来的额外的管理成本就更多了，分的太多反而跑得更慢，存储结果的成本也增加了，不是一个很好的解决方案。可以在以下几个地方增加分区。1.在倾斜的stage之前使用reparation重分区。2.设置shuffle的并行度，大部分情况都使用这个。

> ## 2.2 处理特殊case

这种就比较常见了，经常会发现很多stage跑到剩下一个task死活跑不过或者耗时非常久。倾斜的key我们可以通过groupbykey进行count来寻找，一般都是空值、空字符串、还有特别热点的key。如何处理这就看你的业务需求咯。

> ## 2.3 利用小trick打散key

针对第二种倾斜的形式，我们可以在key上加随机前缀或后缀这样加盐的方式来将一个key变成多个key先进行一次shuffle，最后再还原回来。

例如我们需要进行分组统计，但是数据倾斜了，我们可以对key加随机前缀，把一个key变成多个进行count，最后sum。

这种方式比较麻烦特别是在join的情况下，要考虑的东西比较多。加盐的方式也会数据量不是那么多的key也打的更散了，计算起来有点浪费资源。

> ## 2.4 自定义分区方案

这种就更高端了些，需要自己去实现一个partitioner，不多说，还不如构造key来实现自定义分区。