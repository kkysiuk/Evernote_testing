from selenium import webdriver

class Wrapper(object):

	_instance = None	

	def __new__(cls, *args, **kwargs):
		"""Singleton pattern"""
		if not cls._instance:
			cls._instance = super(Wrapper, cls).__new__(cls, *args, **kwargs)
			cls.browser = webdriver.Firefox()
			#cls.browser.maximize_window()
		return cls.browser

	def close(cls):
		cls.browser.close()



