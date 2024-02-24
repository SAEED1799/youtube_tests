from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Mute_Video_Page:
    def __init__(self, driver):
        self.driver = driver

    def go_to_video(self, video_url):
        self.driver.get(video_url)
        WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='movie_player']/div[1]/video")))

    def mute_video(self):
        try:
            # Wait for the mute button to be clickable
            mute_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Mute']"))
            )
            # Click the mute button
            mute_button.click()
        except TimeoutException:
            print("Mute button not found or not clickable within 10 seconds.")

    def is_video_muted(self):
        try:
            # Find the mute button
            mute_button = self.driver.find_element(By.CSS_SELECTOR, "button.ytp-mute-button")
            if mute_button:
                # Check if the mute button is in the muted state
                return "ytp-mute-button" in mute_button.get_attribute("class").split()
            else:
                print("Mute button not found.")
                return False
        except NoSuchElementException:
            print("Mute button not found.")
            return False