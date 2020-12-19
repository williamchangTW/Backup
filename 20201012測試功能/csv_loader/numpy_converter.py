# numpy processing
# TODO: need change parameter
class SizedReader:
    def __init__(self, fd, encoding='utf-8'):
        self.fd = fd
        self.size = 0
        self.encoding = encoding   # specify encoding in constructor, with utf8 as default
    def __next__(self):
        line = next(self.fd)
        self.size += len(line)
        return line.decode(self.encoding)   # returns a decoded line (a true Python 3 string)
    def __iter__(self):
        return self
