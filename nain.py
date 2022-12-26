#4_задача

def x(*args):
    list = []
    list.extend(*args)

print(x([],[1],[2],[3],[1,2],[2,3],[1,2,3]))