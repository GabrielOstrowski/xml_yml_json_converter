class JsonWriter(object):
    def __init__(self,file):
        self.file = file

    def writedata(self):
        x = json.dumps(self.file)
        return x


if file2.endswith('.json') and filewritten == False:
    dstread = JsonWriter(srcfile) # moze wystapic blad podczas kopiowania jesli wartosci sa puste
    dstfile = dstread.writedata() # dlatego dodalem zmienna filewritten
    with open(file2,'w') as f:
        f.write(dstfile)