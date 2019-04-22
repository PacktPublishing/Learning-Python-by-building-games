def about(**kwargs):
    for key, value in kwargs.items():
          print("{} is {}".format(key,value))

about(Python = "Easy", Java = "Hard")
