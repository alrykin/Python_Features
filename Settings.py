#unrealized potential

    metod_list = [metod for metod in dir(e) if not metod.startswith("__")]
    print(metod_list)
    for metod in metod_list:
      e.globals()[metod]()