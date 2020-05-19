from django.shortcuts import render, redirect,HttpResponseRedirect
from .forms import RegisterForm
from users.models import Resulttable,Insertposter
from django.db import models

def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', context={'form': form})

def index(request):
    return render(request, 'users/..//index.html')
# 为啥？

def check(request):
    return render((request, 'users/..//index.html'))
# def showregist(request):
#     pass


def showmessage(request):
    usermovieid = []
    usermovietitle = []
    data=Resulttable.objects.filter(userId=1001)
    for row in data:
        usermovieid.append(row.imdbId)

    try:
        conn = get_conn()
        cur = conn.cursor()
        #Insertposter.objects.filter(userId=USERID).delete()
        for i in usermovieid:
            cur.execute('select * from moviegenre3 where imdbId = %s',i)
            rr = cur.fetchall()
            for imdbId,title,poster in rr:
                usermovietitle.append(title)
                print(title)

        # print(poster_result)
    finally:
        conn.close()
    return render(request, 'users/message.html', locals())


# USERID = 1002
def recommend1(request):
    USERID = int(request.GET["userIdd"]) + 1000
    Insertposter.objects.filter(userId=USERID).delete()
    #selectMysql()
    read_mysql_to_csv('users/static/users_resulttable.csv',USERID)  #追加数据，提高速率
    ratingfile = os.path.join('users/static', 'users_resulttable.csv')
    usercf = UserBasedCF()
    userid = str(USERID)#得到了当前用户的id
    print(userid)
    usercf.generate_dataset(ratingfile)
    usercf.calc_user_sim()
    usercf.recommend(userid)    #得到imdbId号

    #先删除所有数据


    try:
        conn = get_conn()
        cur = conn.cursor()
        #Insertposter.objects.filter(userId=USERID).delete()
        for i in matrix:
            cur.execute('select * from moviegenre3 where imdbId = %s',i)
            rr = cur.fetchall()
            for imdbId,title,poster in rr:
                #print(value)         #value才是真正的海报链接
                if(Insertposter.objects.filter(title=title)):
                    continue
                else:
                    Insertposter.objects.create(userId=USERID, title=title, poster=poster)

        # print(poster_result)
    finally:
        conn.close()
    #results = Insertposter.objects.all()       #从这里传递给html= Insertposter.objects.all()  # 从这里传递给html
    results = Insertposter.objects.filter(userId=USERID)
    return render(request,'users/movieRecommend.html', locals())
    # return render(request, 'users/..//index.html', locals())


def recommend2(request):
    # USERID = int(request.GET["userIddd"]) + 1000
    USERID = 1001
    Insertposter.objects.filter(userId=USERID).delete()
    #selectMysql()
    read_mysql_to_csv2('users/static/users_resulttable2.csv',USERID)  #追加数据，提高速率
    ratingfile2 = os.path.join('users/static', 'users_resulttable2.csv')
    itemcf = ItemBasedCF()
    #userid = '1001'
    userid = str(USERID)#得到了当前用户的id
    print(userid)
    itemcf.generate_dataset(ratingfile2)
    itemcf.calc_movie_sim()
    itemcf.recommend(userid)    #得到imdbId号

    #先删除所有数据


    try:
        conn = get_conn()
        cur = conn.cursor()
        #Insertposter.objects.filter(userId=USERID).delete()
        for i in matrix2:
            cur.execute('select * from moviegenre3 where imdbId = %s',i)
            rr = cur.fetchall()
            for imdbId,title,poster in rr:
                #print(value)         #value才是真正的海报链接
                if(Insertposter.objects.filter(title=title)):
                    continue
                else:
                    Insertposter.objects.create(userId=USERID, title=title, poster=poster)

        # print(poster_result)
    finally:
        conn.close()
        results = Insertposter.objects.filter(userId=USERID)       #从这里传递给html= Insertposter.objects.all()  # 从这里传递给html

    return render(request, 'users/movieRecommend2.html',locals())
    # return HttpResponseRedirect('movieRecommend.html', locals())






