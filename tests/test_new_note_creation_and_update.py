import pytest

from time import sleep

from pages.loginPage import LoginPage
from pages.mainPage import MainPage 
from pages.editor import Editor 
from resources import config
from selenium.webdriver.common.keys import Keys

class TestNewNoteCreation(object):

	note_name = config.note_name
	base_note_name = config.base_note_name
	note_text = config.test_data


	@classmethod
	def setup_class(cls):
		cls.login_page = LoginPage()
		cls.main_page = MainPage()
		cls.editor = Editor()
		cls.login_page.open_url()
		cls.login_page.login()


	@classmethod
	def teardown_class(cls):
		cls.main_page.delete_note()
		sleep(2)
		cls.login_page.browser.close()

	def test_new_note_creation(self):
		self.main_page.click_on("new note button")
		self.editor.fill_in("title field", self.base_note_name)
		sleep(2)
		self.editor.enter_note_text(self.note_text)
		self.main_page.click_on("done button")

		assert self.editor.get_note_text() == self.note_text
		
	def test_note_title_update(self):
		self.main_page.open_new_tab()
		self.main_page.open_url()
		sleep(5)
		self.editor.fill_in("title field", self.note_name)
		self.main_page.click_on("notes button")
		self.main_page.switch_to_another_tab()
		self.main_page.click_on("notes button")
	
		assert self.editor.get_note_title() == self.note_name

