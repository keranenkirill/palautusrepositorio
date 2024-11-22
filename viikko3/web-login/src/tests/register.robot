*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
   Set Username  aapo
   Set Password  aapo1234
   Set Password Confirmation  aapo1234
   Submit Registration
   Register Should Succeed


Register With Too Short Username And Valid Password
   Set Username  aa
   Set Password  aapo1234
   Set Password Confirmation  aapo1234
   Submit Registration
   Register Should Fail With Message  Username must be at least 3 characters long


Register With Valid Username And Too Short Password
   Set Username  aapo
   Set Password  aa
   Set Password Confirmation  aa
   Submit Registration
   Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
   Set Username  aapo
   Set Password  qwertyuio
   Set Password Confirmation  qwertyuio
   Submit Registration
   Register Should Fail With Message  Password must not be only letters

Register With Nonmatching Password And Password Confirmation
   Set Username  aapo
   Set Password  aapo1234
   Set Password Confirmation  aapo4321
   Submit Registration
   Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
   Set Username  kalle
   Set Password  aapo1234
   Set Password Confirmation  aapo1234
   Submit Registration
   Register Should Fail With Message  Username is already in use

*** Keywords ***
Register Should Succeed
   Welcome Page Should Be Open

Register Should Fail With Message
   [Arguments]  ${message}
   Register Page Should Be Open
   Page Should Contain  ${message}

Set Username
   [Arguments]  ${username}
   Input Text  username  ${username}

Set Password
   [Arguments]  ${password}
   Input Password  password  ${password}

Set Password Confirmation
   [Arguments]  ${password_confirmation}
   Input Password  password_confirmation  ${password_confirmation}

Submit Registration
   Click Button  Register


*** Keywords ***
Reset Application Create User And Go To Register Page
   Reset Application
   Create User  kalle  kalle1234
   Go To Register Page