def insert(request):
    # MOVIEID = int(request.GET["movieId"])
    global USERID
    USERID = int(request.GET["userId"])+1000
    # USERID = {{}}
    RATING = float(request.GET["rating"])
    IMDBID = int(request.GET["imdbId"])

    Resulttable.objects.create(userId=USERID, rating=RATING,imdbId=IMDBID)
    #print(USERID)
    # return HttpResponseRedirect('/')
    return render(request, 'index.html',{'userId':USERID,'rating':RATING,'imdbId':IMDBID})



import sys
import random
import os,math
from operator import itemgetter
import pymysql
import csv
from django.http import HttpResponse
import codecs


def get_conn():
    conn = pymysql.connect(host='127.0.0.1', port=3307, user='root', passwd='admin', db='haha', charset='utf8')
    return conn

def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()

def read_mysql_to_csv(filename,user):
    with codecs.open(filename=filename, mode='w', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('select * from users_resulttable')
        #sql = ('select * from users_resulttable WHERE userId = 1001')
        rr = cur.fetchall()
        #results = query_all(cur=cur, sql=sql, args=None)
        for result in rr:
            #print(result)
            write.writerow(result[:-1])


def read_mysql_to_csv2(filename,user):
    with codecs.open(filename=filename, mode='a', encoding='utf-8') as f:
        write = csv.writer(f, dialect='excel')
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('select * from users_resulttable')
        sql = ('select * from users_resulttable WHERE userId = 1001')
        rr = cur.fetchall()
        results = query_all(cur=cur, sql=sql, args=None)
        for result in results:
            #print(result)
            write.writerow(result[:-1])





# if __name__ == '__main__':
#     # main()
#     read_mysql_to_csv('../users/static/users_resulttable.csv')
#


import sys
import random
import math
import os
from operator import itemgetter

random.seed(0)
user_sim_mat = {}
matrix = []  #全局变量
matrix2 = []

class UserBasedCF(object):
    ''' TopN recommendation - User Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}  # 训练集
        self.testset = {}  # 测试集
        self.initialset = {}  # 存储要推荐的用户的信息
        self.n_sim_user = 30
        self.n_rec_movie = 10

        self.movie_popular = {}
        self.movie_count = 0  # 总电影数量

        print('Similar user number = %d' % self.n_sim_user, file=sys.stderr)
        print('recommended movie number = %d' %
              self.n_rec_movie, file=sys.stderr)

    @staticmethod
    def loadfile(filename):
        ''' load a file, return a generator. '''
        fp = open(filename, 'r', encoding='UTF-8')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            # if i % 100000 == 0:
            #     print ('loading %s(%s)' % (filename, i), file=sys.stderr)
        fp.close()
        print('load %s success' % filename, file=sys.stderr)

    def initial_dataset(self, filename1):
        initialset_len = 0
        for lines in self.loadfile(filename1):
            users, movies, ratings = lines.split(',')
            self.initialset.setdefault(users, {})
            self.initialset[users][movies] = (ratings)
            initialset_len += 1

    def generate_dataset(self, filename2, pivot=1.0):
        ''' load rating data and split it to training set and test set '''
        trainset_len = 0
        testset_len = 0

        for line in self.loadfile(filename2):
            # user, movie, rating, _ = line.split('::')
            user, movie, rating = line.split(',')
            # split the data by pivot
            if random.random() < pivot:  # pivot=0.7应该表示训练集：测试集=7：3
                self.trainset.setdefault(user, {})
                self.trainset[user][movie] = (rating)  # trainset[user][movie]可以获取用户对电影的评分  都是整数
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})
                self.testset[user][movie] = (rating)
                testset_len += 1

        print('split training set and test set succ', file=sys.stderr)
        print('train set = %s' % trainset_len, file=sys.stderr)
        print('test set = %s' % testset_len, file=sys.stderr)

    def calc_user_sim(self):
        movie2users = dict()

        for user, movies in self.trainset.items():
            for movie in movies:
                # inverse table for item-users
                if movie not in movie2users:
                    movie2users[movie] = set()
                movie2users[movie].add(user)  # 看这个电影的用户id
                # print(movie)   #输出的是movieId
                # print(movie2users[movie])   #输出的是{'userId'...}
                # print(movie2users)    #movieId:{'userId','userId'...}

                # count item popularity at the same time
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        # print ('build movie-users inverse table succ', file=sys.stderr)

        # save the total movie number, which will be used in evaluation
        self.movie_count = len(movie2users)
        print('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated items between users  计算用户之间共同评分的物品
        usersim_mat = user_sim_mat
        # print ('building user co-rated movies matrix...', file=sys.stderr)

        for movie, users in movie2users.items():  # 通过.items()遍历movie2users这个字典里的所有键、值
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    usersim_mat.setdefault(u, {})
                    usersim_mat[u].setdefault(v, 0)
                    usersim_mat[u][v] += 1 / math.log(1 + len(users))  # usersim_mat二维矩阵应该存的是用户u和用户v之间共同评分的电影数目
        # print ('build user co-rated movies matrix succ', file=sys.stderr)

        # calculate similarity matrix
        # print ('calculating user similarity matrix...', file=sys.stderr)
        simfactor_count = 0
        PRINT_STEP = 20000

        for u, related_users in usersim_mat.items():
            for v, count in related_users.items():
                usersim_mat[u][v] = count / math.sqrt(
                    len(self.trainset[u]) * len(self.trainset[v]))
                simfactor_count += 1


    def recommend(self, user):
        ''' Find K similar users and recommend N movies. '''
        matrix.clear()   #每次都要清空
        K = self.n_sim_user  # 这里等于20
        N = self.n_rec_movie  # 这里等于10
        rank = dict()  # 用户对电影的兴趣度
        # print(self.initialset[user])
        watched_movies = self.trainset[user]  # user用户已经看过的电影  只包括训练集里的
        # 这里之后不能是训练集
        # watched_movies = self.initialset[user]
        for similar_user, similarity_factor in sorted(user_sim_mat[user].items(),
                                                      key=itemgetter(1), reverse=True)[
                                               0:K]:  # itemgetter(1)表示对第2个域(相似度)排序   reverse=TRUE表示降序
            for imdbid in self.trainset[similar_user]:  # similar_user是items里面的键，就是所有用户   similarity_factor是值，就是对应的相似度
                if imdbid in watched_movies:
                    continue  # 如果该电影用户已经看过，则跳过
                # predict the user's "interest" for each movie
                rank.setdefault(imdbid, 0)  # 没有值就为0
                rank[imdbid] += similarity_factor   #rank[movie]就是各个电影的相似度
                # 这里是把和各个用户的相似度加起来，而各个用户的相似度只是基于看过的公共电影数目除以这两个用户看过的电影数量积
                #print(rank[movie])
        # return the N best movies
       # rank_ = dict()
        rank_ = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]  #类型是list不是字典了
        for key,value in rank_:
            matrix.append(key)    #matrix为存储推荐的imdbId号的数组
            #print(key)     #得到了推荐的电影的imdbid号
        print(matrix)
        #return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
        return matrix







# class UserBasedCF(object):
#     ''' TopN recommendation - User Based Collaborative Filtering '''
#
#     def __init__(self):
#         self.trainset = {}  # 训练集
#         self.testset = {}  # 测试集
#         self.initialset = {}  # 存储要推荐的用户的信息
#         self.n_sim_user = 50
#         self.n_rec_movie = 10
#
#         self.movie_popular = {}
#         self.movie_count = 0  # 总电影数量
#
#         print('Similar user number = %d' % self.n_sim_user, file=sys.stderr)
#         print('recommended movie number = %d' %
#               self.n_rec_movie, file=sys.stderr)
#
#     @staticmethod
#     def loadfile(filename):
#         ''' load a file, return a generator. '''
#         fp = open(filename, 'r', encoding='UTF-8')
#         for i, line in enumerate(fp):
#             yield line.strip('\r\n')
#             # if i % 100000 == 0:
#             #     print ('loading %s(%s)' % (filename, i), file=sys.stderr)
#         fp.close()
#         print('load %s success' % filename, file=sys.stderr)
#
#     def initial_dataset(self, filename1):
#         initialset_len = 0
#         for lines in self.loadfile(filename1):
#             users, movies, ratings = lines.split(',')
#             self.initialset.setdefault(users, {})
#             self.initialset[users][movies] = (ratings)
#             initialset_len += 1
#
#     def generate_dataset(self, filename2, pivot=0.7):
#         ''' load rating data and split it to training set and test set '''
#         trainset_len = 0
#         testset_len = 0
#
#         for line in self.loadfile(filename2):
#             # user, movie, rating, _ = line.split('::')
#             user, movie, rating = line.split(',')
#             # split the data by pivot
#             if random.random() < pivot:  # pivot=0.7应该表示训练集：测试集=7：3
#                 self.trainset.setdefault(user, {})
#                 self.trainset[user][movie] = (rating)  # trainset[user][movie]可以获取用户对电影的评分  都是整数
#                 trainset_len += 1
#             else:
#                 self.testset.setdefault(user, {})
#                 self.testset[user][movie] = (rating)
#                 testset_len += 1
#
#         print('split training set and test set succ', file=sys.stderr)
#         print('train set = %s' % trainset_len, file=sys.stderr)
#         print('test set = %s' % testset_len, file=sys.stderr)
#
#     def calc_user_sim(self):
#         ''' calculate user similarity matrix '''
#         # build inverse table for item-users
#         # key=movieID, value=list of userIDs who have seen this movie
#         # print ('building movie-users inverse table...', file=sys.stderr)
#         movie2users = dict()
#
#         for user, movies in self.trainset.items():
#             for movie in movies:
#                 # inverse table for item-users
#                 if movie not in movie2users:
#                     movie2users[movie] = set()
#                 movie2users[movie].add(user)  # 看这个电影的用户id
#                 # print(movie)   #输出的是movieId
#                 # print(movie2users[movie])   #输出的是{'userId'...}
#                 # print(movie2users)    #movieId:{'userId','userId'...}
#
#                 # count item popularity at the same time
#                 if movie not in self.movie_popular:
#                     self.movie_popular[movie] = 0
#                 self.movie_popular[movie] += 1
#         # print ('build movie-users inverse table succ', file=sys.stderr)
#
#         # save the total movie number, which will be used in evaluation
#         self.movie_count = len(movie2users)
#         print('total movie number = %d' % self.movie_count, file=sys.stderr)
#
#         # count co-rated items between users  计算用户之间共同评分的物品
#         usersim_mat = user_sim_mat
#         # print ('building user co-rated movies matrix...', file=sys.stderr)
#
#         for movie, users in movie2users.items():  # 通过.items()遍历movie2users这个字典里的所有键、值
#             for u in users:
#                 for v in users:
#                     if u == v:
#                         continue
#                     usersim_mat.setdefault(u, {})
#                     usersim_mat[u].setdefault(v, 0)
#                     usersim_mat[u][v] += 1 / math.log(1 + len(users))  # usersim_mat二维矩阵应该存的是用户u和用户v之间共同评分的电影数目
#         # print ('build user co-rated movies matrix succ', file=sys.stderr)
#
#         # calculate similarity matrix
#         # print ('calculating user similarity matrix...', file=sys.stderr)
#         simfactor_count = 0
#         PRINT_STEP = 20000
#
#         for u, related_users in usersim_mat.items():
#             for v, count in related_users.items():
#                 usersim_mat[u][v] = count / math.sqrt(
#                     len(self.trainset[u]) * len(self.trainset[v]))
#                 simfactor_count += 1
#         #         if simfactor_count % PRINT_STEP == 0:
#         #             print ('calculating user similarity factor(%d)' %
#         #                    simfactor_count, file=sys.stderr)
#
#         # print ('calculate user similarity matrix(similarity factor) succ',
#         #        file=sys.stderr)
#         # print ('Total similarity factor number = %d' %
#         #        simfactor_count, file=sys.stderr)
#
#
#     def recommend(self, user):
#         ''' Find K similar users and recommend N movies. '''
#         matrix.clear()   #每次都要清空
#         K = self.n_sim_user  # 这里等于20
#         N = self.n_rec_movie  # 这里等于10
#         rank = dict()  # 用户对电影的兴趣度
#         # print(self.initialset[user])
#         # print(self.trainset[user])
#         watched_movies = self.trainset[user]  # user用户已经看过的电影  只包括训练集里的
#         # 这里之后不能是训练集
#         # watched_movies = self.initialset[user]
#         for similar_user, similarity_factor in sorted(user_sim_mat[user].items(),
#                                                       key=itemgetter(1), reverse=True)[
#                                                0:K]:  # itemgetter(1)表示对第2个域(相似度)排序   reverse=TRUE表示降序
#             for imdbid in self.trainset[similar_user]:  # similar_user是items里面的键，就是所有用户   similarity_factor是值，就是对应的相似度
#                 if imdbid in watched_movies:
#                     continue  # 如果该电影用户已经看过，则跳过
#                 # predict the user's "interest" for each movie
#                 rank.setdefault(imdbid, 0)  # 没有值就为0
#                 rank[imdbid] += similarity_factor   #rank[movie]就是各个电影的相似度
#                 # 这里是把和各个用户的相似度加起来，而各个用户的相似度只是基于看过的公共电影数目除以这两个用户看过的电影数量积
#                 #print(rank[movie])
#         # return the N best movies
#        # rank_ = dict()
#         rank_ = sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]  #类型是list不是字典了
#         for key,value in rank_:
#             matrix.append(key)    #matrix为存储推荐的imdbId号的数组
#             #print(key)     #得到了推荐的电影的imdbid号
#         print(matrix)
#         #return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]
#         return matrix


class ItemBasedCF(object):
    ''' TopN recommendation - Item Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_movie = 20
        self.n_rec_movie = 10

        self.movie_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        # print('Similar movie number = %d' % self.n_sim_movie, file=sys.stderr)
        # print('Recommended movie number = %d' %
        #       self.n_rec_movie, file=sys.stderr)

    @staticmethod
    def loadfile(filename):
        ''' load a file, return a generator. '''
        # data1=np.loadtxt(filename,delimiter=',',dtype=float)
        fp = open(filename, 'r', encoding='UTF-8')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            # if i % 100000 == 0:
            #     print ('loading %s(%s)' % (filename, i), file=sys.stderr)
        fp.close()
        print('load %s succ' % filename, file=sys.stderr)

    def generate_dataset(self, filename, pivot=1.0):
        ''' load rating data and split it to training set and test set '''
        trainset_len = 0
        testset_len = 0

        for line in self.loadfile(filename):
            user, movie, rating = line.split(',')
            # user, movie, rating = np.loadtxt(filename,delimiter=',')
            rating = float(rating)
            # print(type(rating))

            # split the data by pivot
            if random.random() < pivot:
                self.trainset.setdefault(user, {})

                self.trainset[user][movie] = float(rating)
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})

                self.testset[user][movie] = float(rating)
                testset_len += 1

        # print('split training set and test set succ', file=sys.stderr)
        print('train set = %s' % trainset_len, file=sys.stderr)
        # print('test set = %s' % testset_len, file=sys.stderr)

    def calc_movie_sim(self):
        ''' calculate movie similarity matrix '''
        print('counting movies number and popularity...', file=sys.stderr)

        for user, movies in self.trainset.items():
            for movie in movies:
                # count item popularity
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1

        # print('count movies number and popularity succ', file=sys.stderr)

        # save the total number of movies
        self.movie_count = len(self.movie_popular)
        print('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated users between items
        itemsim_mat = self.movie_sim_mat
        # print('building co-rated users matrix...', file=sys.stderr)

        for user, movies in self.trainset.items():
            for m1 in movies:
                for m2 in movies:
                    if m1 == m2:
                        continue
                    itemsim_mat.setdefault(m1, {})
                    itemsim_mat[m1].setdefault(m2, 0)
                    itemsim_mat[m1][m2] += 1 / math.log(1 + len(movies) * 1.0)

        #print('build co-rated users matrix succ', file=sys.stderr)

        # calculate similarity matrix
        #print('calculating movie similarity matrix...', file=sys.stderr)
        simfactor_count = 0
        PRINT_STEP = 2000000

        for m1, related_movies in itemsim_mat.items():
            for m2, count in related_movies.items():
                itemsim_mat[m1][m2] = count / math.sqrt(
                    self.movie_popular[m1] * self.movie_popular[m2])
                simfactor_count += 1
                if simfactor_count % PRINT_STEP == 0:
                    print('calculating movie similarity factor(%d)' %
                          simfactor_count, file=sys.stderr)

        #print('calculate movie similarity matrix(similarity factor) succ',
             # file=sys.stderr)
        #print('Total similarity factor number = %d' %
              #simfactor_count, file=sys.stderr)

    def recommend(self, user):
        ''' Find K similar movies and recommend N movies. '''
        K = self.n_sim_movie
        N = self.n_rec_movie
        matrix2.clear()
        rank = {}
        watched_movies = self.trainset[user]

        for movie, rating in watched_movies.items():
            for related_movie, similarity_factor in sorted(self.movie_sim_mat[movie].items(),
                                                           key=itemgetter(1), reverse=True)[:K]:
                if related_movie in watched_movies:
                    continue
                rank.setdefault(related_movie, 0)
                rank[related_movie] += similarity_factor * rating
        # return the N best movies
        #print(sorted(rank.items(), key=itemgetter(1), reverse=True)[:N])
        rank_ = sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]
        for key,value in rank_:
            matrix2.append(key)    #matrix为存储推荐的imdbId号的数组
            #print(key)     #得到了推荐的电影的imdbid号
        print(matrix2)
        #return sorted(rank.items(), key=itemgetter(1), reverse=True)[:N]
        return matrix2





#
if __name__ == '__main__':
    # ratingfile = os.path.join('ml-1m', 'ratings.dat')
    # ratingfile1 = os.path.join('ml-100k', 'insertusers.csv')
    ratingfile2 = os.path.join('static', 'users_resulttable.csv')  # 一共671个用户
    #ratingfile2 = os.path.join('static', 'rrtotaltable.csv')

    usercf = UserBasedCF()
    userId = '1'
    # usercf.initial_dataset(ratingfile1)
    usercf.generate_dataset(ratingfile2)
    usercf.calc_user_sim()
    # usercf.evaluate()
    usercf.recommend(userId)  # 给用户5推荐了10部电影  输出的是‘movieId’,兴趣度   109444、110148都是用户2已经看过并且评分为4的电影。
# print(sorted(user_sim_mat['2'].items(),key=itemgetter(1), reverse=True)[0:20])    #输出的是{'useId':{'另一个userId':相似度,'其他userId':'相似度...'}}...
#这里输的userId,是要从另一张储存登录用户的userid# 这里输的userId,是要从另一张储存登录用户的userid





