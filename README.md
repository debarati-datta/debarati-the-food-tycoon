<h1 align="center">Debarati-The Food Tycoon</h1>

[View the live project here.](https://debarati-the-food-tycoon.herokuapp.com/)

**This is the website for a recipe collection of basic indian regional favourites. Anyone can become a user and add to the collection.**

## Debarati - The Food Tycoon - Introduction

### The idea stems from looking at the the popularity of indian curries and creating a platform for people to add their own recipes. Many dishes with the same name and basic ingedients are cooked in slightly different ways in different parts of India and in order to accomodates this variety, the website has catagories representing different states of the country. 

## User Experience (UX)

### User stories

- ### User 1 : I want to understand in one quick glace the purpose of the site

 1. The callout section clearly spells out the purpose of the site.![image](https://user-images.githubusercontent.com/66360068/112591232-f912d200-8dfb-11eb-93b9-f4f93678fe7e.png)
 2. Also the very first paragraph on the home page describes the purpose of the website. ![image](https://user-images.githubusercontent.com/66360068/112591385-2fe8e800-8dfc-11eb-8670-05f40c6e6021.png)


- ### User 2 : I want to navigate with ease and find thing easily

 1. The user is greeted with a clean and easily readable navigation bar that allows you to go to the page of your choice. 
 2. The most relevant information is immediately available with the 'Recipes' and 'New Recipe' sections on the home page.
 ![image](https://user-images.githubusercontent.com/66360068/112591937-05e3f580-8dfd-11eb-9d28-4cfa342e0fb6.png)
![image](https://user-images.githubusercontent.com/66360068/112591989-214f0080-8dfd-11eb-9032-15696781ef1c.png)
 
 - ### User 3 : I want to add my own recipes and have them sit in the database with my name on it

1. The add recipe tab opens up a form that takes in your input in a certain format. 
2. Upon submission, the recipe gets stored in the database with your initials displaying. It also allows you to amend and delete your own recipe when you log in with the same credentials as you used while creating the recipe.
![image](https://user-images.githubusercontent.com/66360068/113972396-785bc900-9832-11eb-8a9e-dc73ecb43f8e.png)


- ### User 4 : I want to add my own recipe as a video

1. The add recipe section allows you to add a video link. This can be your own video or something available on youtube. 
![image](https://user-images.githubusercontent.com/66360068/113972507-9fb29600-9832-11eb-891c-ecb7ceac2ccf.png)



### Site owner goals

### Goal 1 : To offer a visually appealing page to get people interested in the recipes

 1. The home page offers a beautiful banner with indian spices displayed
 2. The home page also shows a lot of recipes with a search function at the top which will only get better with time and more and more people contributing recipes.
 
 ### Goal 2 : To offer some interactive elements so the user stays longer on the site that results in adding more recipes to the page

1. The "Add Recipe" page allows people to add their own recipes and upon submitting also flashes a "success" message
2. The "Edit" button on the home page allows users to later add or delete their own content what they previously entered which makes the site quite interactive.



## Features

1. The website feature of adding, editing and deleting your own recipes makes it easy for the user to own the idea and keep coming back to it.

2. The feature of adding a video link to the recipe allows users to create their very own video clip and using it for their recipe via youtube


## New Features to be implemented in future

Ideally, I would like to add quite a few features to it namely :

1. The option to like/love others recipes and add comments for each recipe. that will truly make it a very interactive website which members would love.

2. The option to add more info about each member so the users can connect with other users more on a one to one basis to exchange ideas on cooking


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Wireframes

1. The home page for desktop
 - [wireframe for home page](https://user-images.githubusercontent.com/66360068/116749462-e3935800-a9f8-11eb-8a2e-ba18594f7f58.png)
 
2. The manage catagories page
 - [wireframe for manage catagories page](https://user-images.githubusercontent.com/66360068/116749770-56043800-a9f9-11eb-89a8-741600b58e05.png)


### Frameworks, Libraries, Tutorials & Programs Used

1. [Materialize](https://materializecss.com/getting-started.html)
    - Materialise is used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on various buttons to add the float transition while being hovered over.
1. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [youtube:](https://www.youtube.com/)
    - youtube videos of various recipes have been added by the siteowner and other users
1. [w3schools:](https://www.w3schools.com/)
    - w3school tutorial are used to understand various python functions
1. [stack-overflow:](https://stackoverflow.com/)
    - Stack Overflow is used to get answers to various whys and hows
1. [Google](https://www.google.org/)
    - Some recipe descriptions have been taken from material available over the internet

## Testing

The W3C Markup Validator, W3C CSS Validator and JSHint Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input) - Throws up errors due to usage of jinja templating language which is expected
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results]![image](https://user-images.githubusercontent.com/66360068/118509651-23ac4780-b728-11eb-9c0c-796d992ede79.png)
-   [JSHint](https://jshint.com) 
              1. [Result : App]![image](https://user-images.githubusercontent.com/66360068/118510102-8d2c5600-b728-11eb-8644-1e57d5ad386a.png)
              2. [Result : Script]![image](https://user-images.githubusercontent.com/66360068/118510351-cbc21080-b728-11eb-8d82-9fde2042c1d0.png)


### Further Testing
**Browser testing**

-   The Website was tested on Google Chrome, Microsoft Edge and Safari browsers. 5 differnt users registered from a different country and added recipes. They described the experience to be smooth.

**Device testing**
-   The website was viewed on a variety of devices such as Desktop, Laptop, Samsung Galaxy Note9, iPhone 8 & iPhoneX.
-   A good amount of testing was done to ensure that all pages were linking correctly.


**New Recipe Form: Testing**
1.  Go to the "New Recipe" page
2.  Try to submit the empty form - a prompt message about the required fields appears.
3.  Try to submit the form with any empty field - a prompt message appears.


**Backend Mongo DB entry Testing**
*Each entry directly on Mongo DB collections page can be immediately seen on the site *
-   [Mongo DB entry]![image](https://user-images.githubusercontent.com/66360068/118511461-d204bc80-b729-11eb-8bce-e0ea55ea8aac.png)
-   [visibility on site]![image](https://user-images.githubusercontent.com/66360068/118511582-f52f6c00-b729-11eb-8c48-d96b9935d527.png)


## Learnings

-   I enjoyed learning Python and have tried to access other material available on the internet to support my learning. Python is easier to learn as it has clean syntax. Although I have only just studied a web framework but I am quite aware of the numerous third-party modules contained in PyPI that makes Python capable of interacting with many other language platforms. The jinja templating language and the template inheritance that I learnt is immensely helpful to make multi page websites without having to change code on each page constantly. 

-   I added the defensive programming on my own. When a user hits the delete button, a flash message appears asking the user to confirm deletion. I am quite proud of it. Here is a [screenshot]![image](https://user-images.githubusercontent.com/66360068/118802805-7e65b080-b89a-11eb-80c4-4ff63480aba7.png)


## Limitations

-   The profile Page is not useful at the moment. It can be made better by having a lot of information about the member in terms of their specific food interests, some food hacks that they tried which they want to share, some provision for pictures of their own recipes etc. All of this can make a user profile a lot more interesting and the site more interactive.
-   

## Deployment

### Heroku

**The project was deployed to Heroku using the following steps**

1. Download Heroku. Register and create an account. 
2. Under personal tab, create a new app and give it the same name as your project on github. ![image](https://user-images.githubusercontent.com/66360068/121634560-af419b80-ca7c-11eb-9198-75dd66060cbc.png)
3. Under settings tab, reveal the config vars and add those to your project's env.py file and choose the app owner by providing your email id.![image](https://user-images.githubusercontent.com/66360068/121634690-f16add00-ca7c-11eb-85dc-26111a5f4dd8.png)
4. Under the delopy tab, connect to github and enable automatic deploys. Choose the master branch to deploy. ![image](https://user-images.githubusercontent.com/66360068/121634839-2f680100-ca7d-11eb-9cf9-904e51014e1f.png)
5. Wait for it to connect while the final url is being created. Find the link under settings tab. ![image](https://user-images.githubusercontent.com/66360068/121635190-ba48fb80-ca7d-11eb-8534-7935ebc56ac6.png)
6. Click the final link to see your app running.


**Issues tab on github was used to generate screenshot links to use in the ReadMe file**

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Issues" button next to "Code" button on the menu.
3. Click the green button on right saying "New issue"
4. In the comment box, paste your screenshot link - it will generate a url
5. Paste it in the ReadMe file for reference


## Sources
### This project is inspired by 

- The task manager mini project(Code Institute) - The entire design and pages


### Content

-   Remaining content(recipes) is written by the developer and other users of the app.

### Media

-   The hero Image is obtained from the internet and renamed.

### Acknowledgements

-   I thanks my Mentor, tutor support and slack community for continuous helpful feedback. 

