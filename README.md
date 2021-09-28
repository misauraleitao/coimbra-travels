# Coimbra Travels 




## Deployment to Heroku


Here are the steps that I took to deploy my application to Heroku:

1. First of all, you must `register/login` to deploy the application. I am already a member therefore I simply logged in my details and clicked the button to log in.
2. Onced logged in, it took me straight to my apps page and I clicked create new app which took me to the page displayed on the picture bellow. 
It required me to come up with a unique name for my app, for which I named `coimbra-travels`(please note app names should contain lowercase and no spaces) which was available.
I then selected the region section dropdown of `europe` as that is where I am located. I then proceeded to click the `Create app` button to create my application.
3. Now in order to connect our app we can choose from one of a few options like, we could connect it through the use of the `Heroku CLI`. However, for this project I chose to simplify the process by setting up an `Automatic Deployment` from my `GitHub Repository`. So, I click the section highlighted in the picture (`connect to GitHub`). I then make sure that I type in my `repository name` correctly and connect to the repo displayed under that.
4. To avoid application errors, as I have hidden variables and Heroku will not be able to read them I click to the settings page on the nav bar above and I scroll down to `Reveal Config Vars`. I then writen my config vars to Heroku in a secured maner.(making sure to not include any quotes for the key or value).
5. Once we have completed the `Config Vars` we will hide them and go back to the `Deploy` tab, but before I deployed it I made sure to push some files first

