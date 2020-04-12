from selenium import webdriver
import os
import sys
import time

browser = webdriver.Chrome("/home/rahul/Desktop/DevFest/drivers/chromedriver")
browser.get("https://github.com/")

ReqName = str(sys.argv[1])
RepoName = str(sys.argv[2])

browser.get("https://github.com/"+ReqName)

browser.get("https://github.com/"+ReqName+"/"+RepoName)