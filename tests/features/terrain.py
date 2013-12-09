from lettuce import *
from selenium import webdriver

@before.each_scenario
def start_webdriver(scenario):
    world.driver = webdriver.Firefox()

@after.each_scenario
def quit_webdriver(scenario):
    world.driver.quit()
