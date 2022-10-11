class BuildInFunction_grps:
    def __init__(self,name):
        self.name = name
        self.module = None
    def function(self,ctx,pos_start=None,pos_end=None):
        from importlib import import_module
        try:
            from importlib import import_module
            self.module = import_module(f"BuildInFunction.{self.name}")
            print(self.module)
            return self.module.module(ctx,pos_start,pos_end)
        except ModuleNotFoundError:
            print(f"Ops ! no module name {self.name}")