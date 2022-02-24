import bs4
import requests as req
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_hospital_info():  # Gets the information to be displayed to the chat people
    global hospital_names, general_beds, oxygen_beds, phone_number
    main_code = req.get(
        "https://covidhelplinebangalore.com/covid-19-beds-availability/"
    )
    soup = bs4.BeautifulSoup(main_code.text, "lxml")
    table_rows = soup.select("tr")
    hospital_names = []
    general_beds = []
    oxygen_beds = []
    phone_number = []
    for i in range(3, len(table_rows) - 1):
        text = table_rows[i].getText()
        table_list = text.splitlines()
        hospital_names += table_list[2]
        general_beds += table_list[4]
        oxygen_beds += table_list[5]
        phone_number += table_list[7]


def set_browser():  # Open a chrome driver where the whatsapp conversation takes place
    global whatsapp
    whatsapp = webdriver.Chrome(
        executable_path=r"C:\Users\sidli\Desktop\Python\Whatsapp Chatbot\chromedriver.exe"
    )


def open_whatsapp():  # Opens Whatsapp in the automated chromedriver
    whatsapp.get(r"https://web.whatsapp.com/")


def response():  # Logic for the response selection. Will take input from the user and send messages depending the sector.
    sec = True
    sector = msg[-1]
    while sec == True:  # Loop to check for typing errors
        if sector == "R R Nagar":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThe closest hospital to you is {hospital_names[0]}.\nThere are {general_beds[0]} general beds and {oxygen_beds[0]} oxygen_beds available.\nTo book an appointment please call this number - {phone_number[0]}.\nFor directions please open the following link - https://goo.gl/maps/5bRVSq7BqUqeZShZ8."
                + Keys.ENTER
            )
            sec = False
        elif sector == "Yelahamka":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThere are two hospitals close to you:\n{hospital_names[1]}.There are:\n1) {general_beds[1]} general beds and {oxygen_beds[1]} oxygen_beds available.\nTo book an appointment here please call - {phone_number[1]}.\nFor directions please open the following link - https://goo.gl/maps/HKtXUcMvquUvg87m9.\n\n2) {hospital_names[10]}.\nThere are {general_beds[10]} general beds and {oxygen_beds[10]} oxygen_beds available\nTo book an appointment here please call - {phone_number[10]}.\nFor directions please open the following link - https://goo.gl/maps/gm75w1EVEqzddEVa6."
                + Keys.ENTER
            )
            sec = False
        elif sector == "Daasarahalli":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThe closest hospital to you is {hospital_names[2]}.\nThere are {general_beds[2]} general beds and {oxygen_beds[2]} oxygen_beds available.\nTo book an appointment here please call - {phone_number[1]}.\nFor directions please open the following link - https://goo.gl/maps/yL1J6xiEtVcx17HA9."
                + Keys.ENTER
            )
            sec = False
        elif sector == "East":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThere are two hospitals close to you:\n{hospital_names[3]}.There are:\n1) {general_beds[3]} general beds and {oxygen_beds[3]} oxygen_beds available.\nTo book an appointment here please call - {phone_number[3]}.\nFor directions please open the following link - https://goo.gl/maps/sJ7EsGqtFjLdxqdt5.\n\n2) {hospital_names[4]}.\nThere are {general_beds[4]} general beds and {oxygen_beds[4]} oxygen_beds available\nTo book an appointment here please call - {phone_number[4]}.\nFor directions please open the following link - https://goo.gl/maps/e4JxxUr8kZvn5jch9."
                + Keys.ENTER
            )
            sec = False
        elif sector == "Mahadeva Pura":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThere are two hospitals close to you:\n{hospital_names[5]}.There are:\n1) {general_beds[5]} general beds and {oxygen_beds[5]} oxygen_beds available.\nTo book an appointment here please call - {phone_number[5]}.\n\n2) {hospital_names[6]}.\nThere are {general_beds[6]} general beds and {oxygen_beds[6]} oxygen_beds available\nTo book an appointment here please call - {phone_number[6]}."
                + Keys.ENTER
            )
            sec = False
        elif sector == "West":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThe closest hospital to you is {hospital_names[7]}.\nThere are {general_beds[7]} general beds and {oxygen_beds[7]} oxygen_beds available.\nTo book an appointment please call this number - {phone_number[7]}.\nFor directions please open the following link - https://goo.gl/maps/kYAEZPXo699UPuVC7."
                + Keys.ENTER
            )
            sec = False
        elif sector == "South":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThe closest hospital to you is {hospital_names[8]}.\nThere are {general_beds[8]} general beds and {oxygen_beds[8]} oxygen_beds available.\nTo book an appointment please call this number - {phone_number[8]}.\nFor directions please open the following link - https://goo.gl/maps/moPhTJkHzRSSatBS8."
                + Keys.ENTER
            )
            sec = False
        elif sector == "Bommanahalli":
            search[0].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                f"Dear Customer thank you for contacting us.\nThe closest hospital to you is {hospital_names[9]}.\nThere are {general_beds[9]} general beds and {oxygen_beds[9]} oxygen_beds available.\nTo book an appointment please call this number - {phone_number[9]}.\nFor directions please open the following link - https://goo.gl/maps/RdXzydorXry8JNMM6."
                + Keys.ENTER
            )
            sec = False
        else:
            search[1].send_keys(number[0] + Keys.ENTER)
            search[1].send_keys(
                "Please enter a valid sector as posted on the list above."
            )
            continue


