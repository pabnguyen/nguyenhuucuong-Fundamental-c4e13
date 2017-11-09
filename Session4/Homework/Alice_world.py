
myf = open('alice.txt', 'r',encoding='utf8')

count = {}
#read words in lines
for line in myf:
    for word in line.split():

        # remove punctuation
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '')

        # ignore case
        word = word.lower()

        # ignore numbers
        if word.isalpha():
            if word in count:
                count[word] = count[word] + 1
            else:
                count[word] = 1

keys = list(count.keys())
keys.sort()

# save the word count analysis to a file
out = open('alice_words.txt', 'w')
out.write("Word \t \t \t \tCount\n")
out.write("====================\n")
for word in keys:
    out.write("%-12s%d\n" % (word, count[word]))
    out.write('\n')

print("The word 'alice' appears " , count['alice'] , " times in the book.")

#lengthest word
ks = list(count.keys())
max_length = len(ks[0])
for i in range (len(ks)):
    if max_length < len(ks[i]):
        max_length = len(ks[i])
        vt = i

print("Lenghest word is",ks[vt],"Have",max_length,"words")
