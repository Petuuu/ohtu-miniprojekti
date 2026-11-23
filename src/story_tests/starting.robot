*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser

*** Test Cases ***
After starting main page loads normally
    Go To  ${HOME_URL}
    Get Title  ==  Reference Manager

After adding a reference it shows on the main page
    Go To  ${HOME_URL}
    Fill field  field_name="key"    field_text=woke
    Fill field  field_name="author"  field_text=Kapteeni
    Fill field  field_name="title"    field_text=KRHK: Johtamisen haasteet modernissa yhteiskunnassa
    Fill field  field_name="journal"    field_text=Helsingin Sanomat
    Fill field  field_name="year"    field_text=2025
    Fill field  field_name="volume"    field_text=21/25
    Fill field  field_name="number"    field_text=1.
    Fill field  field_name="pages"    field_text=1-300
    Fill field  field_name="month"    field_text=""
    Fill field  field_name="note"    field_text=something something liberaalit
    
    Click  id=submit
    Get Text  body  *=   Kapteeni

*** Keywords ***

Fill field
    [Arguments]  ${field_name}  ${field_text}
    Fill Text  [name=${field_name}]  ${field_text}


