class XmlReader(object):
    def __init__(self,file):
        self.file = file

    def readdata(self):
        x = xmltodict.parse(self.file)
        return x


if file1.endswith('.xml') and file2.endswith('.xml'):
    with open(file2, 'w') as f:
        f.write(file1)
    filewritten = True
elif file1.endswith('.xml') and filewritten == False:
    srcread = XmlReader(file1)
    srcfile = srcread.readdata()
    print(srcfile)
else:
    pass