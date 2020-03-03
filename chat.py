#打開一個檔案，一行一行的讀取
def read_file(filename): 
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:#'utf-8-sig'是去除掉檔案前面的特定編碼
		for line in f:
			lines.append(line.strip())#.strip()是去除換行符號 '\n'
	return lines

#一行一行讀取的時候，如果遇到人名後面就加入":"跟內容，如果沒遇到人名，就直接顯示內容，
def convert(lines):
	new = []
	person = None #假設person沒有被宣告的話，因為擔心第一行如果不是人名就會無法執行
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #直接進回到迴圈for line in lines:
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #如果person沒有值的話直接忽略person執行這行
			new.append(person + ': ' + line)
	return new

#做完上面兩個function後，將檔案名及內容寫進新的檔案內
def write_file(filename, lines): #除了寫入檔名外,也要寫入內容lines
	with open(filename, 'w') as f: #先創造一個有檔案名的檔案
		for line in lines:
			f.write(line + '\n') #逐行的把lines換行寫入


def main(): #主function
	lines = read_file('input.txt') #用read_file這個function打開'input.txt'
	lines = convert(lines) #使用convert這個function一行一行讀取的時候，如果遇到人名後面就加入":"跟內容，如果沒遇到人名，就直接顯示內容，並覆蓋上一個lines
	write_file('output.txt', lines) #使用write_file這個function，寫入檔案名'output.txt'，以及寫入內容lines

main() #進入點