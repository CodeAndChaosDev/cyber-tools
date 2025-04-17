class Scanner(object):
    def __init__(self, url=None, ip=None):
        self.url = url
        self.ip = ip
    
    
    def init(self):
        if self.url and self. ip == None:
            return "URL or IP needed"