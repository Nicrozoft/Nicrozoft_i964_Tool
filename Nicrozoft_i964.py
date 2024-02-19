import json
import os

def getfiles(path):
	print(1)
	global cnt
	try:
		df = os.listdir(path)
	except:
		return []
	ff = []
	files = [name for name in df if os.path.isfile(os.path.join(path, name))]
	for file in files:
		ff.append([cnt, file])
		cnt += 1
	folders = [name for name in df if not os.path.isfile(os.path.join(path, name))]
	for folder in folders:
		fd = getfiles(path + '\\' + folder)
		fd.insert(0, folder)
		ff.append(fd)
	return ff

def compress_file(filename, cnt):
	os.system('makecab /l %s %s %d.i964'% (outptd, filename, cnt))

def uncompress_file(filename, outptdir):
	os.system('7z x %s -o%s -aoa'% (filename, outptdir))

def compress_files(curtree, path):
	ct = curtree[1:]
	for f_d in ct:
		if str(type(f_d[0])) == "<class 'int'>":
			compress_file((path + '\\' + f_d[1]), f_d[0])
		else:
			compress_files(f_d, path + '\\' + f_d[0])

def uncompress_files(curtree, path):
	ct = curtree[1:]
	for f_d in ct:
		if str(type(f_d[0])) == "<class 'int'>":
			uncompress_file(('%s\\%d'% (compressed_dir, f_d[0])) + '.i964', (path + '\\'))
		else:
			os.system('md %s\\%s'% (path, f_d[0]))
			uncompress_files(f_d, path + '\\' + f_d[0])

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
		tree = getfiles(originaldir)
		tree.insert(0, '')
		os.system('cls')
		print('使用 Nicrozoft i964 封装文件夹\n正在封装文件……\n')
		os.system('md %s'% (outptd))
		compress_files(tree, originaldir)
		with open('%s\\%s'% (outptd, 'tree.json'), 'w', encoding = 'utf-8') as f:
			json.dump(tree, f)
		os.system('cls')
		print('使用 Nicrozoft i964 封装文件夹\n封装完成\n')
		os.system('pause')
	if o == 2:
		os.system('cls')
		print('使用 Nicrozoft i964 解压缩已被封装的文件夹')
		compressed_dir = input('输入已被封装的文件夹(末尾不加路径分隔符):')
		outptd = input('输入要解压缩到的位置(末尾不加路径分隔符):')
		os.system('cls')
		print('使用 Nicrozoft i964 解压缩已被封装的文件夹\n正在获取文件目录结构信息……\n')
		with open('%s\\%s'% (compressed_dir, 'tree.json'), 'r', encoding = 'utf-8') as f:
			tree = json.load(f)
		os.system('cls')
		print('使用 Nicrozoft i964 解压缩已被封装的文件夹\n正在解压缩文件……\n')
		os.system('md %s' % (outptd))
		uncompress_files(tree, outptd)
		os.system('cls')
		print('使用 Nicrozoft i964 解压缩已被封装的文件夹\n解压缩完成\n')
		os.system('pause')
	if o == 3:
		break
