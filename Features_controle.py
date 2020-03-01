import sys
from Features.F_descriptors import Descriptor_usage 
from Features.F_basic_exeptions import Exeption_handler

class Features():
  def __init__(self):
    self.feature_list = {"list" : self.list_of_features, 
                         "exit" : sys.exit,
                         "descriptor" : self.descriptor, 
                         "exeptions" : self.exeptions, 
                         "f2" : 2, 
                         "f2" : 3
                         } 

  def list_of_features(self):
    for feature in self.feature_list.keys():
      print(f" *{feature}")
    pass

  def descriptor(self):
    c= Descriptor_usage()
    print(f" current value is = {c.value_get()}")
    c.value_set(1)
    print(f" current value is = {c.value_get()}")

  def exeptions(self):
    e = Exeption_handler()
    e.eof_error()
    e.exception_error()
    e.file_exists_error()
    e.file_not_found_error()
    e.import_error()
    e.index_error()
    e.io_error()
    e.key_error()
    e.keyboard_interrupt()
    e.name_error()
    e.type_error()
    e.value_error()
    e.w_warning()
    e.zero_division_error()

