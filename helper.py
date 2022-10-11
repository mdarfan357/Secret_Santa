import streamlit as st
from csv import writer
import pandas as pd
import time
import random 



def create_csv():
    
    with open("database.csv",'w',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow(['First Name',"Last Name","Email","Phone No.","User Name","Password"])  
    return True

def append_to_csv(FName,LName,Email,PNo,Uname,Pass):
    with open("database.csv",'a',encoding="utf8",newline="") as f:
        mywriter = writer(f)
        mywriter.writerow([FName,LName,Email,PNo,Uname,Pass])
        f.close()
    return True  
