class YamlReader(object):
    def __init__(self,file):
        self.file = file

    def readdata(self):
        with open(self.file, 'r') as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data


if file1.endswith('.yml' or '.yaml') and file2.endswith('.yml' or '.yaml'):
    with open(file2, 'w') as f:
        f.write(file1)
    filewritten = True
elif file1.endswith('.yaml') and filewritten == False:
    srcread = YamlReader(file1)
    srcfile = srcread.readdata()
    print(srcfile)
else:
    pass