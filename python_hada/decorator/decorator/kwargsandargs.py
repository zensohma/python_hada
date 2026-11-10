def log_fungsi(func):
    def wrapper(*args, **kwargs):
        print(f"Panggilan fungsi: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_fungsi
def tambah(a, b):
    return a + b

print(tambah(3, 5)) 
# Output:
# Panggilan fungsi: tambah
# 8
