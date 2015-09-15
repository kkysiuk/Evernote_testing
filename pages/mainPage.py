from selenium.webdriver.common.keys import Keys

from time import sleep

from pages.basePage import BasePage 
from resources.config import *

class MainPage(BasePage):
	"""LOCATORS"""
	buttons = {
		"new note button": "//div[contains(@id, 'Sidebar-newNoteButton')]",
		"search button": "//div[contains(@id, 'Sidebar-searchButton')]",
		"notes button": "//div[@id='gwt-debug-Sidebar-notesButton-container']//img",
		"done button": "//button[@id='gwt-debug-NoteAttributes-doneButton']",

		"delete button": "//div[@id='gwt-debug-NoteAttributes-trashButton']",
		"confirm delete button": "//span[@id='gwt-debug-ConfirmationDialog-confirm']"
	}

	dropdowns = {

	}

	radiobuttons = {
		
	}

	fields = {
		"search field": "//input[@id='gwt-debug-searchViewSearchBox']"
	}

	checkboxes = {
		
	}

	other_elements = {
		"note widget": "//div[contains(@class, 'qa-noteWidget')]",
		"note title": "//div[contains(@class, 'qa-title')]"
	}

	def search_note(self, note_name):
		self.click_on("search button")
		self.fill_in("search field", note_name)
		self.find("search field").send_keys(Keys.RETURN)

	def delete_note(self):
		self.click_on("delete button")
		self.click_on("confirm delete button")
		sleep(2)

		
	def open_note(self):
		elements_xpath = self.find_xpath_by_key('note widget')
		elements = self.browser.find_elements_by_xpath(elements_xpath)
		sleep(2)
		elements[0].click()
	