class XmlWriter(object):
    def __init__(self,file):
        self.file = file

    def writedata(self):
        x = dicttoxml(self.file).decode('utf-8')
        return x


if file2.endswith('.xml') and filewritten == False:
    dstread = XmlWriter(srcfile)
    dstfile = dstread.writedata()
    with open(file2,'wb') as f:
        f.write(dstfile)