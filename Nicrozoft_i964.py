import json
import os

def getfiles(path):
	global cnt
	try:
		df = os.listdir(correntpath)
	except:
		return []
	ff = []
	files = [name for name in df if os.path.isfile(os.path.join(path, name))]
	for file in files:
		ff.append([cnt, file])
		cnt += 1
	folders = [name for name in df if not os.path.isfile(os.path.join(path, name))]
	for folder in folders:
		ff.append(getfiles(path + '\\' + folder).insert(0, folder))
	return ff

def compress_file(filename, cnt):
	os.system('makecab /l %s %s %d.i964'% (outptd, filename, cnt))

def uncompress_file(filename, outptdir):
	os.system('7z x %s -o%s'% (filename, outptdir))

def compress_files(curtree, path):
	ct = curtree[1:]
	for f_d in ct:
		if str(type(f_d[0])) == "<class 'int'>":
			compress_file((path + '\\' + f_d[1]), f_d[0])
		else:
			compress_files(f_d, path + '\\' + f_d[0])

os.system('title Nicrozoft i964')

while True:
	os.system('cls')
	o = input('Nicrozoft i964 打包及解压缩工具\n请选择操作: \n1.将某个文件夹封装到 i964 实例\n2.从某个已封装的 i964 实例解压缩\n9.退出\n\n警告！务必输入正确的路径！否则可能会带来不可预测的损失！\n\n键入操作: ')
	if (not len(list(o)) == 1) or (not o.isdigit()):
		continue
	o = int(o)
	if o == 1:
		os.system('cls')
		print('使用 Nicrozoft i964 封装文件夹')
		originaldir = input('输入要封装的文件夹(末尾不加路径分隔符):')
		outptd = input('输入要封装到的位置(末尾不加路径分隔符):')
		os.system('cls')
		print('使用 Nicrozoft i964 封装文件夹\n正在获取文件目录结构信息……\n')
		cnt = 0
		tree = getfiles(originaldir).insert(0, '')
		print(tree)
		os.system('pause')
		os.system('cls')
		print('使用 Nicrozoft i964 封装文件夹\n正在封装文件……\n')
		os.system('md %s'% (outptd))
		compress_files(tree, originaldir)
		json.dump(tree, '%s\\%s'% (outptd, 'tree.json'))
		os.system('cls')
		print('使用 Nicrozoft i964 封装文件夹\n封装完成\n')
		os.system('pause')
	if o == 2:
		pass
	if o == 3:
		break
