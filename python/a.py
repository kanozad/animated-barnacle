
def spam():
    print('a.spam')
    
from b import spam

if __name__=='__main__':
    spam()
