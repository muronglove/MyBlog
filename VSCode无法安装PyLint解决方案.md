VSCode无法安装PyLint解决方案
==
1.问题描述
--
使用VSCode敲完**python**之后保存，会出现安装**pylint**（一个对python进行检查的插件）的提示，但是点击安装后发现无法安装

2.问题解决
---

* 在stackoverflow上有一个类似问题的回答，原因是没有安装pip，虽然不知道pip是干什么的，但是安装pip的命令还是挺简单的，打开命令行输入`sudo easy_install pip`和相应的密码即可
* 安装完pip之后依然存在问题，这个时候直接复制粘贴编辑器提示的问题已经无法解决问题了，所以我在搜索引擎里输入了**VSCode pylint**，发现了一个关键的回答，原来安装pip是要用pip安装pylint，在命令行中输入`pip install pylint`，问题就完全解决了

&copy;*Brandon*

*2018/4/14*
