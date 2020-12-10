#### 创建、删除文件及目录

<br>
> touch 创建指定文件

-  touch 文件名

```
# 实例：
touch 1.txt 2.txt 3.txt
```

<br>

> rm 删除文件、目录

- -i 删除前逐一询问确认（有交互）
- -f 强制移除，即使属性是只读
- -r 移除目录

```
#
rm ~/test/*.txt
rm -r ~/test
```

<br>

> mkdir 创建文件夹

- -p 确保目录名称存在，不存在就创建一个

```
# 若无-p参数，test2目录不存在，则产生错误
mkdir -p test2/test 
```