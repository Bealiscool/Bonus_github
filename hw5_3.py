
def read_file(filename):
	#read file
	movie_data = []
	with open(filename, "r") as f:
		lines = f.readlines()
		headers = lines[0].strip().split(",")
		#把標題和內容結合起來
		for line in lines[1:]:
			values = line.strip().split(",")
			movie = dict(zip(headers, values))
			movie_data.append(movie)
	return movie_data
		
#print(lines[0])
#print(headers)
#print(movie_data)
#print(values)
#print(movie)


def top2016(data):
	movie_2016 = []
	movie_2016_title = []
	l = []
	for i in data:
		#把2016年的電影評分和標題各存起來
		if i['Year'] == '2016':
			movie_2016.append(i['Rating'])
			movie_2016_title.append(i['Title'])
	#把他們縫起來等等拿來用			
	dic2016 = dict(zip(movie_2016_title, movie_2016))
	n = 1
	for key in (sorted(dic2016, key = dic2016.get, reverse = True))[0:3]:
		print("Top", n, ":", key)
		n = n + 1

	

#revenue沒辦法轉成float
#a_revenue = {}
#revenue = 0
#for i in movie_data:
	#actors = i['Actors'].split('|')
	#revenue = convert_revenue(i['Revenue (Millions)'])
	#for j in actors:
		#if j in a_revenue:
			#a_revenue[j] += revenue
		#else:
			#a_revenue[j] = revenue

#print(float(revenue))

#print(a_revenue)
#h_a_revenue = sorted(a_revenue, key = a_revenue.get, reverse = True)
#print(h_a_revenue[0])











def EmmaWatson_rating(data):
	Emma = []
	score = []
	for i in data:
		if 'Emma Watson' in i['Actors']:
			#把該演員的標題和評分各存成列表
			Emma.append(i['Title'])
			score.append(float(i['Rating']))
	#用兩個列表算平均		
	average_rating = sum(score)/len(score)
	print("The average rating of Emma Watson's movies :", average_rating)
#print(score)
#print(Emma)


def top_4_actor(data):
	counts = {}
	for i in data:
		actors = i['Actors'].split('|')
		#演員在字典裡數字就加一
		for j in actors:
			if j in counts:
				counts[j] += 1
			else:
				counts[j] = 1
	#用value由高到低排序
	top_actors = sorted(counts, key = counts.get, reverse = True)[0:11]
	#因為前四名超過四個演員所以取最多參與次數11和9共十一名演員
	print(top_actors)

#print(actors)
#print(counts)

#top_actors = sorted(counts, key=counts.get, reverse=True)[:4]
#print(top_actors)

#sorted_times = sorted(counts.values(), reverse = True)
#actor_times = list(counts.items())
#for i in actor_times:
	#if i[1] == 11:
		#print(i)
	#if i[1] == 9:
		#print(i)

data = read_file("IMDB-Movie-Data.csv")
top2016(data)
EmmaWatson_rating(data)
top_4_actor(data)




