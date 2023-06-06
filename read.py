#文字計數
data = []
count = 0
with open("reviews.txt", "r") as f:
	for line in f:
		data.append(line)
		count +=1
wc = {}# word cnt

for d in data:
	words = d.split()
	for word in words:
		if word in wc:#如果這個字有在字典裡 我把你字數加1
			wc[word] += 1
		else:
			wc[word] = 1#如果這個字沒有在字典裡 我把你新增key 進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
print(len(wc))
print(wc["Allen"])
while True:
	word = input("你要查什麼字:")
	if word == "q":
		break
	elif word in wc:
		print(word, "出現過的次數:", wc[word])
	else:
		print("這個字沒有出現過歐")
print("感謝使用本查詢功能")









sum_len = 0
for d in data: 
	sum_len += len(d)
print("留言的平均長度:", sum_len / len(data))

new = []
for d in data:
	if len(d) <= 100:
		new.append(d)
print("一共有",len(new), "筆留言長度小於等於100")

good = []
for d in data:
	if "good" in d:
		good.append(d)
print("一共有", len(good), "筆留言提到good")
