# web_app

## Problem

We have always been in the situation where we want to play secret santa with our friends and family. The traditional way of randomly getting your santa is by picking out chits. The problem with this approch is that there could be a situation where **a person would get his own name as the santa**, More over because of the secretive behavior of the players after getting there santa names **there is no way of validating the names** after they are picked without breaching the confidentiality of the game.


The following repo contains two possible solutions to secret santa game.

## Solution 1 - login to see your santa 
 
In this we use a login page that displays your santa as you login to the site. This is achieved by using Streamlit as a frontend and python and csv as backend of the site. This approch is a little naive as the security is weak, But the program was meant to be run locally on your personal computers. 

When some one signs up to the website there credentials are stored on the database.csv file. the algorithm then uses these names to generate a santa for everyone.

## Solution 2 - sending names by emails 

I have tried to create a program that takes in the number of users

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mdarfan357-sb2.streamlit.app/)
