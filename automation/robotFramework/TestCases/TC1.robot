*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Test Cases ***
GoogleTest
    #create webdriver  chrome    executable_path="C:\drivers\chromedriver.exe"
    open browser    http://www.google.com   chrome
    input text  name:q  test
    click element   id:gsr

*** Keywords ***
