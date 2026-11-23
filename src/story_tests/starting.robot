*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Go To  ${HOME_URL}

*** Variables ***
${AUTHOR}   Kapteeni
${JOURNAL}  HS
${YEAR}     2025

*** Test Cases ***
After starting main page loads normally
    Get Title  ==  Reference Manager

After adding a reference it shows on the main page
    Add Reference
    ...    key=woke
    ...    title=KRHK: Johtamisen haasteet modernissa yhteiskunnassa
    Get Text  body  *=  Kapteeni
    
After deleting a reference it disappears from the main page
    Add Reference  key=delete_this  title=Delete Me
    Handle Future Dialogs  action=accept
    Click  css=h3:has-text("Delete Me") ~ form button
    ${body}=  Get Text  body
    Should Not Contain  ${body}  Delete Me

*** Keywords ***
Add Reference
    [Arguments]    ${key}    ${title}
    ...            ${author}=${AUTHOR}
    ...            ${journal}=${JOURNAL}
    ...            ${year}=${YEAR}
    Fill Field    key      ${key}
    Fill Field    author   ${author}
    Fill Field    title    ${title}
    Fill Field    journal  ${journal}
    Fill Field    year     ${year}
    Click  id=submit

Fill field
    [Arguments]  ${field_name}  ${field_text}
    Fill Text  [name=${field_name}]  ${field_text}


