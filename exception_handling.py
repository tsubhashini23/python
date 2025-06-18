# with open("demo.txt","w") as testfile:
#     testfile.write("Sample exception handling two")
    
# try:
#     with open("test.txt","r") as testfile:
#         print(testfile.read())
    
# except Exception as e:
#     print(e) 
    
# finally:
#     print("close db connection")


try:
    
    numbers = [1,6,3,2]
    for num in numbers:
        if numbers[num] == 5:
            print(numbers[:: -1])

except Exception as e:
    print(e)
    
finally:
    print("Always executes")
