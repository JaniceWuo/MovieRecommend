import csv
import pandas as pd

data = pd.read_csv('ratings.csv')
print(data)
# filename = 'ratings.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	print(header_row)
	#for row in reader: 

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }
#print(users["Veronica"])

#计算曼哈顿距离
def manhattan(rating1,rating2):
	distance = 0
	for key in rating1:
		if key in rating2:
			distance += abs(rating1[key] - rating2[key])
	return distance

#print(manhattan(users['Hailey'],users['Veronica']))

#对曼哈顿距离排序
def Neighbor(username,users):
	distances = []
	for user in users:  #在users里面循环找
		if user != username:
			distance = manhattan(users[user],users[username])
			distances.append((distance,user))
	distances.sort()
	return distances

#找距离最近的用户看过但自己未看过的
def recommend(username,users):
	nearest = Neighbor(username,users)[0][1]
	recommendation = []
	neighborRating = users[nearest]#最近邻居看过的电影列表
	userRating = users[username] #自己看过的电影列表

	for artist in neighborRating:
		if not artist in userRating:
			recommendation.append((artist,neighborRating[artist]))

	return sorted(recommendation, key=lambda artistTuple: artistTuple[1], reverse = True)


print(recommend('Hailey', users))  