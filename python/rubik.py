from __future__ import print_function

RED, ORANGE, YELLOW, WHITE, BLUE, GREEN = range(6)
FRONT, BACK, LEFT, RIGHT, TOP, BOTTOM = range(6)
N = [
     (TOP, RIGHT, BOTTOM, LEFT), #FRONT
     (TOP, LEFT, BOTTOM, RIGHT), #BACK
     (TOP, FRONT, BOTTOM, BACK), #LEFT
     (TOP, BACK, BOTTOM, RIGHT), #RIGHT
     (BACK, RIGHT, FRONT, LEFT), #TOP
     (BACK, LEFT, FRONT, BOTTOM), #BOTTOM
     ]

def main():
    init_faces()
    t = [('A', 'B', 'C'),
         ('D', 'E', 'F'),
         ('G', 'H', 'I')]
    print (t)
    print (rotateCW(t))
    print (rotateCW(rotateCW(t)))


    #print(rotate(t, CW))
    #print(rotate(t, CCW))


def rotateCCW(face):
    result = zip(*face)
    tmp = result[2]
    result[2] = result[0]
    result[0] = tmp
    return result 

def rotateCW(face):
    for i in range(3):
        face = rotateCCW(face)
    return face


def init_faces():
    for f in range(6):
        for c in range(6):
            pass


if __name__ == '__main__':
    main()
