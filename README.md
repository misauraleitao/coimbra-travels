# Coimbra Travels <img src="static/images/logo-image/coimbra-travels-logo.png" alt="coimbra-travels-logo" width="50" height="50">


Coimbra Travels is a fully responsive application targeting Coimbra city travellers allowing them to view and create posts of various places in the city.
This application will be useful to the users as they can plan their itinerary to their liking, and/or they can add places that they have visited that are not yet listed in the app so that other users can also plan ahead.




## Deployment to Heroku


Here are the steps that I took to deploy my application to Heroku:

1. First of all, you must `register/login` to deploy the application. I am already a member therefore I simply logged in my details and clicked the button to log in.

<img src="static/images/deployment-images/Screenshot (2)_LI.jpg" alt="screenshot" width="700" height="350">

2. Onced logged in, it took me straight to my apps page and I clicked create new app which took me to the page displayed on the picture bellow. 
It required me to come up with a unique name for my app, for which I named `coimbra-travels`(please note app names should contain lowercase and no spaces) which was available.
I then selected the region section dropdown of `europe` as that is where I am located. I then proceeded to click the `Create app` button to create my application.

<img src="static/images/deployment-images/Screenshot (3)_LI.jpg" alt="screenshot" width="700" height="350">

3. Now in order to connect our app we can choose from one of a few options like, we could connect it through the use of the `Heroku CLI`. However, for this project I chose to simplify the process by setting up an `Automatic Deployment` from my `GitHub Repository`. So, I click the section highlighted in the picture (`connect to GitHub`). I then make sure that I type in my `repository name` correctly and connect to the repo displayed under that.

<img src="static/images/deployment-images/Screenshot (4)_LI.jpg" alt="screenshot" width="700" height="350">

4. To avoid application errors, as I have hidden variables and Heroku will not be able to read them I click to the settings page on the nav bar above and I scroll down to `Reveal Config Vars`. I then writen my config vars to Heroku in a secured maner.(making sure to not include any quotes for the key or value).

<img src="static/images/deployment-images/Screenshot (6).png" alt="screenshot" width="700" height="350">

5. Once we have completed the `Config Vars` we will hide them and go back to the `Deploy` tab, but before I deployed it I made sure to push some files first (`Procfile/requirements.txt`) and I then headed back to the Heroku.


6. I now know that I can safely `Enable Automatic Deployment`, as everything should now be available on my repository.


7. After clicking the enable button I can now go down to `manual deploy` section and click `deploy branch`.

<img src="static/images/deployment-images/Screenshot (8).png" alt="screenshot" width="700" height="350">

8. Heroku will now receive the code from `GitHub` and start building the app using my required packages. After I waited for my app to build I then seen a message displayed `Your app was successfully deployed` and a link button beneath displaying `View`.

<img src="static/images/deployment-images/Screenshot (9).png" alt="screenshot" width="700" height="350">

9. After clicking that I know that my application has been deployed and I can view it. As of now, any coded pushed to GitHub will now automaticly add to my deployed application.
<img src="static/images/deployment-images/Screenshot (10).png" alt="screenshot" width="700" height="350">

