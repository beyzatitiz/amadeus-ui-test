import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

UI_URL = "https://flights-app.pages.dev/"

class FlightAppProject(unittest.TestCase):
    
    def setUp(self):  
        self.driver = webdriver.Firefox()

    def test_same_flight(self):
        self.driver.get(UI_URL)

        from_input = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-input-:Rq9lla:"]')
        from_input.click()
        from_input.send_keys("IST")
        from_input.send_keys(Keys.RETURN)

        to_input = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-input-:Rqhlla:"]')
        to_input.click()
        to_input.send_keys("IST")

        to_list = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-options-:R1qhlla:"]')
        all_list_items = to_list.find_elements(By.TAG_NAME, "li")

        self.assertEqual(0, len(all_list_items))

    def test_flight_finding(self):
        self.driver.get(UI_URL)

        from_input = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-input-:Rq9lla:"]')
        from_input.click()
        from_input.send_keys("IST")
        from_input.send_keys(Keys.RETURN)
        
        to_input = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-input-:Rqhlla:"]')
        to_input.click()
        to_input.send_keys("LAX")
        to_input.send_keys(Keys.RETURN)

        found_x_items_text = self.driver.find_element(By.XPATH, '/html/body/main/div[2]/div/p').get_attribute('innerText')
        found_x_items_text = found_x_items_text.split(" ")
        found_flight_count = int(found_x_items_text[1])
        flights_list = self.driver.find_elements(By.XPATH, '/html/body/main/div[2]/div/ul/li')
        flights_list_item_count = len(flights_list)

        self.assertEqual(found_flight_count, flights_list_item_count)

    def test_no_available_flights(self):
        self.driver.get(UI_URL)

        from_input = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-input-:Rq9lla:"]')
        from_input.click()
        from_input.send_keys("IST")
        from_input.send_keys(Keys.RETURN)

        to_input = self.driver.find_element(By.XPATH, '//*[@id="headlessui-combobox-input-:Rqhlla:"]')
        to_input.click()
        to_input.send_keys("JFK")
        to_input.send_keys(Keys.RETURN)

        main_div_children = self.driver.find_elements(By.XPATH, '/html/body/main/div[2]/*')

        self.assertEqual(len(main_div_children), 0)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
  print("---- Welcome to Amadeus Flight Search APP UI test script ----")
  unittest.main()
