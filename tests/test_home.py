from seleniumbase import BaseCase
import time
class HomeTest(BaseCase):
    def test_home_page(self):
        self.open("restaurantapp-c2ed6.firebaseapp.com")
        self.click('//*[@id="root"]/div/main/div/section[2]/div[2]/div[4]/div[1]/div[2]')
        self.click('//*[@id="menu"]/div/div[2]/div/div[4]/div[1]/div[2]')
        self.click('//*[@id="root"]/div/header/div[1]/div/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]')
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[1]/div/div[2]/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[1]/div')
        self.click('//*[@id="menu"]/div/div[1]/div[5]')
        self.click('//*[@id="menu"]/div/div[2]/div/div[3]/div[1]/div[2]')
        self.click('//*[@id="root"]/div/header/div[1]/div/div[1]')
        time.sleep(5)