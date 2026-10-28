# interaction.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Step 5: identify the element. The article count is the anchor (a)
# inside the div whose id is "articlecount", so the CSS selector is:
#     #articlecount a
