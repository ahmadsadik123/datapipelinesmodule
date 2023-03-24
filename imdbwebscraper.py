from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = webdriver.Chrome(
    "chromedriver.exe",
    options=options,
)


url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

driver.get(url)

time.sleep(2)

list = []

shows = driver.find_elements(
    "xpath",
    "//tbody[@class='lister-list']/tr",
)

for show in shows:
    title = show.find_element("xpath", ".//td[@class='titleColumn']/a").text
    year = show.find_element("xpath", ".//td[@class='titleColumn']/span").text
    rating = show.find_element("xpath", ".//td[@class='ratingColumn imdbRating']").text

    dict = {
        "Title": title,
        "Year": year,
        "Rating": rating,
    }

    list.append(dict)


df = pd.DataFrame(list)
df.insert(0, "Rank", range(1, len(df) + 1))
df["Year"] = df["Year"].str.replace("(", "").str.replace(")", "")
df["Year"] = df["Year"].astype("int")
print(df)
df.to_csv("Top250TVShows.csv", index=False)

driver.quit()
