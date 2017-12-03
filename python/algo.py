""" Basic algorithm functions and suchlike nonsense """
import sys
import logging


class Tree:

    def __init__(self, firstKid, nextSibling=None):
        self.firstKid = self.val = firstKid
        self.nextSibling = nextSibling


class Bunch(dict):

    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ = self


def main(args):
    logging.info(args)

    t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
    logging.debug(t.firstKid.nextSibling.nextSibling.val)

    j = Bunch(name='Jayne Cobb', position='Public Relations')
    logging.debug(j.name + ', ' + j.position)

if __name__ == '__main__':
    logging.basicConfig(
        format='%(levelname)s:%(asctime)s:%(message)s',
        level=logging.DEBUG)

    main(sys.argv[1:])
