# 配置Android Studio && Git

- **配置Android Studio**

1. 国内镜像：https://www.jianshu.com/p/53080a8cbc95, 通常使用 mirrors.neusoft.edu.cn 端口：80
2. 仓库服务：https://maven.aliyun.com/mvn/search, 阿里云加速较快，代码如下:
   ``` 
   repositories {
   
        maven { url 'https://maven.aliyun.com/repository/google' }

        maven{ url 'https://maven.aliyun.com/repository/jcenter' }

    }
    ```
3. 遇到浏览器能下载，但是Android Studio无法下载的插件，https://zhuanlan.zhihu.com/p/364825122, 删除C:\Users\Administrator\\.gradle文件中的代理配置


- 配置Git
1. 下载windows版本的Git后安装： https://www.git-scm.com/download/win
2. 配置github，用于上传和下载代码：https://zhuanlan.zhihu.com/p/111548833


