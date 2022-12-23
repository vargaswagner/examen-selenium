from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys, ActionChains
import unittest
import time
import pytest

import json
import requests
from typing import List

class TestClase01(unittest.TestCase):
    def setUp(self):
        driver_path = r'D:/CICLO VIII/ELECTIVO I TESTING/chromedriver_win32V108/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        self.driver = driver
        self.driver.get('http://localhost:8004/ping')
        print('\n In setUp()...')
    
    def tearDown(self):
        print('\n In tearDown')
        time.sleep(10)
        self.driver.close()
        time.sleep(10)
        self.driver.quit()
    
    def test_get(self):
        print('\n Int Test_case01_lamb()...')
         # obtener el cuadro de texto de búsqueda
        url = "http://localhost:8004/ping"
        self.search_field = self.driver.find_element(By.XPATH, "//body//pre[@style='word-wrap: break-word; white-space: pre-wrap;']")

        ping = json.loads(self.search_field.text).keys()
        
        i = 0
        while i in range(3):
            print("hlhlhlh", ping)    
            i = i+1


        ActionChains(self.driver)\
            .move_to_element(self.search_field)\
            .pause(1)\
            .key_down(Keys.CONTROL)\
            .pause(5)\
            .click_and_hold()\
            .pause(1)\
            .send_keys("Hola")\
            .send_keys(Keys.RETURN)\
            .perform()
        
        l = self.driver

        print("HA TERMINADO")

        
if __name__ == '__main__':
    unittest.main()