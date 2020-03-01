# value description code example. GOTO for watching over some stuff

#! exess_info remove method is not implemetned

class Descriptor():
  value = None
  exess_information_displayed = True

  def __get__(self, inst, cls):
    if self.value == None: return None # remove triggering when created
    self.information_output(f"Reading descripted value = {self.value}", \
                            f" from {inst}")
    return self.value
  
  def __set__(self, inst, val):
    print(f"Rewriting descripted value form {self.value} to {val}", \
          f" on {inst}")
    self.value = val

  def information_show_mode_change(self):
    self.exess_information_displayed = not(self.exess_information_displayed)

  def information_output(self, text, exess_text):
    if self.exess_information_displayed:
      print(text + exess_text)
    else:
      print(text) 


class Descriptor_usage():
  descripted_value = Descriptor()

  def __init__(self):
    print(" class created")
    print(f" current value is = {self.value_get()}")
    self.descripted_value = 0

  def value_get(self):
    return self.descripted_value

  def value_set(self, value):
    self.descripted_value = value


if __name__ == '__main__':
  c= Descriptor_usage()
  print(f" current value is = {c.value_get()}")
  c.value_set(1)
  print(f" current value is = {c.value_get()}")