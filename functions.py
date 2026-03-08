def student_info(*args, **kwargs):
    print(args)  # ('Math', 'Art', 'History')
    print(kwargs)  # {'name': 'John', 'age': 22}


courses = ["Math", "Art", "History"]
info = {"name": "John", "age": 22}
student_info(*courses, **info)
