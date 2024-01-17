class Myclass:
    Greeting = ""
    def __init__(self, Name = 'There'):
        self.Greeting = Name + "!"
    
    def SayHello(self):
        print ("Hello {0}".format(self.Greeting))

Myinstance = Myclass()

Myinstance.SayHello()
Myinstance2 = Myclass("Amy")
Myinstance2.SayHello()
Myinstance.Greeting = "Harry"
Myinstance.SayHello()
 