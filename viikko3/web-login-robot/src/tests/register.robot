*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page First

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nimi
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail With Message  Usermane must contain only charachters a-z and be at least 3 letters long

Register With Valid Username And Too Short Password
    Set Username  aaa
    Set Password  s
    Set Password Confirmation  s
    Submit Credentials
    Register Should Fail With Message  Password must must be at least 8 charachters long and contain letters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  aaa
    Set Password  salasana123
    Set Password Confirmation  naamasalama666
    Submit Credentials
    Register Should Fail With Message  Please enter the same password twice

Login After Successful Registration
    Set Username  uusinimi
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Logout And Go To Login Page
    Set Username  uusinimi
    Set Password  salasana123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  u
    Set Password  s
    Set Password Confirmation  s
    Submit Credentials
    Logout And Go To Login Page
    Set Username  u
    Set Password  s
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Go To Register Page First
    Go To Register Page

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login
Logout And Go To Login Page
    Go To Login Page
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}