a =4
b =0

try:
    print("resource open")
    c = a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("resource close")
    print("finally block")
