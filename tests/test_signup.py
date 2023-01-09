from seleniumbase import BaseCase
class LoginTest(BaseCase):
    def test_chromesignup_page(self):
        self.open(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        self.send_keys('//*[@id="identifierId"]',"mehulkumarsinghchauhan@gmail.com")
        self.click('//*[@id="identifierNext"]/div/button/span')
        self.send_keys('//*[@id="password"]/div[1]/div/div[1]/input',"Flixborough@123")
        self.click('//*[@id="passwordNext"]/div/button/span')