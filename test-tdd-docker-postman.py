from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

import json
from typing import List

class TestClase01(unittest.TestCase):
    def setUp(self):
        driver_path = r'D:/CICLO VIII/ELECTIVO I TESTING/chromedriver_win32V108/chromedriver.exe'
        driver = webdriver.Chrome(executable_path=driver_path)
        self.driver = driver
        self.driver.get('http://localhost:8004/docs/')
        print('\n In setUp()...')
        time.sleep(3)
    
    def tearDown(self):
        print('\n In tearDown')
        time.sleep(10)
        self.driver.close()
        time.sleep(10)
        self.driver.quit()
    
    def test_summaries(self):
        print('\n Int Test_summaries()...')

        # GET
        i = 0
        while i in range(1):
            content = self.driver.find_elements(By.XPATH, "//button[@class='opblock-summary-control']")
            contenido=content[i].text
            content[1].click()
            summaries = self.driver.find_element(By.XPATH, "//div[@class='highlight-code']//pre")
            summary = summaries.text
            print(summary)
            
            time.sleep(5)
            content[2].click()
            try_it_out = self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-create_summary_summaries__post']//button[@class='btn try-out__btn']")

            try_it_out.click()

            # ------------------------------------------------------------------------------
            # POST
            print("\n Int Post()...")
            time.sleep(5)

            urls_lista = [
                {
                    'url': 'http://upeu.edu.pe',
                    'id': 0
                },
                {
                    'url': 'http://webapp.upeu.edu.pe',
                    'id': 1
                },
                {
                    'url': 'http://lambacademic.upeu.edu.pe',
                    'id': 2
                },
                {
                    'url': 'http://lamblearning.upeu.edu.pe',
                    'id': 3
                },
            ]    
            j=0
            while j in range(4):
                time.sleep(2)
                text_area = self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-create_summary_summaries__post']//textarea")
                text_area.clear()
                time.sleep(2)
                jsonarea = urls_lista[j]
                text_area.send_keys(json.dumps(jsonarea))
                self.driver.find_element(By.XPATH, "//button[@class='btn execute opblock-control__btn']").click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//button[@class='btn btn-clear opblock-control__btn']").click()
                print("Insertado", urls_lista[j])
                j=j+1
            
            # ------------------------------------------------------------------------------
            # PUT
            print("\n Int Update()...")
            time.sleep(5)
            content[4].click()
            try_it_outid = self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-update_summary_summaries__id___put']//button[@class='btn try-out__btn']")
            try_it_outid.click()

            time.sleep(3)
            self.driver.find_element(By.XPATH, "//td[@class='parameters-col_description']/input").send_keys(1)
            text_actualizar = {
                    "url": "http://www.upeu.edu.pe",
                    "summary": "Modificado"
                }
            texto_put = self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-update_summary_summaries__id___put']//textarea[@class='body-param__text']")
            texto_put.clear()
            texto_put.send_keys(json.dumps(text_actualizar))
            self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-update_summary_summaries__id___put']//button[@class='btn execute opblock-control__btn']").click()

            time.sleep(3)

            # ------------------------------------------------------------------------------
            # DELETE
            print("\n Int Delete()...") 
            content[5].click()
            try_it_outdelete = self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-delete_summary_summaries__id___delete']//button[@class='btn try-out__btn']")
            try_it_outdelete.click()
            
            time.sleep(3)
            self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-delete_summary_summaries__id___delete']//td[@class='parameters-col_description']/input").send_keys(2)
            
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-delete_summary_summaries__id___delete']//button[@class='btn execute opblock-control__btn']").click()

            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-delete_summary_summaries__id___delete']//button[@class='btn btn-clear opblock-control__btn']").click()
            

            time.sleep(3)
            id2delete =  self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-delete_summary_summaries__id___delete']//td[@class='parameters-col_description']/input")
            id2delete.clear()
            time.sleep(2)
            id2delete.send_keys(0)

            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[@id='operations-summaries-delete_summary_summaries__id___delete']//button[@class='btn execute opblock-control__btn']").click()

            i = i+1
        

        print("\n EL PROCESO HA TERMINADO()...")

        
if __name__ == '__main__':
    unittest.main()