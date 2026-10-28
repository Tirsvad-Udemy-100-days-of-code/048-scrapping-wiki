# interaction.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# Step 7: the next lectures interact with the page:
# article_count.click()  # click a link
# search = driver.find_element(By.NAME, "search")  # type into a search field

driver.quit()
