import sys
import random
import math
import os
from operator import itemgetter


random.seed(0)
user_sim_mat = {}
class UserBasedCF(object):
    ''' TopN recommendation - User Based Collaborative Filtering '''

    def __init__(self):
        self.trainset = {}   #训练集
        self.testset = {}    #测试集

        self.n_sim_user = 20
        self.n_rec_movie = 10


        self.movie_popular = {}
        self.movie_count = 0   #总电影数量

        print ('Similar user number = %d' % self.n_sim_user, file=sys.stderr)
        print ('recommended movie number = %d' %
               self.n_rec_movie, file=sys.stderr)

    @staticmethod
    def loadfile(filename):
        ''' load a file, return a generator. '''
        fp = open(filename, 'r')
        for i, line in enumerate(fp):
            yield line.strip('\r\n')
            # if i % 100000 == 0:
            #     print ('loading %s(%s)' % (filename, i), file=sys.stderr)
        fp.close()
        print ('load %s success' % filename, file=sys.stderr)

    def generate_dataset(self, filename, pivot=0.7):
        ''' load rating data and split it to training set and test set '''
        trainset_len = 0
        testset_len = 0

        for line in self.loadfile(filename):
           # user, movie, rating, _ = line.split('::')
            user, movie, rating= line.split(',')
            # split the data by pivot
            if random.random() < pivot:       #pivot=0.7应该表示训练集：测试集=7：3
                self.trainset.setdefault(user, {})
                self.trainset[user][movie] = (rating)    #  trainset[user][movie]可以获取用户对电影的评分  都是整数
                trainset_len += 1
            else:
                self.testset.setdefault(user, {})
                self.testset[user][movie] = (rating)
                testset_len += 1

        print ('split training set and test set succ', file=sys.stderr)
        print ('train set = %s' % trainset_len, file=sys.stderr)
        print ('test set = %s' % testset_len, file=sys.stderr)

    def calc_user_sim(self):
        ''' calculate user similarity matrix '''
        # build inverse table for item-users
        # key=movieID, value=list of userIDs who have seen this movie
        #print ('building movie-users inverse table...', file=sys.stderr)
        movie2users = dict()

        for user, movies in self.trainset.items():
            for movie in movies:
                # inverse table for item-users
                if movie not in movie2users:
                    movie2users[movie] = set()
                movie2users[movie].add(user)  #看这个电影的用户id
                #print(movie)   #输出的是movieId
                #print(movie2users[movie])   #输出的是{'userId'...}
                #print(movie2users)    #movieId:{'userId','userId'...}

                # count item popularity at the same time
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        #print ('build movie-users inverse table succ', file=sys.stderr)

        # save the total movie number, which will be used in evaluation
        self.movie_count = len(movie2users)
        print ('total movie number = %d' % self.movie_count, file=sys.stderr)

        # count co-rated items between users  计算用户之间共同评分的物品
        usersim_mat = user_sim_mat
        #print ('building user co-rated movies matrix...', file=sys.stderr)

        for movie, users in movie2users.items():   #通过.items()遍历movie2users这个字典里的所有键、值
            for u in users:
                for v in users:
                    if u == v:
                        continue
                    usersim_mat.setdefault(u, {})
                    usersim_mat[u].setdefault(v, 0)
                    usersim_mat[u][v] += 1 / math.log(1+len(users))  #usersim_mat二维矩阵应该存的是用户u和用户v之间共同评分的电影数目
        #print ('build user co-rated movies matrix succ', file=sys.stderr)

        # calculate similarity matrix
       # print ('calculating user similarity matrix...', file=sys.stderr)
        simfactor_count = 0
        PRINT_STEP = 20000

        for u, related_users in usersim_mat.items():
            for v, count in related_users.items():
                usersim_mat[u][v] = count / math.sqrt(
                    len(self.trainset[u]) * len(self.trainset[v]))
                simfactor_count += 1
        #         if simfactor_count % PRINT_STEP == 0:
        #             print ('calculating user similarity factor(%d)' %
        #                    simfactor_count, file=sys.stderr)

        # print ('calculate user similarity matrix(similarity factor) succ',
        #        file=sys.stderr)
        # print ('Total similarity factor number = %d' %
        #        simfactor_count, file=sys.stderr)

    def recommend(self, user):
        ''' Find K similar users and recommend N movies. '''
        K = self.n_sim_user  #这里等于20
        N = self.n_rec_movie  #这里等于10
        rank = dict()  #用户对电影的兴趣度
        watched_movies = self.trainset[user]   #user用户已经看过的电影  只包括训练集里的

        for similar_user, similarity_factor in sorted(user_sim_mat[user].items(),
                                                      key=itemgetter(1), reverse=True)[0:K]: #itemgetter(1)表示对第2个域(相似度)排序   reverse=TRUE表示降序
            for movie in self.trainset[similar_user]:       #similar_user是items里面的键，就是所有用户   similarity_factor是值，就是对应的相似度
                if movie in watched_movies:
                    continue       #如果该电影用户已经看过，则跳过
                # predict the user's "interest" for each movie
                rank.setdefault(movie, 0)  #没有值就为0
                rank[movie] += similarity_factor    #这里是把和各个用户的相似度加起来，而各个用户的相似度只是基于看过的公共电影数目除以这两个用户看过的电影数量积
        # return the N best movies
        print(sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N])
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]

    def evaluate(self):
        ''' print evaluation result: precision, recall, coverage and popularity '''
        print ('Evaluation start...', file=sys.stderr)

        N = self.n_rec_movie
        #  varables for precision and recall
        hit = 0
        rec_count = 0
        test_count = 0
        # varables for coverage
        all_rec_movies = set()
        # varables for popularity
        popular_sum = 0

        for i, user in enumerate(self.trainset):
            if i % 100 == 0:
                print ('recommended for %d users' % i, file=sys.stderr)
            test_movies = self.testset.get(user, {})
            rec_movies = self.recommend(user)
            for movie, _ in rec_movies:
                if movie in test_movies:
                    hit += 1           #求推荐的电影和测试集中电影的交集数量，做分子
                all_rec_movies.add(movie)
                popular_sum += math.log(1 + self.movie_popular[movie])
            rec_count += N
            test_count += len(test_movies)

        precision = hit / (1.0 * rec_count)
        recall = hit / (1.0 * test_count)
        coverage = len(all_rec_movies) / (1.0 * self.movie_count)
        popularity = popular_sum / (1.0 * rec_count)

        print ('precision=%.4f\trecall=%.4f\tcoverage=%.4f\tpopularity=%.4f' %
               (precision, recall, coverage, popularity), file=sys.stderr)


if __name__ == '__main__':
    #ratingfile = os.path.join('ml-1m', 'ratings.dat')
    ratingfile = os.path.join('ml-100k', 'rrtotaltable.csv')         #一共671个用户
    usercf = UserBasedCF()
    userId = '671'
    usercf.generate_dataset(ratingfile)
    usercf.calc_user_sim()
    #usercf.evaluate()
    usercf.recommend(userId)   #给用户5推荐了10部电影  输出的是‘movieId’,兴趣度   109444、110148都是用户2已经看过并且评分为4的电影。
   # print(sorted(user_sim_mat['2'].items(),key=itemgetter(1), reverse=True)[0:20])    #输出的是{'useId':{'另一个userId':相似度,'其他userId':'相似度...'}}...
