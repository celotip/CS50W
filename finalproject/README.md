# Food Ordering Web App in Restaurants - AntaResto
#### Video Demo:  <https://youtu.be/Aue8bPhJDsY>

## Distinctiveness and Complexity
I think that this project is fairly distinct and more complex than all the projects in CS50W course because I have added a few features that is not taught in this course:
1. The concept of ordering food in a restaurant itself is distinct from all the projects in CS50W
1. The usage of localstorage to store, get, and remove various items
1. User expiry time along with usage of middleware.py to check if the time has passed the expiry
1. Usage of ngrok to allow other users than the localhost to use my web app, including smartphone users
1. Usage of cards and progress bar in bootstrap
1. The back button
1. usage of UserAdmin to make a user in the admin page with hashed password
1. The item.html itself is fairly complex considering the amount of script needed to be written.
1. CSS is also quite complex. Involves layering (z-index), and vertical and horizonatal alignment


## What’s contained in each file created
1. Layout.html: The back button can be seen in layout.html 
1. Index.html: Shows the homepage. Pretty straightforward, only shows the logo, and two buttons
1. The first button (Order now) will take you to the login page if not logged in. If logged in, it will take you to menu.html. This page will show you the pictures and names of categories excluding the exclude_list in views.py. There will also be a check button in each card that will take you to that category. At the top of the page, the table no., and the last order time is shown. Table no. can be set with the django admin page, whereas the last order time has a default value of 30 mins after the user is created. After the expiry time, the user has no longer access to any of the page except the homepage and will be redirected to expired.html
1. Menu_ext.html: Once you press the check button you will go to menu_ext.html. You can see each item in the category that you chose. In each item, a picture, title, description, and price is shown in a card. You ca press the plus button to choose that item. 
1. Item.html: Allows user to select their drinks (and soup). The layout will be different if the soup is not selectable. A progress bar will be shown at the top of the page. If the user selects an option with an additional price (not Rp. 0), the price will be added in the checkout page. At the bottom of the page there is a counter, which represents the quantity of order, which you can choose to increase or decrease. The price will change accordingly. Once you press continue, you will go to the checkout page. Here, you are shown the items in which you have chosen to add. You can either go back and edit your order or you can proceed to checkout. Once you checkout, and order object will be created and you can view it in the history.html page which is accessible through the "Order history" button.
1. History.html: Here, you can see all the orders you have made along with the total price.
1. Static folder: contains styles.css and options.js (javascript file for menu_ext.html). The script in checkout.html and item.html are not made into seperate files because jinja is needed.
1. Settings.py was editted to allow ngrok to be used (added ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS). I also added "resto.middleware.AccountExpiry" in MIDDLEWARE to check if the time has passed the user's expiry time. I also changed the TIME_ZONE for this feature to work properly.
1. admin.py was editted to allow admin to view orders properly and also create users (with username and password) and edit their table_no.
1. models.py: added 4 models
1. urls.py: added 10 urls
1. views.py contains the views functions for each url

## How to run application
To run this application, you can either use python manage.py runserver to run it in the localhost, or use ngrok http 8000, to run it using ngrok in port 8000. Then, you need to add the link provided by ngrok in the allowed hosts and csrf trusted origins in the settings.py. If you don't have a user yet, you need to login to the admin page by creating your own superuser (python manage.py createsuperuser) and add a user from the admin page. Then, change the table_no of the user you created. To view all orders, you can do so in the admin page.

## Additional information
For this application to run properly, the timezone needs to be set correctly. Otherwise, your account may be considered expired.
