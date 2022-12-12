<div align="center">
  <img src="https://media.giphy.com/media/L2kr3y97uJauF6T6Lh/giphy.gif" width="100"/>
</div>

<h1><img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>Ecommerce Application</h1>

<h4>A Full stack ecommerce application made using quasar 2 for frontend and django rest framework for backend. The application is coupled with [auth-application](https://github.com/Abdul-Mueed-Shahbaz/Auth-Application) for login and jwt token authentication.</h4>



#
### How to couple the authentication application with another
* You can configure the app to be coupled by another app for authentication by adding the required information in COUPLED_APPS object in app.js
* The Coupled application's required information includes the application name, Icon's name to be displayed(Place the app icon in assets/icons) and the url of the application to be verified
* The jwt token recieved on successful authentication includes the user's email and id present in the login app's database. The coupled app needs to be configured in such a way that the token should be included in the HTTP request's header or cookie with the key of auth_token. The backend of the coupled app needs to implement the appropirate authentication mechanism to check the availibity/validity of the token
#

 Main Features</h2>

* Complete input fields validation(Frontend)
* Input fields can easily be modified/added by changing the concerned objects in reactive.js file
* Completely responsive
* State managed properly using vuex
* Proper error handling
* The auth app redirects to the coupled app along with the auth_token property with the value of jwt token in the query string
* The application uses mysql as the database

#




### Technologies used

<div style="display:flex">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" />
<img src="https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white" />
<img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D" />
 
![Quasar](https://img.shields.io/badge/Quasar-16B7FB?style=for-the-badge&logo=quasar&logoColor=black)![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  
</div>

#
<h2><img  width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0115.gif" border="0" alt="animated-television-image-0115" />
  Screenshots</h2>

![Home](https://user-images.githubusercontent.com/52679916/207143514-df94da04-a394-4960-9990-a49942889cd8.png)
![summer](https://user-images.githubusercontent.com/52679916/207143677-15f60563-80b4-480d-a094-586697e2730c.png)
![Winter](https://user-images.githubusercontent.com/52679916/207143688-48a67dfb-a47f-43b4-b4af-242fd84a20d5.png)
![ProductDetails](https://user-images.githubusercontent.com/52679916/207143624-13513a4a-2717-45c3-810a-7bfb6578c4d8.png)
![AccountDetails](https://user-images.githubusercontent.com/52679916/207143392-8cf216ac-c119-41b1-9de0-f33f2db901c1.png)
![Notifications](https://user-images.githubusercontent.com/52679916/207143556-7504b5c2-5e44-4869-8138-ea71f3af62b2.png)
![ErrorHandling](https://user-images.githubusercontent.com/52679916/207143501-12f5deb1-81c0-4fbb-aa26-6baf37fb8ddb.png)
![loginWithAuthApplication](https://user-images.githubusercontent.com/52679916/207143548-6a925a9f-e4a6-4082-ba18-09d1a3e98fbc.png)
![Cart](https://user-images.githubusercontent.com/52679916/207143476-2587bc15-ccf9-40b7-be99-d04647310322.png)
![Checkout](https://user-images.githubusercontent.com/52679916/207143485-048a50e6-ddf4-48d7-b57c-c49ff39ea3a5.png)

<h2><img width="30px" src="https://www.animatedimages.org/data/media/491/animated-television-image-0134.gif" border="0" alt="animated-television-image-0134" />


<h2><img width="30px" src="https://www.animatedimages.org/data/media/318/animated-computer-smiley-image-0080.gif" border="0" alt="animated-computer-smiley-image-0080" />  Commands:</h2>

##
Install the dependencies
(FrontEnd/gui)
```bash
yarn
# or
npm install
```
(BackEnd/api)
```
# Create virtual env by executing the setup.bat in the build folder
# Activate the venv by using the activate file in the build-env/scripts folder
# After completing the above mentioned steps
# Install the required packages by executing the following command
pip install -r .\requirements\bast.txt 
# Change the settings file if you want to change the database related information
# Use the manage.py file and execute the following commands to apply required migrations
python manage.py makemigrations 
python manage.py migrate
```

### Start the app in development mode (hot-code reloading, error reporting, etc.)
```bash
quasar dev
```
### To start the server
```
python manage.py runserver 8000
```

### Lint the files
```bash
yarn lint
# or
npm run lint
```



### Build the app for production
```bash
quasar build
```

### Customize the configuration
See [Configuring quasar.config.js](https://v2.quasar.dev/quasar-cli-webpack/quasar-config-js).

