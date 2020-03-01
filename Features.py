from F_descriptors import Descriptor_usage 

class Features():
  def __init__(self):
    feature_list = {"descriptor" : self.descriptor} 

  def descriptor(self):
    c= Descriptor_usage()
    print(f" current value is = {c.value_get()}")
    c.value_set(1)
    print(f" current value is = {c.value_get()}")

