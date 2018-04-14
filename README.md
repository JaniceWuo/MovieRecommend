# MovieRecommend  
一个电影推荐系统，毕业设计   

***
**笔记**  
    2018年2月18日 寒假过的好快啊，前一阵子准备用flask，但是后面进一步了解之后决定用django+mysql+python完成这个推荐系统，现在就在懵懵懂懂的学django    

    2018/4/5    
    UserCF是给用户推荐和他有共同兴趣爱好的用户喜欢的电影，ItemCF是给用户推荐那些和他之前喜欢的电影类似的电影。    
    目前已经实现UserCF部分算法，模拟了用户-电影矩阵数据，对已有用户里的某一位用户进行电影推荐。之后的工作就是要从csv中获取数据。    
    看了《推荐系统实践》这本书，后期可能用基于标签，但是基于标签算法涉及更多，每部电影都需要多个标签，不能用movielens数据集。

    2018/4/7		
    今天尝试用了pycharm，之前一直用的sublime，但是文件管理的比较混乱。用pycharm的时候遇到坑了，我系统按安装的是django1.11,
    但是pycharm里面安装的是最新版本2.0，导致项目文件自带的代码有错误。后来又卸了重新安装，统一成了1.11.0版本。    
    接下来是mysql，项目迁移如下：

![image](https://github.com/JaniceWuo/MovieRecommend/blob/master/djangostuding/images/databaseMigration.jpg)
    
   这只是生成了迁移文件，还要执行迁移文件
   ```python
       python manage.py migrate
   ```
***
   2018/4/8    
   进行一下流程梳理：   
   1.先启动mysql:net start mysql;mysql -u root -p;    
   2. create database [数据库名字];
   3.pycharm直接创建一个django项目，然后进入这个项目下，python manage.py startapp myApp  
   4.在settings.py 中：在INSTALLED_APPS后面加上'myApp'(也可以取其他名字，但是要和前面取的相同)；再配置数据库，代码为：    
   ```python
      DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[数据库名字]',
        'PASSWORD': '[自己设置一个密码]',
        'HOST': '127.0.0.1',
        'USER': 'root',
        'PORT': '',   
    }
}
   ```
   5.在_init_.py中： import pymysql;  pymysql.install_as_MySQLdb()    
   6.models.py:加入模型类，属性等。    
   7.生成迁移文件：python manage.py makemigrations;执行迁移：python manage.py migrate;   
   8.在mysql>中：use [数据库名];  show tables;    
     在项目文件下，python manage.py runserver  浏览器中输入127.0.0.1:8000    
   9.在templates下写html文件，然后和views.py视图文件、urls.py文件进行匹配    
***
   2018/4/10    
   今天搭建了django的虚拟开发环境，安装了virtualenv,下次直接输入命令行：e:\GradProject\Scripts\activate，一定要保证整个项目都在虚拟环境中运行。 django1.11.1  
   关于html文件调用js、css等文件：首先在建的app目录下建一个static文件，分支如下   
   ├─migrations    
│  └─__pycache__    
├─static    
│  ├─css    
│  ├─img    
│  └─js    
└─__pycache__        
    注意migrations和static文件同级。html文件开头要加上 {% load staticfiles %}，引入css的语句为：    
    ```python
       <link rel="stylesheet" href="{% static 'css/Test.css' %}">
    ```    
    如果纯粹像写前端那样调用css、js是不能成功的。    
    输入'http://127.0.0.1:8000/users/login/'，  返回用户登录界面：    
    ![image](https://github.com/JaniceWuo/MovieRecommend/blob/master/djangostuding/images/login.jpg)    
    点击登录后进入推荐系统首页（目前的首页只有一个电影分类页面，之后应增加分页，以及实现用户对电影评分，数据库记录用户对电影的评分）    

    2018/4/12    
    今天找到了另一个csv文件，里面含有电影海报的链接，这样可以直接用Js动态获取链接然后加载图片；    
    还有由于有很多个csv文件，每个文件包含的内容都不一样，所以要将各个文件合并。准备直接用mysql的多表查询。花了很久才成功把csv导入进mysql表中的ratings：    

```mysql
   mysql->CREATE TABLE ratings(userId INT NOT NULL,movieId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,rating DECIMAL(3,1) NOT NULL);
   mysql> load data local infile "e:/Moviedatabase/hhhh.csv" into table ratings fields terminated by ','
    -> enclosed by '"'
    -> lines terminated by '\n'
    -> (userId,movieId,rating);
```     

    2018/4/13    
    注意result表里面要存电影的名字，而名字里面很多不确定的特殊符号，比如有逗号，冒号等。所以不能加enclosed by '"'这句，否则csv导进mysql表时会中断。    
    然后创建一个总表：
    mysql->CREATE TABLE RTotalTable(movieId INT NOT NULL,userId INT NOT NULL,rating INT,imdbId INT NOT NULL,title varchar(50) NOT NULL);
    mysql->INSERT INTO RTotalTable SELECT *FROM(SELECT * from ratings natural join result) AS tb; //将ratings和result两张表连接后插入建好的RTotalTable表中。    
    得到的最终表如下图所示，可以直接从这张表中得到用户信息及对电影的评分，然后获得推荐电影的id或者名字，通过imdbId可以获取到本地的电影海报。
  
  ![image](https://github.com/JaniceWuo/MovieRecommend/blob/master/djangostuding/images/RTotalTable.JPG)    
    昨天通过python下载图片时用的电影名字命名，这样过一会就异常了，原因同上，title里面含‘？’或者‘/’都会出错，所以今天改用imdbId.jpg来存图片。    


    4/14    
    今天做的很少，主要都去看深度学习视频了，为以后的研究生项目扫盲。    
    主要还是csv和Mysql的问题，不知道要怎么去遍历里面的数据。之前是自己模拟的几个用户对电影进行评分，用的是列表类型，我就想能不能读取csv然后转为列表再操作。