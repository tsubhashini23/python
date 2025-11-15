# with open("test.txt", "w") as document:
#     document.write("Sample text, Check")
#
# with open ("test.txt", "r") as document:
#     print(document.read())

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import json

driver = webdriver.Chrome()

data = {"name": "madhu", "role": "analyst", "company": "epam"}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)
print("Data written to file")

with open("data.json", "r") as read_file:
    loaded_data = json.load(read_file)
print(loaded_data)



# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "name")))

