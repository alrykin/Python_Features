import sys
from Features.F_descriptors import Descriptor_usage 

class Features():
  def __init__(self):
    self.feature_list = {"list" : self.list_of_features, 
                         "exit" : sys.exit,
                         "descriptor" : self.descriptor, 
                         "f1" : 1, 
                         "f2" : 2, 
                         "f3" : 3
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

