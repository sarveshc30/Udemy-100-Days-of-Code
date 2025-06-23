
try:
    file = open('file.txt')
except FileNotFoundError:
    file = open('file.txt', 'w')
else:
    content = file.read()
    print(content)
finally:
    file.close()
