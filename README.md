## Amber.ai
Your personal concierge

# NLU engine + bot builder platform + Telegram

This NLP agent will be used along with a bot builder platform and a messenger like telegram

![yo1](https://user-images.githubusercontent.com/17767383/30844391-b1b29488-a243-11e7-8f7d-c1d35c02a31e.png)


![selection_045](https://user-images.githubusercontent.com/17767383/28778124-9d2a280e-761b-11e7-9f89-6cbcee6c12cd.png)

![selection_046](https://user-images.githubusercontent.com/17767383/28778138-ab806512-761b-11e7-840e-16833296becf.png)

## Setup :

### 1. Setting up NLU engine
- Create account and import the NLU engine module as a .zip file
- Create a secret customer token

### 2. Setting up the Bot builder
- Create account and import the Bot builder module as a .zip file
- Go to Heading.yaml component -> intent -> NLP instance
    - Now paste the NLP instance customer token 
    - select language 'en'
    - priority '30'
- Connect with the messaging service of your choice 

Many messaging platforms don't support cards display and other rich media contents, please read the documentation.

