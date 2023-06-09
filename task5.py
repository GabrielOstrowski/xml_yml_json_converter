class YamlWriter(object):
    def __init__(self,file):
        self.file = file

    def writedata(self):
        x = yaml.dump(self.file)
        return x


if file2.endswith('.yml' or '.yaml') and filewritten == False:
    dstread = YamlWriter(srcfile)
    dstfile = dstread.writedata()
    with open(file2,'w') as f:
        f.write(dstfile)