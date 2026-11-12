*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
After starting main page loads normally
    Go To  ${HOME_URL}
    Get Title  ==  Miniprojekti
    Get Text  body  *=  Hello World!
