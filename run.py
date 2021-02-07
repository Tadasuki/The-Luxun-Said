import os    # 载入OS模组
os.mkdir("cookie")    # 创建缓存文件夹

# 开始修改
infile = open("putin.txt", "r",encoding='utf-8')    
outfile = open("cookie\mid1.txt", "w",encoding='utf-8')    
for line in infile:
      outfile.write(line.replace('这样', '这般'))
infile.close()
outfile.close()

infile = open("cookie\mid1.txt", "r",encoding='utf-8')
outfile = open("cookie\mid2.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('大概', '大抵'))
infile.close()
outfile.close()

infile = open("cookie\mid2.txt", "r",encoding='utf-8')
outfile = open("cookie\mid3.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('的', '的'))
infile.close()
outfile.close()

infile = open("cookie\mid3.txt", "r",encoding='utf-8')
outfile = open("cookie\mid4.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('就', '便'))
infile.close()
outfile.close()

infile = open("cookie\mid4.txt", "r",encoding='utf-8')
outfile = open("cookie\mid5.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('吧', '罢'))
infile.close()
outfile.close()

infile = open("cookie\mid5.txt", "r",encoding='utf-8')
outfile = open("cookie\mid6.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('她', '伊'))
infile.close()
outfile.close()
 
infile = open("cookie\mid6.txt", "r",encoding='utf-8')
outfile = open("cookie\mid7.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('比如', '譬如'))
infile.close()
outfile.close()

infile = open("cookie\mid7.txt", "r",encoding='utf-8')
outfile = open("cookie\mid8.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('也', '亦然'))
infile.close()
outfile.close()

infile = open("cookie\mid8.txt", "r",encoding='utf-8')
outfile = open("cookie\mid9.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('如果', '倘若'))
infile.close()
outfile.close()

infile = open("cookie\mid9.txt", "r",encoding='utf-8')
outfile = open("cookie\mid10.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('啊', '呵'))
infile.close()
outfile.close()

infile = open("cookie\mid10.txt", "r",encoding='utf-8')
outfile = open("cookie\mid11.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('所以', '因此'))
infile.close()
outfile.close()

infile = open("cookie\mid11.txt", "r",encoding='utf-8')
outfile = open("cookie\mid12.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('什么', '甚么'))
infile.close()
outfile.close()

infile = open("cookie\mid12.txt", "r",encoding='utf-8')
outfile = open("cookie\mid13.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('一向', '向来'))
infile.close()
outfile.close()

infile = open("cookie\mid13.txt", "r",encoding='utf-8')
outfile = open("cookie\mid14.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('越', '愈'))
infile.close()
outfile.close()

infile = open("cookie\mid14.txt", "r",encoding='utf-8')
outfile = open("result.txt", "w",encoding='utf-8')
for line in infile:
      outfile.write(line.replace('寒冷', '凄冷'))
infile.close()
outfile.close()
# 修改结束

# 删除缓存
os.remove("cookie\mid1.txt")
os.remove("cookie\mid2.txt")
os.remove("cookie\mid3.txt")
os.remove("cookie\mid4.txt")
os.remove("cookie\mid5.txt")
os.remove("cookie\mid6.txt")
os.remove("cookie\mid7.txt")
os.remove("cookie\mid8.txt")
os.remove("cookie\mid9.txt")
os.remove("cookie\mid10.txt")
os.remove("cookie\mid11.txt")
os.remove("cookie\mid12.txt")
os.remove("cookie\mid13.txt")
os.remove("cookie\mid14.txt")
os.rmdir("cookie")

