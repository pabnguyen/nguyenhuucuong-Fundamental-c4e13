
myf = open('alice.txt', 'r',encoding='utf8')

count = {}
#Đọc từng dòng rồi chia từng dòng thành từng từ
for line in myf:
    for word in line.split():

        # xóa những ký tự đặc biệt
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # chấp nhận ký tự in hoa
        word = word.lower()

        # chỉ chấp nhận chữ cái
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1
#xếp theo thứ tự 
keys = list(count.keys())
keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')
out.write("Word \t \t \t \tCount\n")
out.write("====================\n")
for word in keys:
    #Tiến hành in key và value
    out.write("%-12s%d\n" % (word, count[word]))
    out.write('\n')

print("The word 'alice' appears " , count['alice'] , " times in the book.")

#lTừ Dài nhất
ks = list(count.keys())
max_length = len(ks[0])
for i in range (len(ks)):
    if max_length < len(ks[i]):
        max_length = len(ks[i])
        vt = i

print("Lenghest word is",ks[vt],"Have",max_length,"words")
