# import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googleapiclient.discovery import build
import pandas as pd
import time
time.sleep(3)""
# Get user subscribers names
user = input("Enter your subscribers name: ")
sp = [(j.strip()) for j in user.split(",")]
# Process driver
driver = webdriver.Chrome()
driver.maximize_window()

# Prepare result lists
names = []
subscribers = []
videos = []

# Search multiple times user
for i in sp:
    try:
        # Search the users youtube channel name
        driver.get("http://www.youtube.com")
        wait = WebDriverWait(driver, 5)
        # find youtube search bar
        wait.until(EC.visibility_of_element_located((By.NAME, "search_query")))
        search_bar = driver.find_element(By.NAME, "search_query")
        search_bar.clear()
        search_bar.send_keys(i)
        search_bar.send_keys(Keys.ENTER)
        channel = wait.until(EC.element_to_be_clickable((
            By.XPATH, "(//a[@id='main-link' and contains(@href, '/@')])[1]"
        )))
        # then click
        channel.click()
    except Exception as e:
        print(e)

    # Default values if API lookup fails
    sub = "N/A"
    vid = "N/A"

    try:
        api = "AIzaSyB3AeKi7YU3T-ggwoRcD8nvmM59wsByTz8"
        youtube = build('youtube', 'v3', developerKey=api)
        # Search for the channel to get channelId
        request = youtube.search().list(
            part='snippet',
            q=i,
            type='channel',
            maxResults=1
        )
        response = request.execute()
        # if response items empty raise a error
        if not response.get('items'):
            raise Exception("Empty")
        channel_id = response['items'][0]['id'].get('channelId')
        if not channel_id:
            raise Exception("No channel id found")
        # get youtube channel statistics
        state = youtube.channels().list(
            part='statistics',
            id=channel_id
        )
        state_response = state.execute()
        stats = state_response['items'][0]['statistics']
        sub = stats.get('subscriberCount', "N/A")
        vid = stats.get('videoCount', "N/A")
    except Exception as e:
        print(e)

    # Append results for this channel
    names.append(i)
    subscribers.append(sub)
    videos.append(vid)

time.sleep(3)
driver.quit()

# Build dataframe and save
d = {"Name": names, "Subscriber": subscribers, "VideoCount": videos}

try:
    df = pd.DataFrame(d)
    df.to_csv('result2.csv', index=False)
except Exception as e:
    print(f"Error in: {e}")