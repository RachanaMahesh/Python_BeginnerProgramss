
def wrap(string, max_width):
    i=0
    while len(string)>0:
        print(string[:max_width])
        string = string[max_width-1:]
    return

string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
max_width = 4
wrap(string,max_width)