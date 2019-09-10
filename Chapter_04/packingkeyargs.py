def about(name, age, like):
    info = "I am {}. I am {} years old and I like {}. ".format(name, age, like)
    return info


dictionary = {"name": "Ross", "age": 55, "like": "Python"}
print(about(**dictionary))
