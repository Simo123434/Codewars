def rev(n):
    return " ".join([word[::-1] for word in n.split(" ")])

print(rev("Hello World"))
