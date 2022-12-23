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
        self.driver.get('http://localhost:8004/docs/')
        print('\n In setUp()...')
    
    def tearDown(self):
        print('\n In tearDown')
        time.sleep(10)
        self.driver.close()
        time.sleep(10)
        self.driver.quit()
    
    def test_json(self):
        print('\n Int Test_case01_lamb()...')
         # obtener el cuadro de texto de búsqueda

        i = 0
        while i in range(6):
            content = self.driver.find_elements(By.XPATH, "//button[@class='opblock-summary-control']")
            contenido=content[i].text
            content[1].click()
            summaries = self.driver.find_element(By.XPATH, "//div[@class='highlight-code']//pre")
            summary = summaries.text
            print(summary)
            
            time.sleep(5)
            content[2].click()
            # xpath_base_post = self.driver.find_element(By.XPATH,"//div[@id='operations-summaries-create_summary_summaries__post']")

            urls = ["http://upeu.edu.pe", "http://webapp.upeu.edu.pe", "http://lambacademic.upeu.edu.pe", "- http://lamblearning.upeu.edu.pe"]    
            j=0
            while j <= len(urls):
                self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-create_summary_summaries__post']//textarea").send_keys("{'url':}", urls[j])
                self.driver.find_element(By.XPATH, '//button[@class="btn execute opblock-control__btn"]').click()
                print()
                j=j+1

            print(summary)
            # POST

            i = i+1
        

        print("HA TERMINADO")

        
if __name__ == '__main__':
    unittest.main()