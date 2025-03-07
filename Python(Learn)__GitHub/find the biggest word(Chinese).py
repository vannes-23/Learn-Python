# 引入 urllib 库以连接到互联网
import urllib.request, urllib.parse, urllib.error

address = input('Please enter the address: ')
# 将地址转换为文件句柄
fahand = urllib.request.urlopen(address)

# 初始化一个字典来统计单词出现的次数
word_count = {}
for line in fahand:
    # 解码意味着将字节转换为字符串
    words = line.decode().split()
    # 这段代码用于统计文本中每个单词出现的次数
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

bigword = None
bigcount = None
# 这段代码用于找到文本中出现次数最多的单词
for word, count in word_count.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
