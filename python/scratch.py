import string

kill1 = [chr(x) for x in range(97)]
kill2 = [chr(x) for x in range(123, 256)]
kill = "".join(kill1 + kill2)
all = string.maketrans('', '')
#kill = string.printable[:10] + string.printable[63:]

text = []
files = ['pg996.txt', 'pg76.txt']
for fname in files:
    text = text + [l[:-1] for l in open(fname, 'r')]
#print len(text)

words = []
for l in text:
    tmp = map(lambda x: x.lower().strip(kill), l[:-1].split(' '))
    words = words + tmp

#print len(words)

d = {}

for word in words:
    key = string.translate(word, all, kill)
    d[key] = d.get(key, 0) + 1

l1 = [(k, v) for (k, v) in d.iteritems()]
l1.sort(key=lambda x: -x[1])

import shelve
db = shelve.open('data-shelve')
db['dict'] = d
db['list'] = l1
#db.close()


words = [k*v for (k, v) in l1]

lettercount = {}
for word in words:
    tmp = list(word)
    for c in tmp:
       lettercount[c] = lettercount.get(c, 0) + 1

db['letters'] = lettercount
letters_kv = [(k, v) for (k, v) in lettercount.iteritems()]
letters_kv.sort(key = lambda x: -x[1])
db['letters-kv'] = letters_kv
db.close()
