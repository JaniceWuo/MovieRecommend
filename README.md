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




![image](https://github.com/JaniceWuo/MovieRecommend/blob/master/djangostuding/images/databaseMigration.jpg)
