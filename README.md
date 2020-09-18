# BITCOIN_PRICE_NOTIFICATIONS #

## About the project
This project regarding a Bitcoin_Price_notifications with 2 applets and a HTTP requests module and define the webhook URL variable. Now we just have to send an HTTP POST request to the IFTTT webhook URL using the requests.post() function.

### we're going to create two IFTTT applets:

* one for emergency notification when Bitcoin_Price falls under a certain threshold; and. 

* another for regular Telegram updates on the Bitcoin price.

# an IFTTT applet is composed to two parts:

* a trigger
* an action
### Creating IFTTT Applets:

* Now we’re finally ready for the main part. Before starting with the code we need to create two new IFTTT applets: one for emergency Bitcoin price notifications and one for regular updates.

* Now that we have IFTTT out of the way, let’s start coding! You’ll start by creating the standard Python command-prompt. Take this code and save it in a file called bitcoin_notifications.py

### Both will be triggered by our Python app which will consume the data from the Coinmarketcap API.

## About the code
The code for this project is written by using python 3.8. So we should have to make sure installed python 3.8 in our pc to run this code alnog with the pip requests .

## Functions
* We can create test IFTTT notification and install their mobile app.

* check whether the notifications are working and later implement the code


* next we create an emergency Bitcon_Price notifications for the app notifications

* Check the status of the notifiactions whether they are receiving in the app or not.

* next create an telegram notifactions applet to know the Bitcoin_Price in the Telegram bot app for regular price notifications.

## How to run? 
This code can be run in two modes
* interactive ( We can give required input manually )
* File mode: It can also run by accepting the file which is containing inputs. 

## Interactive mode

To choose Interactive mode just we need to type ' Interactive '. So that it will ask you the input ( requirements ). 

### Commands to get an output
We can use the following commands in Interactive mode to geet an out.

* create Bitcoin_Price_notifications < NUMBER OF NOTIFICATIONS> It will create the price notifications with no.of required actions.


* applets<creating webhooks><creating the link with HTTP POST requests> <connecting to the apps > <creating the api url > <and excuting in terminal> <and getting the code run>

<An important thing is to avoid sending out these requests too frequently, for two reasons:

* the Coinmarketcap API states that they update the data only once every 5 minutes, so there’s no point in reloading the latest pricing info more frequently than that

* if your app sends too many requests to the Coinmarketcap API your IP might get banned or temporarily suspended.



## File mode

It accepts a filename(bitcoin_notifications.py) as a parameter at the terminal and read the commands from the file.
 
* open command prompt on your pc.
* then copy the file path where the py file is located in ur pc
* and add paste it in the CMD then open the py file.
* then write the py file name to excute the code then 
* then the code excutes and ask the confirmations for excuting and getting the no.of required notifications

* In this, we created our very own Bitcoin notification service. You learned how to send HTTP GET and POST requests using the requests package. You saw how easy it was to connect your Python app to external services using IFTTT and webhooks.


# Thank you              