# main Code
set_browser()
open_whatsapp()
New = False
Track = 1

while (
    Track == 1
):  # Loop to continuously check when update is detected if new number joins the whatsapp chat list
    number = whatsapp.find_elements_by_class_name("N2dUK")
    time.sleep(30)
    new_number = whatsapp.find_elements_by_class_name("N2dUK")
    if len(new_number) == len(number):
        continue
    elif len(new_number) > len(number):
        truk = True
        while truk:  # Loop to check if people want to try again
            new_num_set = set(new_number)
            num_set = set(number)
            new_num = new_num_set.difference(num_set)
            search = whatsapp.find_elements_by_class_name("_2_1wd")
            search[0].send_keys(new_num[0] + Keys.ENTER)
            search[1].send_keys(
                "Hello and welcome.\nI am an automated chatbot who can help you find hospital beds both general and oxygenated at government registered hospital near you.\nCurrently my search area only extends to the state of Karnataka."
                + Keys.ENTER
            )
            search[1].send_keys(
                "Please Enter a sector from the list below.\n - R R Nagar\n - Yelahamka\n - Daasarahalli\n - East\n - Mahadeva Pura\n - West\n - South\n - Bommanahalli"
            )

            soc = True
            while soc:  # Loop to check for response
                message = whatsapp.find_elements_by_class_name("_3ExzF")
                time.sleep(5)
                new_message = whatsapp.find_elements_by_class_name("_3ExzF")
                if len(new_number) == len(number):
                    continue
                else:
                    soc = False

            msg = whatsapp.find_elements_by_class_name("_3ExzF")
            state = "Karnataka"
            if state == "Karnataka":
                response()
            time.sleep(2)
            search[1].send_keys(
                "Thank you for using this chatbot. As of present date this chatbot can only perform limited functions and accept limited information.\nTo know about hospital availability in other sectors, please type 'Yes'.\n If not please type 'No'"
                + Keys.ENTER
            )

            soc = True
            while soc:  # Loop to check for response
                message = whatsapp.find_elements_by_class_name("_3ExzF")
                time.sleep(5)
                new_message = whatsapp.find_elements_by_class_name("_3ExzF")
                if len(new_number) == len(number):
                    continue
                else:
                    soc = False

            msg = whatsapp.find_elements_by_class_name("_3ExzF")
            choice = msg[-1]
            if choice == "Yes":
                continue
            else:
                break
