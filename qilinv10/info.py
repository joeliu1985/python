class Info:
    def __init__(self, str,ip):
        self.str = str
        self.ip=ip

    def __repr__(self):
        return 'info({})'.format(self.ip)