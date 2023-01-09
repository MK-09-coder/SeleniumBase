from seleniumbase import BaseCase
class CreateTest(BaseCase):
    def test_create_page(self):
        self.open("https://www.swiggy.com/")
        self.click("._2fX4J a")
        self.click("._3p4qh")
        self.send_keys("input#mobile","7204493460")
        self.send_keys("input#name","MK")
        self.send_keys("input#email","MK@gmail.com")
        self.click(".a-ayg")

