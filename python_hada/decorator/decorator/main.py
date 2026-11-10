def decorator_saya(func):
    def wrapper():
        print("Sebelum fungsi")
        func()
        print("setelah fungsi dipanggil")
    return wrapper 

@decorator_saya
def say_hello():
    print("hello world")

say_hello()