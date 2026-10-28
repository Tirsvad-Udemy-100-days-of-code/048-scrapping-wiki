# interaction.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Step 4: navigate to the main page of Wikipedia with get().
driver.get("https://en.wikipedia.org/wiki/Main_Page")
