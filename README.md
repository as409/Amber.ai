## Amber.ai
Your personal concierge

# NLU engine + bot builder platform + Telegram

This api.ai agent will be used along with a bot builder platform and a messenger like telegram

![yo](https://user-images.githubusercontent.com/17767383/30829356-6b47a568-a1f5-11e7-8f36-8a5d5934788a.png)


![selection_045](https://user-images.githubusercontent.com/17767383/28778124-9d2a280e-761b-11e7-9f89-6cbcee6c12cd.png)

![selection_046](https://user-images.githubusercontent.com/17767383/28778138-ab806512-761b-11e7-840e-16833296becf.png)

## Setup :

### 1. Setting up NLU engine
- Create account and import the NLU engine module as a .zip file
- Create a secret customer token

### 2. Setting up the Bot builder
- Create account and import the Bot builder module as a .zip file
- Go to Heading.yaml component -> intent -> api.ai
    - Now paste the api.ai customer token 
    - select language 'en'
    - priority '30'
- Connect with the messaging service of your choice 

Many messaging platforms don't support cards display and other rich media contents, please read the documentation.
