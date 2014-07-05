python 项目
==========

## 待完成

待完成，添加一个自动搜索选项

## 功能设想


* src/a_class.f90
* src/b_class.f90
* ...
* tests/a_class.fun
* tests/b_class.fun
* ...


### 0.

### 1. 创建
```	bash
$ funit a_class
```

生成临时文件 `tests/a_class_fun.f90`

### 2. 编译

``` bash
$ gfortran -c src/a_class.f90 -o tests/a_class.o
$ gfortran tests/a_class_fun.f90 tests/a_class.o -o tests/a.out
```

### 3. 运行

``` bash
$ cat a_class.InputFile | ./a_class.out | a_class.log
```

屏幕上显示
> time = 0.1s  
> pass function
> ...  
> pass 8/8 fail 0/8

### 4. 清理
```
$ rm a_class.o, a_class.mod, a_class_fun.f90, a_class.out
```
保留 a_class.log

### 5. 重复 1-4 步
