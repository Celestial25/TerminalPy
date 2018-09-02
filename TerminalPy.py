class color():

    #to be used as:
    #from TerminalPy import *
    #print(color.red + "your text")

    default = '\033[39m'
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[00m'



    #part 2:
    #to be used as:
    #from TerminalPy import *
    #c = color()
    #c.setc("red")

    def setc(self, colo):
        colo = colo.lower()
        if colo == "default":
            print(self.default)
        elif colo == "black":
            print(self.black)
        elif colo == "red":
    	    print(self.red)
        elif colo == "green":
             print(self.green)
        elif colo == "yellow":
            print(self.yellow)
        elif colo == "blue":
            print(self.blue)
        elif colo == "magenta":
            print(self.magenta)
        elif colo == "cyan":
            print(self.cyan)
        elif colo == "white":
            print(self.white)
        else:
	        print(self.red)
