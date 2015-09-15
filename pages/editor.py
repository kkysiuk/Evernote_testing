from pages.basePage import BasePage 
from resources.config import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import unicodedata


class Editor(BasePage):
	"""LOCATORS"""
	buttons = {
	

	}

	dropdowns = {

	}

	radiobuttons = {
		
	}

	fields = {
		"title field": "//input[@id='gwt-debug-NoteTitleView-textBox']"

	}

	checkboxes = {
		
	}

	other_elements = {
		"editor frame": "//iframe[@id='entinymce_328_ifr']",
		"editor inactive frame": "//iframe[@id='EN_IframePanel_0']",
		"editor": "//body",
		"note title text": "//div[@id='gwt-debug-NoteTitleView-label']"

	}

	def enter_note_text(self, text):
		elem = self.switch_to_frame("editor frame")
		el = self.browser.find_element_by_id("tinymce")
		el.clear()
		el.send_keys(text)
		self.switch_to_default_frame()

	def get_note_text(self):
		elem = self.switch_to_frame("editor frame")
		self.click_on("editor")
		sleep(2)
		note_text = self.browser.find_element_by_id("tinymce").text
		self.switch_to_default_frame()
		return note_text		

	def get_note_title(self):
		elem = self.find('note title text')
		utext = elem.get_attribute('textContent') 
		text = unicodedata.normalize('NFKD', utext).encode('ascii','ignore')
		return text

