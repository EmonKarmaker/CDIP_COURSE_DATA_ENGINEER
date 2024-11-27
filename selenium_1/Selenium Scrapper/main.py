from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import json


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")


chrome_driver_path = r'C:\Users\Emon Karmoker\Downloads\chromedriver_win32\chromedriver.exe'



driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)


driver.get("https://www.imdb.com/calendar/?ref_=rlm&region=US&type=MOVIE")


time.sleep(5)


stop_date = "2025-01"


movie_data = []


try:
    movie_elements = driver.find_elements(By.CLASS_NAME, 'list_item')

    for movie in movie_elements:
        try:
            movie_name = movie.find_element(By.CLASS_NAME, 'hover-over-image').text
            release_date = movie.find_element(By.CLASS_NAME, 'release_date').text.strip()


            if release_date and release_date != "TBD" and release_date <= stop_date:

                movie_data.append({
                    "Movie name": movie_name,
                    "Release Date": release_date
                })

        except Exception as e:
            continue


    for movie in movie_data:
        print(f"Movie name: {movie['Movie name']}, Release Date: {movie['Release Date']}")


    with open("imdb_movies.json", "w") as file:
        json.dump(movie_data, file, indent=4)

    print("Data saved to imdb_movies.json")

finally:

    driver.quit()
