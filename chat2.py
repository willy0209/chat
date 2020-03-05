#清單切割寫法:
#n[開始值:結束值](開始有包行，結束沒包含)
#n[:3]可以拿到前三個(開始值是0可以不用寫)
#n[2:4]可以以一個清單裝著拿到n[2]跟n[4]
#n[-2:]可以拿到最後兩個(結尾值不寫表示到底)

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	person = None
	Allen_word_count = 0
	Viki_word_count = 0
	Allen_sticker_count = 0
	Viki_sticker_count = 0
	Allen_image_count = 0
	Viki_image_count = 0
	for line in lines:
		s = line.split(' ') #遇到空白鑑就切一刀
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				Allen_sticker_count +=1
			elif s[2] == '圖片':
				Allen_image_count +=1
			else:
				for m in s[2:]:
					Allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				Viki_sticker_count +=1
			elif s[2] == '圖片':
				Viki_image_count += 1
			else:
				for m in s[2:]:
					Viki_word_count += len(m)
	print('Allen 說了', Allen_word_count, '個字,', '傳了', Allen_sticker_count, '個貼圖,', '傳了', Allen_image_count, '張圖片。')
	print('Viki 說了', Viki_word_count, '個字,', '傳了', Viki_sticker_count, '個貼圖,', '傳了', Viki_image_count, '張圖片。')

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('line_vicky.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)


main()