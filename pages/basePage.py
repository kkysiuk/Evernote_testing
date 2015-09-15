from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from resources.wrapper import Wrapper
from resources.config import login_page_url

class BasePage(object):
	def __init__(self):
		self.browser = Wrapper()
		#self.browser.maximize_window()

	def open_url(self, url=login_page_url):
		self.browser.get(url)

	def find_xpath_by_key(self, key):
		key = key.lower()
		if key in self.dropdowns:
			element_xp = self.dropdowns[key]
		elif key in self.fields:
			element_xp = self.fields[key]
		elif key in self.checkboxes:
			element_xp = self.checkboxes[key]
		elif key in self.radiobuttons:
			element_xp = self.radiobuttons[key]
		elif key in self.buttons:
			element_xp = self.buttons[key]
		elif key in self.other_elements:
			element_xp = self.other_elements[key]
		else:
			raise AssertionError, "Cannot find %s key in %s" % (key, str(self))
		return element_xp


	def find(self, key):
		element = self.find_xpath_by_key(key)
		WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, element)))
		return self.browser.find_element_by_xpath(element)

	def fill_in(self, key, value = ''):
		el = self.find(key)
		el.clear()
		el.send_keys(value)
		return el
	
	def text_of(self, key):
		return self.find(key).text

	def click_on(self, key):
		self.find(key).click()

	def move_to(self, key):
		actions = ActionChains(self.browser)
		actions.move_to_element(self.find(key)).perform()

	def element_should_be_present(self, key):
		self.find(key).is_displayed()

	def switch_to_frame(self, key):
		iframe = self.browser.find_element_by_xpath(self.other_elements[key])
		self.browser.switch_to_frame(iframe)

	def switch_to_default_frame(self):
		self.browser.switch_to_default_content()

	def open_new_tab(self):
		body = self.browser.find_element_by_tag_name('body')
		body.send_keys(Keys.CONTROL + 't')
		

	def switch_to_another_tab(self):
		body = self.browser.find_element_by_tag_name('body')
		body.send_keys(Keys.ALT + '1')
		