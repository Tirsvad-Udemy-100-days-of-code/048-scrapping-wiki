# interaction.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Step 6: find the element with find_element() and print its text.
article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

driver.quit()
