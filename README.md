# MovieRecommend  
一个电影推荐系统，毕业设计   

## 写在前面的话    
  距我的毕业设计完成其实已经过去半年时间了，所以很多实现细节我也记不清楚了。    
  鉴于有同学在issues向我提问，而且提的是很细节的问题，对此我不予回复与解答，望理解。    
  还有就是希望大家不要copy到本地修改后直接当做自己的毕业设计，    
  因为中间有很多地方你不去学一下是调不通程序的。我完成毕业设计的时间线可以参考文末的“笔记”。    

  下面贴出我在做这个电影推荐系统过程中收藏的部分资料链接，希望对大家有帮助。    
  [Window 下 MySQL 5.6.15 下载安装及使用](https://blog.csdn.net/wtfmonking/article/details/17467399)    
  [Python3 MySQL 数据库连接](http://www.runoob.com/python3/python3-mysql.html)    
  [协同过滤算法](https://blog.csdn.net/acdreamers/article/details/44672305)    
  [django](https://www.cnblogs.com/fengbo1113/p/8547302.html)    
  [Django用户登录与注册](https://blog.csdn.net/xiaoxujohna/article/details/51210186)  

## 系统实现工具
  1.pycharm    
  2.python3.6+django1.11    
  3.mysql    
  4.jquery+css+html5    

## 如何使用    
  首先将项目克隆到本地，用pycharm打开，将用到的csv文件导入mysql数据表中，配置好数据库；    
  注意数据库相关代码可能都要进行修改以符合实际情况；    
  代码完成后要进行migration，最后python manage.py runserver就能在浏览器中打开

## 系统流程    
  用户登录系统，对电影进行评分，查看自己已评价电影，查看推荐结果(两种)    

## 论文    
  本科毕业论文已上传，关于推荐系统的介绍、展示都在论文中，有需要者可阅读

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
    输入'http://127.0.0.1:8000/users/login/'，  返回用户登录界面       
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
      
    昨天通过python下载图片时用的电影名字命名，这样过一会就异常了，原因同上，title里面含‘？’或者‘/’都会出错，所以今天改用imdbId.jpg来存图片。    


    4/14    
    今天做的很少，主要都去看深度学习视频了，为以后的研究生项目扫盲。    
    主要还是csv和Mysql的问题，不知道要怎么去遍历里面的数据。之前是自己模拟的几个用户对电影进行评分，用的是列表类型，我就想能不能读取csv然后转为列表再操作。    


    4/20    
    由于之前创建表时，不小心将rating设为了int型，所以今天重新建了一张表改为DECIMAL，名为resultTable。而且增加了主键:id。    
    ‘alter table resultTable add column id int auto_increment PRIMARY KEY;’是给表增加一列并设为自增主键。    
    现在前端页面已经可以获取图片的imdbId号和评分，接下来就是获取当前用户的名字，给他分一个从669开始的userId号。然后插入imdbId号和rating，调用算法进行分析。    


    4/25    
    今天实现了可以从前端页面获取评分的电影的rating和imdbId号并存入users_resulttable中，还要解决的是给登录用户自动分配一个userId号，与他的评分相对应。    
    之后要实现算法从数据库中获取数据得出推荐结果。现在没有存title，后面得出推荐结果了就通过查询imdbId号得到海报和title。    
    还实现了index.html显示用户登录信息。    
    重新根据model生产数据表要将所有的迁移文件都删除才能生成成功。    

    4/26    
    实现了给每个用户分配一个id，其实是在原有的user.id基础上加1000.    
    然后将算法导入pycharm，并且实现了可以将mysql数据表导出为csv文件。    
    现在的Mysql表是user_resulttable，同csv文件，csv文件导出到static下。明天的任务是通过按钮将其连贯起来。    

    4/27    
    poster2从moviegenre7.txt导入。    
    对users_resulttable的处理：    
    alter table users_resulttable drop column id;    
    load data local infile "e:/Moviedatabase/rrtotaltable.csv" into table users_resulttable fields terminated by ','    
    lines terminated by '\n'    
    (userId,imdbId,rating);    
    alter table users_resulttable add column id int auto_increment PRIMARY KEY;     
    费劲周折终于实现了从数据库里获取海报链接并且显示在Html上。    
    但是，还没有实现从recommend函数得到的imdbId中查询到poster再显示。可能要将imdbId存到数组里再循环查询。    
    而且还有个问题，就是现在页面一刷新数据库里就会出现重复的值。    

    4/28    
    有个最大的问题，现在imdbId和poster对应的表不完整，很多推荐出来的ImdbId号找不到电影海报。    
    必须要解决这个问题，而且最好增加title。现已解决select查询语句遍历recommend函数输出的数组。    

    4/29    
    到今天为止，毕设基本已经完成。且增加了用户注销按钮。    
    但有几点不足：    
    1.推荐页面的排版样式未设计  2.运行速度有点慢  3.只用了一种推荐算法   4.每次刷新都在重新生成推荐列表，应该去除这种效果，刷新不应该变动。    

    4/30    
    提高了一点运行速度。    
    
    5/2    
    今天写完了ItemCF,但其实性能比UserCF差。因为电影数据集的电影数量比用户多太多。    

    5/7    
    今天登入数据库出现了问题，一直登不进去。后面重新建了数据库，重设置了密码。    
    数据库名改为'haha'，端口号为3307，要删除迁移文件重新执行迁移。    
     CREATE TABLE moviegenre3(imdbId INT NOT NULL PRIMARY KEY,title varchar(300),poster varchar(600));    
     然后通过navicat将moviegenre3.csv自动导入。
