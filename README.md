
## Problem

We have always been in the situation where we want to play secret santa with our friends and family. The traditional way of randomly getting your santa is by picking out chits. The problem with this approch is that there could be a situation where **a person would get his own name as the santa**, More over because of the secretive behavior of the players after getting there santa names **there is no way of validating the names** after they are picked without breaching the confidentiality of the game.


The following repo contains two possible solutions to secret santa game.

## Solution 1 - login to see your santa 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mdarfan357-sb2.streamlit.app/)
 
In this we use a login page that displays your santa as you login to the site. This is achieved by using Streamlit as a frontend and python and csv as backend of the site. This approch is a little naive as the security is weak, But the program was meant to be run locally on your personal computers. 

When some one signs up to the website there credentials are stored on the database.csv file. the algorithm then uses these names to generate a santa for everyone.

## Solution 2 - sending names by emails 

I have tried to create a program using python that takes in the users and there emails in a csv file and generates vaild santa names everytime using the names in the csv file receivers.csv. Once the names are generated the program validates the names then it starts sending emails to all the receivers using email. 


NOTE : The sender needs to activate an App password for this [link for help](https://support.google.com/mail/answer/185833?hl=en). This is done because the mail is beinging sent from code which is bad according to google in terms of security.    

Create an app password accordingly:
![image](https://user-images.githubusercontent.com/77487906/215283075-7f42c1f4-13b0-44fd-940f-b095526ce609.png)

Change the values for these variables in the mail.py file according to your use case and run the mail.py file to send the mails to all the receivers.
![image](https://user-images.githubusercontent.com/77487906/215283743-4fce9cb6-e65f-4bd0-b5ff-1b63be3cdcd1.png)


I have personally used this program for my personal use case and here is how the output looks like: 
![image](https://user-images.githubusercontent.com/77487906/215284024-98b98153-0480-49df-929c-dd3405617e76.png)

