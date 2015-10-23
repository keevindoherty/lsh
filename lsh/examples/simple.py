import pprint
import sys, os

sys.path.insert(0, os.path.abspath('../..'))
from lsh import LSHCache


if __name__ == '__main__':
    cache = LSHCache()
    
    docs = [
        "lipstick on a pig",
        "you can put lipstick on a pig",
        "you can put lipstick on a pig but it's still a pig",
        "you can put lipstick on a pig it's still a pig",
        "i think they put some lipstick on a pig but it's still a pig",
        "putting lipstick on a pig",
        "you know you can put lipstick on a pig",
        "they were going to send us binders full of women",
        "they were going to send us binders of women",
        "a b c d e f",
        "a b c d f"
        ]

    dups = {}
    for i, doc in enumerate(docs):
        dups[i] = cache.insert(doc.split(), i)

    for i, duplist in dups.items():
        if duplist:
            print 'orig [%d]: %s' % (i, docs[i])
            for dup in duplist:
                print'\tdup : [%d] %s' % (dup, docs[dup])
        else:
            print 'no dups found for doc [%d] : %s' % (i, docs[i])

    cache.save('test.pkl')

    # Make a new cache to try loading from file
    new_cache = LSHCache()

    new_cache.from_file('test.pkl')
    print new_cache.num_docs()
    print new_cache._cache == cache._cache
