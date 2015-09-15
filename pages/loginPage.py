from time import sleep

from pages.basePage import BasePage 
from resources.config import *

class LoginPage(BasePage):
	"""LOCATORS"""
	buttons = {
		"signin button":"//input[@id='login']"
	}

	dropdowns = {

	}

	radiobuttons = {
		
	}

	fields = {
		"username field": "//input[@id='username']",
		"password field": "//input[@id='password']"
	}

	checkboxes = {
		
	}

	other_elements = {
		
	}

	def login(self):
		self.fill_in("username field", login);
		self.fill_in("password field", password)
		self.click_on("signin button")
		sleep(10)

