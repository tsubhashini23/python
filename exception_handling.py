with open("demo.txt","w") as testfile:
    testfile.write("Sample exception handling two")
    
try:
    with open("test.txt","r") as testfile:
        print(testfile.read())
    
except Exception as e:
    print(e) 
    
finally:
    print("close db connection")