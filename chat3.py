lines = [] #設計一個lines清單
with open('3.txt', 'r', encoding='utf-8-sig') as f: #打開檔案
	for line in f: #依每一行讀取檔案
		lines.append(line.strip()) #把每一行讀去的檔案塞到lines清單裡面

for line in lines: #叫出lines清單中的每一行
	s = line.split( ' ' ) 
		time = s[0][ :5] #字串可以當清單來看
			name = s[0][5: ]
print(name)
print(time)
print(s)