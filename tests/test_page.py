from seleniumbase import BaseCase
import time
class PageTest(BaseCase):
    def test_page(self):
        self.open("restaurantapp-c2ed6.firebaseapp.com")
        self.click('//*[@id="root"]/div/main/div/section[2]/div[2]/div[1]/div[1]/div[2]')
        self.click('//*[@id="root"]/div/main/div/section[2]/div[2]/div[4]/div[1]/div[2]')
        self.click('//*[@id="menu"]/div/div[1]/div[7]')
        self.click('//*[@id="menu"]/div/div[2]/div/div[9]/div[1]/div[2]')
        self.click('//*[@id="menu"]/div/div[1]/div[6]')
        self.click('//*[@id="menu"]/div/div[2]/div/div[9]/div[1]/div[2]')
        self.click('//*[@id="menu"]/div/div[1]/div[3]')
        self.click('//*[@id="menu"]/div/div[2]/div/div[1]/div[1]/div[2]')
        self.click('//*[@id="root"]/div/header/div[1]/div/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[1]/div/div[2]/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[1]/div')
        self.click('//*[@id="root"]/div/header/div[1]/div/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[1]/p[2]')
        self.click('//*[@id="root"]/div/main/div/div/div[1]/div')
        self.click('//*[@id="root"]/div/main/div/section[2]/div[2]/div[1]/div[1]/div[2]')
        self.click('//*[@id="root"]/div/header/div[1]/div/div[1]')
        time.sleep(5)
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[2]/button')