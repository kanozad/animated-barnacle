import shelve
db = shelve.open('data-shelve')

ll = db.get('list')
db.close()

words = [k*v for (k, v) in ll]

lettercount = {}
for word in words:
    tmp = list(word)
    for c in tmp:
       lettercount[c] = lettercount.get(c, 0) + 1

db = shelve.open('data-shelve')
db['letters'] = lettercount
