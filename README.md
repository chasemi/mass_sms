# mass_sms

# Description

The mass_sms repo contains the send_texts python program and an example csv file. send_texts takes as an argument a csv file with the information needed for the message. The program determines whether an account reached the goal of 4 posts for that week and how their follower increase compares to the average increase across all accounts that week. The message is chosen based off of these two metrics and sent to the managers listed contact number using the twilio api. 

# Setup

- Clone this repo
  
- Import CSV to the repository containing the following information
    - Format CSV with the headers: **Analytics Name, Username, This Weeks Posts, This Weeks Followers, Phone Number**
    | Analytics Name | Username | This Weeks Posts | This Weeks Followers | Phone Number |
    - the phone number can be formatted in any typical fashion, but the raw string of ten characters is best: ##########
      
- Set the following variables with the information found at [twilio.com/console](http://twilio.com/console). Note that you must be invited by an admin for these credentials to authenticate.
    - account_sid = 'YOUR ACCOUNT SID HERE'
    - auth_token = 'YOUR AUTH TOKEN HERE'
    - phone = "YOUR PHONE NUMBER HERE”

# Run Program

- Run send_texts.py with the name of the csv file as an argument
    - >> python3 send_texts.py info_list.csv

# Troubleshooting

- To check the status of your message can navigate to [twilio.com/console](http://twilio.com/console) >> monitor >> logs >> messaging
- [Debugging Common Issues](https://www.twilio.com/docs/sms/troubleshooting/debugging-common-issues) is a great resource for troubleshooting
