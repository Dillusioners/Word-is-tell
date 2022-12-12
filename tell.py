#Author - jayspray
#Team - Dillusioners
#Info - This program tells you a joke with the help of the official-jokes-api(link given in program)

#Importing required modules
import json
import requests

#This function is to retrieve the joke
def joke_sender(url):

    #Data returned after request at the url is stored in joke_data
    joke_data = requests.get(url)
    #Getting it into json
    joke = json.loads(joke_data.text)
    #Returning joke json
    return joke

#Main method
def main():
    #Api link
    loc = r"https://official-joke-api.appspot.com/random_ten"
    cnt = 0
    #While true loop to run until the user wishes it to run
    while True:
        #Simple try-except 
        try:
            choice =int(input("Enter 0 to listen a joke or any number to exit : "))
        except Exception as e:
            print("OOPs something went wrong ;(")
            print("Error ->",e)
        else:
            #Condition to stop or continue with jokes
            if choice != 0:
                break
            #Printing the type,setup and punchline of the joke
            else:
                your_joke = joke_sender(loc)
                jk = your_joke[0]
                print("-------------------------------------------------"+"\nJOKE"+"\n-------------------------------------------------")
                print("type : ",jk["type"],"\nsetup : ",jk["setup"],"\npunchline : ",jk["punchline"],"\n-------------------------------------------------")
                cnt+=1
    #Final display line
    print("Have a nice day :)")

#Main method is invoked
main()
#Program ends