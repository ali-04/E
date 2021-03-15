from selenium import webdriver as dr
from time import sleep as sl


def lod (tx='loaded??     '):
    return input(tx)

class sah :
    ...

driv = dr.Firefox()

e = 0
while e == 0:
    try:

        driv.get(r'https://account.emofid.com/Login?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Deasy2_client_pkce%26redirect_uri%3Dhttps%253A%252F%252Fd.easytrader.emofid.com%252Fauth-callback%26response_type%3Dcode%26scope%3Deasy2_api%2520openid%26state%3Df8136d0f40a647e3b379b604c5440222%26code_challenge%3DTVlCox_afM7WZk8aPQJL1bbLxrXezzN2-OPmYxTa6NA%26code_challenge_method%3DS256%26response_mode%3Dquery')

        lod()

        sh = driv.find_element_by_xpath(r'//*[@id="Username"]')

        pas = driv.find_element_by_xpath(r'//*[@id="Password"]')

        cod = driv.find_element_by_xpath(r'//*[@id="Captcha"]')

        log = driv.find_element_by_xpath(r'//*[@id="submit_btn"]')




        lod()


        sh.send_keys('09398043882')
        pas.send_keys('Mah.411481384')
        cod.send_keys(lod(tx='Enter....  '))
        log.click()
        try: e = {'1':1,'y':1,'Y':1,'yes':1,'Yes':1} [lod()]
        except: e = 0
    except: e = 0









