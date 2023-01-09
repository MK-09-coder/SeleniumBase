from seleniumbase import BaseCase
import time
class LoginTest(BaseCase):
    def test_login_page(self):
        self.open("restaurantapp-c2ed6.firebaseapp.com")
        self.click(".drop-shadow-xl")
        self.open("https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=174416156605-c4gfj80mue5rhff6binbfnlgsv7pjvuc.apps.googleusercontent.com&redirect_uri=https%3A%2F%2Frestaurantapp-c2ed6.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmrmPEALBh44Sqie6xIWoxW1X7suCZVKDvKNbJTWgpCS97NetkFh6t3nwbboqAb58zNmiZfZNzr1ocLaAzPgIwAvz-TmUcqv8USx-NMRXR3aON-ccHsYHuV_705mW9N6PdnBUoez4u1fMwpX04XGN0q_7yKRn0UJvnyCE_5WhDmCPubeeQQ-hewAV-RPCfHJysyY3IIQ1jvk8u3-2zF1UhskOMygcBw-78yxF4lUYUc-UWltMezp6_6DM9V_3L1Sl8KCoej_S3f3gTAnvRgDM4wEQt6Kq46qEwxP5QcSSpf9A-WJSd6BOf8olp9SoeFoTVEb_2elc8fKqw&scope=openid%20https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fuserinfo.email%20profile&context_uri=https%3A%2F%2Frestaurantapp-c2ed6.firebaseapp.com")
        self.send_keys('//*[@id="identifierId"]',"mehulkumarsinghchauhan@gmail.com")
        self.click('//*[@id="identifierNext"]/div/button/span')
        self.send_keys('//*[@id="password"]/div[1]/div/div[1]/input',"Flixborough@123")
        self.click('//*[@id="passwordNext"]/div/button/span')
        self.open("restaurantapp-c2ed6.firebaseapp.com")
        self.click(".drop-shadow-xl")
        self.click(".bg-red-600")
        self.click('//*[@id="root"]/div/header/div[1]/div/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[1]/div/div[2]/div[2]')
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[1]/div/div[2]/div[1]')
        self.click('//*[@id="root"]/div/main/div/div/div[2]/div[2]/button')
        time.sleep(5)
        self.click('//*[@id="root"]/div/main/div/div/div[1]/div')
        self.click('//*[@id="root"]/div/header/div[1]/div/div[2]')



