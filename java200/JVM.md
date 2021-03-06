> ## JVM

> **`194.说一下 jvm 的主要组成部分？及其作用？`**

1. 类加载器（Class Loader）：加载类文件到内存。Class loader只管加载，只要符合文件结构就加载，至于能否运行，它不负责，那是有Exectution Engine 负责的。
2. 执行引擎（Execution Engine）：也叫解释器，负责解释命令，交由操作系统执行。
3. 本地库接口（Native Interface）：本地接口的作用是融合不同的语言为java所用
4. 运行时数据区（Runtime Data Area）：堆栈方法区那些

作用 ：首先通过编译器把 Java 代码转换成字节码，类加载器（ClassLoader）再把字节码加载到内存中，将其放在运行时数据区（Runtime data area）的方法区内，而字节码文件只是 JVM 的一套指令集规范，并不能直接交给底层操作系统去执行，因此需要特定的命令解析器执行引擎（Execution Engine），将字节码翻译成底层系统指令，再交由 CPU 去执行，而这个过程中需要调用其他语言的本地库接口（Native Interface）来实现整个程序的功能。

![image](https://img-blog.csdnimg.cn/20200103213149526.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly90aGlua3dvbi5ibG9nLmNzZG4ubmV0,size_16,color_FFFFFF,t_70)

> **`195.说一下 jvm 运行时数据区？`**

1. 堆。堆是java对象的存储区域，任何用new字段分配的java对象实例和数组，都被分配在堆上，java堆可用-Xms和-Xmx进行内存控制，jdk1.7以后，运行时常量池从方法区移到了堆上。
2. 方法区：用于存储已被虚拟机加载的类信息，常量，静态变量，即时编译器编译后的代码等数据。`误区：方法区不等于永生`。很多人原因把方法区称作“永久代”（Permanent Generation），本质上两者并不等价，只是HotSpot虚拟机垃圾回收器团队把GC分代收集扩展到了方法区，或者说是用来永久代来实现方法区而已，这样能省去专门为方法区编写内存管理的代码，但是在Jdk8也移除了“永久代”，使用Native Memory来实现方法区。
3. 虚拟机栈：虚拟机栈中执行每个方法的时候，都会创建一个栈桢用于存储局部变量表，操作数栈，动态链接，方法出口等信息。
4. 本地方法栈：与虚拟机栈发挥的作用相似，相比于虚拟机栈为Java方法服务，本地方法栈为虚拟机使用的Native方法服务，执行每个本地方法的时候，都会创建一个栈帧用于存储局部变量表，操作数栈，动态链接，方法出口等信息。
5. 程序计数器。指示Java虚拟机下一条需要执行的字节码指令。

![image](https://img-blog.csdnimg.cn/20200103213220764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly90aGlua3dvbi5ibG9nLmNzZG4ubmV0,size_16,color_FFFFFF,t_70)

> **`196.说一下堆栈的区别？`**

1. 栈内存:栈内存首先是一片内存区域，存储的都是`局部变量`，凡是定义在方法中的都是局部变量（方法外的是全局变量），for循环内部定义的也是局部变量，是先加载函数才能进行局部变量的定义，所以方法先进栈，然后再定义变量，变量有自己的作用域，`一旦离开作用域，变量就会被释放`。栈内存的更新速度很快，因为局部变量的生命周期都很短。

2. 堆内存:存储的是`数组和对象`（其实数组就是对象），凡是new建立的都是在堆中，堆中存放的都是实体（对象），实体用于封装数据，而且是封装多个（实体的多个属性），如果一个数据消失，这个实体也没有消失，还可以用，所以堆是不会随时释放的，但是栈不一样，栈里存放的都是单个变量，变量被释放了，那就没有了。堆里的实体虽然不会被释放，但是会被当成垃圾，Java有垃圾回收机制不定时的收取。

> **`197.队列和栈是什么？有什么区别？`**

队列和栈都是被用来预存数据的。
1. 操作的名称不同。队列的插入称为入队，队列的删除称为出队。栈的插入称为进栈，栈的删除称为出栈。
2. 可操作的方式不同。队列是在队尾入队，队头出队，即两边都可操作。而栈的进栈和出栈都是在栈顶进行的，无法对栈底直接进行操作。
3. 操作的方法不同。队列是先进先出（FIFO），即队列的修改是依先进先出的原则进行的。新来的成员总是加入队尾（不能从中间插入），每次离开的成员总是队列头上（不允许中途离队）。而栈为后进先出（LIFO）,即每次删除（出栈）的总是当前栈中最新的元素，即最后插入（进栈）的元素，而最先插入的被放在栈的底部，要到最后才能删除。队列允许先进先出检查元素，但也有例外情况。Deque接口允许从两端检索元素。

> **`198.什么是双亲委派模型？`**

当需要加载一个类的时候，子类加载器并不会马上去加载，而是依次去请求父类加载器加载，一直往上请求到最高类加载器：启动类加载器。当启动类加载器加载不了的时候，依次往下让子类加载器进行加载。当达到最底下的时候，如果还是加载不到该类，就会出现ClassNotFound的情况。

好处：保证了程序的安全性。例子：比如我们重新写了一个String类，加载的时候并不会去加载到我们自己写的String类，因为当请求上到最高层的时候，启动类加载器发现自己能够加载String类，因此就不会加载到我们自己写的String类了。

![image](https://img-blog.csdnimg.cn/20200104165551656.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly90aGlua3dvbi5ibG9nLmNzZG4ubmV0,size_16,color_FFFFFF,t_70)

> **`199.说一下类加载的执行过程？`**

举个通俗点的例子来说，JVM在执行某段代码时，遇到了class A， 然而此时内存中并没有class A的相关信息，于是JVM就会到相应的class文件中去寻找class A的类信息，并加载进内存中，这就是我们所说的类加载过程。

由此可见，JVM不是一开始就把所有的类都加载进内存中，而是只有第一次遇到某个需要运行的类时才会加载，且只加载一次。

类加载
类加载的过程主要分为三个部分：加载\链接\初始化
而链接又可以细分为三个小部分：验证\准备\解析

https://blog.csdn.net/ln152315/article/details/79223441


> **`207.说一下 jvm 调优的工具？`**

jvm监控分析工具一般分为两类，一种是jdk自带的工具，一种是第三方的分析工具。jdk自带工具一般在jdk bin目录下面，以exe的形式直接点击就可以使用，其中包含分析工具已经很强大，几乎涉及了方方面面，但是我们最常使用的只有两款：jconsole.exe和jvisualvm.exe；第三方的分析工具有很多，各自的侧重点不同，比较有代表性的：MAT(Memory Analyzer Tool)、GChisto等。


> **`208.常用的 jvm 调优的参数都有哪些？`**
```
-Xms2g：初始化推大小为 2g；
-Xmx2g：堆最大内存为 2g；
-XX:NewRatio=4：设置年轻的和老年代的内存比例为 1:4；
-XX:SurvivorRatio=8：设置新生代 Eden 和 Survivor 比例为 8:2；
–XX:+UseParNewGC：指定使用 ParNew + Serial Old 垃圾回收器组合；
-XX:+UseParallelOldGC：指定使用 ParNew + ParNew Old 垃圾回收器组合；
-XX:+UseConcMarkSweepGC：指定使用 CMS + Serial Old 垃圾回收器组合；
-XX:+PrintGC：开启打印 gc 信息；
-XX:+PrintGCDetails：打印 gc 详细信息。
```

> **`深拷贝和浅拷贝`**

- 浅拷贝（shallowCopy）只是增加了一个指针指向已存在的内存地址，
- 深拷贝（deepCopy）是增加了一个指针并且申请了一个新的内存，使这个增加的指针指向这个新的内存，

> **`对象的创建`**

说到对象的创建，首先让我们看看 Java 中提供的几种对象创建方式：
|Header|解释|
|---|---|
|使用new关键字	|调用了构造函数|
|使用Class的newInstance方法	|调用了构造函数|
|使用Constructor类的newInstance方法|	调用了构造函数|
|使用clone方法	|没有调用构造函数|
|使用反序列化|	没有调用构造函数|

虚拟机遇到一条new指令时，先检查常量池是否已经加载相应的类，如果没有，必须先执行相应的类加载。类加载通过后，接下来分配内存。若Java堆中内存是绝对规整的，使用“指针碰撞“方式分配内存；如果不是规整的，就从空闲列表中分配，叫做”空闲列表“方式。划分内存时还需要考虑一个问题-并发，也有两种方式: CAS同步处理，或者本地线程分配缓冲(Thread Local Allocation Buffer, TLAB)。然后内存空间初始化操作，接着是做一些必要的对象设置(元信息、哈希码…)，最后执行<init>方法。


> **`为对象分配内存`**

类加载完成后，接着会在Java堆中划分一块内存分配给对象。内存分配根据Java堆是否规整，有两种方式：
- `指针碰撞`：如果Java堆的内存是规整，即所有用过的内存放在一边，而空闲的的放在另一边。分配内存时将位于中间的指针指示器向空闲的内存移动一段与对象大小相等的距离，这样便完成分配内存工作。
- `空闲列表`：如果Java堆的内存不是规整的，则需要由虚拟机维护一个列表来记录那些内存是可用的，这样在分配的时候可以从列表中查询到足够大的内存分配给对象，并在分配后更新列表记录。
选择哪种分配方式是由 Java 堆是否规整来决定的，而 Java 堆是否规整又由所采用的垃圾收集器是否带有压缩整理功能决定。

![image](https://img-blog.csdnimg.cn/20200103213812259.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly90aGlua3dvbi5ibG9nLmNzZG4ubmV0,size_16,color_FFFFFF,t_70)

> **`处理并发安全问题`**

对象的创建在虚拟机中是一个非常频繁的行为，哪怕只是修改一个指针所指向的位置，在并发情况下也是不安全的，可能出现正在给对象 A 分配内存，指针还没来得及修改，对象 B 又同时使用了原来的指针来分配内存的情况。解决这个问题有两种方案：

1. 对分配内存空间的动作进行同步处理（采用 CAS + 失败重试来保障更新操作的原子性）；
2. 把内存分配的动作按照线程划分在不同的空间之中进行，即每个线程在 Java 堆中预先分配一小块内存，称为本地线程分配缓冲（Thread Local Allocation Buffer, TLAB）。哪个线程要分配内存，就在哪个线程的 TLAB 上分配。只有 TLAB 用完并分配新的 TLAB 时，才需要同步锁。通过-XX:+/-UserTLAB参数来设定虚拟机是否使用TLAB。

![image](https://img-blog.csdnimg.cn/20200103213833317.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly90aGlua3dvbi5ibG9nLmNzZG4ubmV0,size_16,color_FFFFFF,t_70)

> **`对象的访问定位`**

Java程序需要通过 JVM 栈上的引用访问堆中的具体对象。对象的访问方式取决于 JVM 虚拟机的实现。目前主流的访问方式有 句柄 和 直接指针 两种方式。
- `指针`： 指向对象，代表一个对象在内存中的起始地址。
- `句柄`： 可以理解为指向指针的指针，维护着对象的指针。句柄不直接指向对象，而是指向对象的指针（句柄不发生变化，指向固定内存地址），再由对象的指针指向对象的真实内存地址。
