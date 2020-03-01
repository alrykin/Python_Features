from Features import Features 

class Console():

  def __init__(self):
    self.feature = Features()
    pass

  def call(self, name):
    self.feature.descriptor()
    pass


c = Console()
name = 1#input()
c.call(name)