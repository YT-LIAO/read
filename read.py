#計算有幾筆資料

data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print (len(data))
print('讀取完了，總共有', len(data), '筆資料')


# #計算平均留言的長度

# sum_len = 0
# for d in data:
#     sum_len = sum_len + len(d)

# print('留言的平均長度為',sum_len / len(data))

# #有多少筆資料長度小於100

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('一共有', len(new), '筆資料長度小於100')
# print(new[0])

# #有幾筆留言有good

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# print('一共有', len(good), '筆留言提到good')
# print(good[0])

#文字計數

wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增key進wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請輸入要查找的字: ')
    if word == 'q':
        break
    elif word in wc:
        print(word, '總共出現過', wc[word], '次')
    else:
        print('留言未出現這個字')
print('感謝你的使用')







