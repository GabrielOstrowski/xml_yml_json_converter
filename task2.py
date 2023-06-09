# task 2
class JsonReader(object):
    def __init__(self,file):
        self.file = file

    def readdata(self):
        with open(self.file, 'r') as f:
            data = f.read()
        load = json.loads(data)
        return load

if file1.endswith('.json') and file2.endswith('.json'): # poprawic tak zeby to bylo w klasie
    with open(file2, 'w') as f:
        f.write(file1)
    filewritten = True
elif file1.endswith('.json') and filewritten == False:
    srcread = JsonReader(file1)
    srcfile = srcread.readdata()
    print(srcfile)
else:
    pass