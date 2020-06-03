import sys
import os
import platform
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class absen(object):
    def __init__(self, username, password):
        self.options = Options()
        self.options.headless = True
        self.options.add_argument("--window-size=1366x768")
        self.driver = webdriver.Firefox(options=self.options)
        self.username = username
        self.password = password

    def wait(self, xpath, message, timeout=15):
        timeout = timeout
        try:
            element_present = EC.presence_of_element_located(
                (By.XPATH, xpath))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for {} loaded".format(message))
            self.driver.quit()
            sys.exit(1)

    def login(self):
        print("Login Start")
        self.driver.get('http://siakad.polinema.ac.id/')

        username_input = '//*[@id="username"]'
        password_input = '//*[@id="password"]'
        login_submit = '//*[@id="form_login"]/div[9]/button'

        self.wait(xpath=username_input, message="username input")

        self.driver.find_element_by_xpath(
            username_input).send_keys(self.username)
        self.driver.find_element_by_xpath(
            password_input).send_keys(self.password)
        self.driver.find_element_by_xpath(login_submit).click()

        home_presensi = '//*[@id="gm_akademik"]/ul/li[2]/a'

        self.wait(xpath=home_presensi, message="home page")
        print("Login Completed")

    def presensi(self):
        print("Presensi Start")
        p = []
        for i in range(14):
            p.append(
                '//*[@id="form-action-wrapper-tr_absensi"]/div[1]/div[1]/div/div/div[2]/table/tbody/tr[{}]/td[3]/div/span/input'.format(i+1))
        presensi_submit = '/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/form/div[1]/div[2]/div/div/button'

        self.driver.get(
            'http://siakad.polinema.ac.id/mahasiswa/tr_absensi/add')

        self.wait(xpath=p[0], message="question")

        for i in range(14):
            self.driver.find_element_by_xpath(p[i]).click()
        self.driver.find_element_by_xpath(presensi_submit).click()

        address_warning = '//*[@id="block_alamat"]/div'

        self.wait(xpath=address_warning, message="address")
        print("Presensi Completed")

    def create_log(self):
        print("Create Log Start")
        self.driver.get(
            'http://siakad.polinema.ac.id/mahasiswa/tr_absensi/index')
        latest_absen = '/html/body/div[3]/table/tbody/tr[1]/td[1]'
        view_detail = '/html/body/div[3]/table/tbody/tr[1]/td[2]/a'
        self.wait(xpath=latest_absen, message="latest absen")
        value_latest = self.driver.find_element_by_xpath(latest_absen).text
        self.driver.find_element_by_xpath(view_detail).click()

        p_last = '/html/body/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div[3]/form/div[1]/div/div/div/div[2]/table/tbody/tr[14]'

        self.wait(xpath=p_last, message="last question")

        element = self.driver.find_element_by_xpath(p_last)
        self.driver.execute_script("window.scrollBy(0, 210)")
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

        now = datetime.now()
        path_ss = os.path.join(os.getcwd(), 'log', 'screenshot')
        filename = 'Capture_{0}_{1}.png'.format(
            now.strftime('%d-%m-%Y_%H-%M-%S'), now.astimezone().tzinfo)
        fullname = os.path.join(path_ss, filename)
        self.driver.get_screenshot_as_file(fullname)

        self.driver.quit()

        file = open(os.path.join(os.getcwd(), 'log', 'log_absen.txt'), "a")
        file.write(
            "Job for date : {0} complete at {1}_{2}, please double check at log screenshot, filename : {3} - {4} \n".format(value_latest, now.strftime('%d-%m-%Y_%H-%M-%S'), now.astimezone().tzinfo, filename, self.username))
        file.close()

        print("Job done! see log for further information")
