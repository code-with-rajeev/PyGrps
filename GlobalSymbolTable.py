class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        self.parent_ = ""
        self.type_ = None
    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value
    def set(self, name, value , parent = None):
            self.symbols[name] = value
    def type(self,parent):
        self.type_ = True
        self.parent_ = parent
    def remove(self, name):
        del self.symbols[name]
    def view(self):
        return self.symbols