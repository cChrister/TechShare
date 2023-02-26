# Brief
服务器在/usr/local/cuda有一个主版本。

如何在保持/usr/local/cuda软链接不变动的情况下，让不同的用户使用不容的cuda版本呢？

注：查看cuda版本，不要用nvidia-smi查看，其显示的是cuda-driver-version.
我们可以用`nvcc --version`来查看cuda的版本，其显示才是cuda-runtime-version.

# Theory
服务器默认将cuda的环境变量加入到了系统的`PATH`里面，
```bash
$ cat /etc/bash.bashrc
...
export PATH=/usr/local/cuda/bin:$PATH
```
也可以通过`echo $PATH | grep cuda` 来查看

我们只需要覆盖$PATH里面的cuda路径即可。  

# Practice
```
$ nvcc --version

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Sun_Mar_21_19:15:46_PDT_2021
Cuda compilation tools, release 11.3, V11.3.58
Build cuda_11.3.r11.3/compiler.29745058_0

$ echo $PATH | grep cuda
/opt/anaconda3/bin:/opt/anaconda3/condabin:/usr/local/Matlab/R2018a/bin:/usr/local/cuda/bin:/opt/anaconda3/bin:/opt/clion/clion-2022.2.4/bin:/opt/pycharm-community-2021.2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda/bin:/opt/pycharm-community-2020.2.3/bin:/snap/bin

$ ll /usr/local/cuda
lrwxrwxrwx 1 root root 9 1月   6 17:09 /usr/local/cuda -> cuda-11.3/
```

我们可以看到cuda的版本是11.3， `ll /usr/local/cuda`与`nvcc --version`是一致的。

**接下来我们如果要使用cuda-10.2的版本，但是又没有管理员权限该如何实现呢？**
我们首先下载cuda-10.2的安装包，注意安装的时候，不需要再重新安装驱动了。
我们把cuda的install路径放在我们的用户目录下，比如`/home/renhaofan/cuda-10.2`

之后我们在`~/.bashrc`中加入：
```
export CUDA_HOME=/usr/local/cuda-10.2
export PATH=$PATH:$CUDA_HOME/bin
export LD_LIBRARY_PATH=$CUDA_HOME/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
之后我们更新一下`source ~/.bashrc`

这时候使用`echo $PATH | grep cuda` 会发现存在两个cuda，在有些机器上，我们新加入的cuda会覆盖，但是有些时候并不可行。

于是我们需要从PATH删除原来的cuda，即在`~/.bashrc`中加入：
```
PATH=$(echo :$PATH: | sed -e 's,:/usr/local/cuda/bin:,:,g' -e 's/^://' -e 's/:$//')
export CUDA_HOME=/usr/local/cuda-10.2
export PATH=$PATH:$CUDA_HOME/bin
export LD_LIBRARY_PATH=$CUDA_HOME/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```
更新`source ~/.bashrc`之后，可以通过`nvcc --version`查看cuda的版本：

```
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```




