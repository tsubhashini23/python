with open("test.txt", "w") as document:
    document.write("Sample text, Check")
    
with open ("test.txt", "r") as document:
    print(document.read())