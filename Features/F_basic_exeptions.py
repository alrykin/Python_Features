#types of Exeptions and different handlers

class Exeption_handler():
  def __init__(self):
    pass

  def key_error(self):   
    pass

  def index_error(self):
    a = [1, 2, 3]
    try: print(a[len(a)])
    except IndexError: print("IndexError. a[2] = 3; a.len = 3")

  def zero_division_error(self):
    try: 1 / 0
    except ZeroDivisionError: print("Zero division")

  def type_error(self):
    a = [1, 2, 3]
    try: print(a["b"])
    except TypeError: print("TypeError. int suggested") 

  def name_error(self):
    try: print(a)
    except NameError: print("Variable was not declared or is using before declaration")

  def value_error(self):
    try: int("qwe")
    except ValueError: print("ValueError. Invalid literal. Number suggested") 
  
  def keyboard_interrupt(self):
    pass #"Ctrl + C" in console

  def io_error(self):
    pass

  def import_error(self):
    pass
    
  def w_warning(self):
    pass
    
  def eof_error(self):
    pass

  def exception_error(self):
    pass 
    
  def file_exists_error(self):
    pass

  def file_not_found_error(self):
    try: open("1.txt") #file does not exist
    except: print("FileNotFoundError")
