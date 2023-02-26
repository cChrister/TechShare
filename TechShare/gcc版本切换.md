# Brief
有些时候编译软件，对gcc版本有要求。

如何在不改变系统gcc版本的情况下，不同用户使用不同的gcc版本？

# Theory
gcc实际上是一个可执行程序，我们之所以能在各个地方使用它，是因为其位于`/usr/bin`。
而`PATH`中默认会包含`/usr/bin`。

但是实际上gcc也只是个软连接：
```
$ ll /usr/bin/gcc
lrwxrwxrwx 1 root root 5 3月  20  2020 /usr/bin/gcc -> gcc-9*

$ ls /usr/bin/gcc*
/usr/bin/gcc    /usr/bin/gcc-9   /usr/bin/gcc-ar-8  /usr/bin/gcc-nm    /usr/bin/gcc-nm-9    /usr/bin/gcc-ranlib-8
/usr/bin/gcc-8  /usr/bin/gcc-ar  /usr/bin/gcc-ar-9  /usr/bin/gcc-nm-8  /usr/bin/gcc-ranlib  /usr/bin/gcc-ranlib-9
```



# Practice
```
$ gcc --version
gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
Copyright (C) 2019 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```
可以看到Ubuntu20.04系统默认的gcc版本是9.4.0

如果我们需要使用gcc-8的版本，我们可以确认下系统有没有安装：
```
$ ls /usr/bin/gcc*
/usr/bin/gcc    /usr/bin/gcc-9   /usr/bin/gcc-ar-8  /usr/bin/gcc-nm    /usr/bin/gcc-nm-9    /usr/bin/gcc-ranlib-8
/usr/bin/gcc-8  /usr/bin/gcc-ar  /usr/bin/gcc-ar-9  /usr/bin/gcc-nm-8  /usr/bin/gcc-ranlib  /usr/bin/gcc-ranlib-9
```
可以发现系统已经安装了gcc-8

我们只需要在`~/.bashrc`里面加入
```
alias gcc="/usr/bin/gcc-8"
```
然后更新一下`source ~/.bashrc`

```
$ gcc --version

gcc (Ubuntu 8.4.0-3ubuntu2) 8.4.0
Copyright (C) 2018 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
```

如果你要的gcc版本没有安装，那么你只需要把gcc放到自己的主目录下，更换对应的路径即可。
`àlias gcc="/home/***/gcc"`
