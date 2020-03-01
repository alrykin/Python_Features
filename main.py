import sys
from Features_controle import Features 

class Console():
  def __init__(self):
    try:    
      self.feature = Features()
      print("Console started successfully")
    except:
      print("Error occured")
      sys.exit()

  def call(self, name):
    self.feature.feature_list[name]() 

  def run(self):
    while 1:
      name = input("\n>>>")
      try: c.call(name)
      except KeyError:
       print("There is no such command. Try 'list' ")
      except SystemExit:  
       print("Thanks for using")
       break


if __name__ == "__main__":
  c = Console()
  c.run()

