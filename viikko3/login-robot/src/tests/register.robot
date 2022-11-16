*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  uusinimi  salasana321
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  hyvanimi  anananas123
    Output Should Contain  User with username hyvanimi already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  salasana321
    Output Should Contain  Usermane must contain only charachters a-z and be at least 3 letters long

Register With Valid Username And Too Short Password
    Input Credentials  aaa  sala123
    Output Should Contain  Password must must be at least 8 charachters long and contain letters and numbers
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  aaa  salaminaama
    Output Should Contain  Password must must be at least 8 charachters long and contain letters and numbers
*** Keywords ***
Input New Command And Create User
    Create User  hyvanimi  salasana123
    Input New Command
