# Coimbra Travels 
<img src="static/images/deployment-images/Screenshot (12).png" alt="amiresponsive" width="900" height="500">


Coimbra Travels is a fully responsive application targeting Coimbra city travellers allowing them to view and create posts of various places in the city.
This application will be useful to the users as they can plan their itinerary to their liking, and/or they can add places that they have visited that are not yet listed in the app so that other users can also plan ahead.


Deployed Link : (https://coimbra-travels.herokuapp.com/)

# UX User Experience

## User Stories

### As a first time user :
1. Be able to see and browse places already logged on the app.
2. Be able to search for existing places and read their specification
3. Be able to register to the app.
4. Be able to add, edit and delete my own posts.

### As a returning user :
1. Log in to my existing account.
2. Log out of my existing account.
3. Be able to access my profile.

### As the Admin user :
1. Be able to manipulate categories, to add, edit and delete them.
2. Ensure that the website is simple and easy to navigate for all users.
3. Make sure that users can log in and log out of their account and have suitable content on their profile
4. Make sure that users can add new content at all times.
5. Providing a secure way of registering.
6. Users have to be able to edit and delete their content at all times whenever they feel like.

# UI User Interface

1. Responsive application on all devices.
2. Two diferent nav bars to provide a better experience and design.
3. Forms to create a new place and form to edit the existing places.
4. Keyword based search bar.
4. Two buttons on Place's card one to edit the other to delete.
5. Registration/Log In forms.
6. Log Out Nav Bar functionality.

# Web Design

I wanted the main theme to be dark with an old feel, as Coimbra is one of the oldest cities in the country with a lot of dark and
medieval stories and look. 
I opted for a black background with a type of typo caligraphy to infuse that feel and aesthetic.
I also made sure the carousel images were black and white and were all images of old and historical buildings.
For the buttons I kept their usual black colour unless if it was a "danger" type button like for example the delete action where I have made them 
red so that they stand out to the user.
The Cards are simple and I have decided to display three in a row as it makes the images bigger and easier to see and the card only displays the catagory,
location, date and it has a title of the place. If users wish to view more they can simply click the caret icon to view its description. This helps the overall
look of the website and makes it more interactive.

# Wireframes

All wireframes were made by hand on paper.


# Features

1. Caroussel: Materialize Caroussel for design and to beautify the web app.
2. Adding a new place: Existing user can add a new place
3. Editing a place: For user to be able to edit a place that they have created.
4. Register: First time user can create an account in order to add new places that they have visited.
5. Delete: Functions and buttons so that users can delete places that they have created.
6. Search Bar: Users can search places by typing Keyword.
7. Security: User validation is checked to see if Username already exists in the database. If so, they will be notified.
In order to make the web page secured passwords are also hashed, meaning they are encripted prior to being stored in the database.

# Future Features

1. Add email to register and reset password feature on log in in case the user has forgotten their password.
2. Add a profile picture option on profile, meaning the user could upload their profile picture from their computer files.

# Technology and Resources Used for this project :

1. HTML5 
2. CSS3
3. JQuery
4. Markdown Lang
5. Git
6. GitHub
7. GitPod
8. Heroku
9. MongoDB
10. Flask
11. Chrome DEV tools
12. Materialize
13. Font Awesome
14. AMiResponsive
15. Youtube
16. Course work and lessons- Code Institute
17. Slack 
18. Google Images
19. Canva 
20. Adobe Sparks
21. StackOverFlow
22. Python
23. Werkzeug



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


# Testing

1. Pep8 - No errors, 2 warnings

<img src="static/images/deployment-images/Screenshot (13).png" alt="screenshot" width="700" height="350">

