import sys

def main():
    recaman(0, [0])


def recaman(i, l):
    if i == 100:
        sys.exit()
    
    nextjump = i + 1;
    current = l[-1]
    if current - nextjump < 1 or current - nextjump in l:
        l.append(current + nextjump)
    else:
        l.append(current - nextjump)

    print(l)

    recaman(nextjump, l)
        


if __name__ == '__main__':
    main()