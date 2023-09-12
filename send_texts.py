# Download the helper library from https://www.twilio.com/docs/python/install
import os
import math
import argparse
import csv
from twilio.rest import Client
from emoji import emojize


parser = argparse.ArgumentParser(description='Send Account Updates')
parser.add_argument('info_csv', type=str,
                    help='CSV with weekly post and followers for each handle and phone number.')
args = parser.parse_args()


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'YOUR ACCOUNT SID HERE'
auth_token = 'YOUR AUTH TOKEN HERE'
client = Client(account_sid, auth_token)

# You can find a list of your phone numbers at twilio.com/console. Choose one with sms capabilities.
phone = "YOUR PHONE NUMBER HERE +1##########"

info_list = []
average_increase = 0
# read data from info_csv
with open(args.info_csv, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        info_list.append(row)
        average_increase += int(row[3])

        # strip to format phone number
        row[4] = row[4].replace("(", "")
        row[4] = row[4].replace(")", "")
        row[4] = row[4].replace("-", "")
        row[4] = row[4].replace("+", "")
        row[4] = row[4].replace(" ", "")
        row[4] = row[4].strip()

        # remove country code
        if len(row[4]) != 0:
            if row[4][0] == "1":
                row[4] = row[4][1:]

        # special case trailing whitespace
        if len(row[4]) == 11:
            row[4] = row[4][0:10]

        # special case trailing and leading whitespace
        if len(row[4]) == 13:
            row[4] = row[4][1:11]

        # final special case
        if len(row[4]) != 10 and len(row[4]) != 0:
            row[4] = row[4][0:10]

    average_increase = math.floor(average_increase / len(info_list))


for account in info_list:
    # check for valid phone number
    if len(account[4]) != 10:
        print("Invalid phone number")
    elif int(account[2]) >= 4:
        # Post over 4 and ahead of the average
        if int(account[3]) >= average_increase:
            message = client.messages \
                .create(
                    body="\U0001f525\U0001f9ac WEEKLY YAK UPDATE LFG \U0001f9ac\U0001f525 Your account " + account[1] + " had " + account[2] + " posts this week, absurdly top tier! Your followers increased by " +
                    account[3] + ", which was more than the average of " +
                    str(average_increase) +
                    ". You are the epitome of a true grinder, the Yak commends you! \U0001f9ac \U0001f525 \U0001f4c8",
                    from_=phone,
                    to='+1' + account[4]
                )
        # Post over 4 but behind the average
        else:
            message = client.messages \
                .create(
                    body="\U0001f525\U0001f9ac WEEKLY YAK UPDATE LFG \U0001f9ac\U0001f525 Your account " + account[1] + " had " + account[2] + " posts this week, absurdly top tier! Your followers increased by " +
                    account[3] + ", which was below the average of " +
                    str(average_increase) +
                    ". Keep up the grind and get your account \U0001f51b \U0001f51d \U0001f4c8",
                    from_=phone,
                    to='+1' + account[4]
                )
    else:
        # Post under 4 but ahead of the average
        if int(account[3]) >= average_increase:
            message = client.messages \
                .create(
                    body="\U0001f525\U0001f9ac WEEKLY YAK UPDATE LFG \U0001f9ac\U0001f525 Your account " + account[1] + " had " + account[2] + " posts this week, gotta get those numbers up! Your followers increased by " +
                    account[3] + ", which was more than the average of " +
                    str(average_increase) +
                    ". Start flexing more of that content for even more gains \U0001f4aa \U0001f624",
                    from_=phone,
                    to='+1' + account[4]
                )
        # Post under 4 and behind the average
        else:
            message = client.messages \
                .create(
                    body="\U0001f525\U0001f9ac WEEKLY YAK UPDATE LFG \U0001f9ac\U0001f525 Your account " + account[1] + " had " + account[2] + " posts this week, but I know you have what it takes to run it up! Your followers increased by " +
                    account[3] + ", which was below the average of " +
                    str(average_increase) + ". " +
                    account[1] + "\'s game has plenty of room to maximize your potential \U0001f62c Watch what happens once the grind increases \U0001f680 \U0001f4c8 the Yak is rooting for you!",
                    from_=phone,
                    to='+1' + account[4]
                )
