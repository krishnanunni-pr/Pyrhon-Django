class Vscode:
    def compile(self):
        print("compiling using vscofe")
    def excecute(self):
        print("excecuting using vscode")
    def debug(self):
        print("debug using vscode")
class Pycharm:
    def compile(self):
        print("Compiling using pycharm")
    def excecute(self):
        print("excecuting using pycharm")
    def debug(self):
        print("debug using pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.excecute()
        ide.debug()
dev=Programmer()
pyc=Pycharm()
dev.coding(pyc)