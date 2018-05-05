class JavaScriptObject(dict):
    """docstring for JavaScriptObject."""
    def __init__(self, arg):
        super(JavaScriptObject, self).__init__()
        self.arg = arg
    def __getattribute__(self,item):
        try:
            return self[item]
        except KeyError as e:
            return super().__getattribute__(item)
