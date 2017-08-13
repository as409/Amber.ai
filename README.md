## Travel_Bot
A chat bot to book flight, hotel, cabs etc

# Meya.ai + api.ai + applozic/intercom
This api.ai agent will be used along with #Meya.ai and a messaging platform like intercom, Zendesk or applozic

![tom](https://user-images.githubusercontent.com/17767383/29006341-4f70fba2-7b0b-11e7-9f44-30ada160a471.png)

![selection_045](https://user-images.githubusercontent.com/17767383/28778124-9d2a280e-761b-11e7-9f89-6cbcee6c12cd.png)

![selection_046](https://user-images.githubusercontent.com/17767383/28778138-ab806512-761b-11e7-840e-16833296becf.png)

## Setup :

### 1. Setting up api.ai
- Create an api.ai account and import the api.ai module as a .zip file
- Create a secret customer token

### 2. Setting up meya.ai
- Create a meya account and import the meya module as a .zip file
- Go to Heading.yaml component -> intent -> api.ai
    - Now paste the api.ai customer token 
    - select language 'en'
    - priority '30'
- Connect with the messaging service of your choice (I have testesd this with applozic and meya web)

Many messaging platforms don't support cards display and other rich media contents, please read the meya documentation.

