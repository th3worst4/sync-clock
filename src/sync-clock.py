import requests
from bs4 import BeautifulSoup
    
def formatdate(rawdate):
    date = rawdate.split(", ")
    date[0] = date[0].split("/")
    for i in range(3):
        date[0].append(date[0][1-i])
        date[0].pop(1-i)
    date[0] = "".join(date[0])   
    return " ".join(date)
    
def main():
    data = requests.get("https://free.timeanddate.com/clock/i9aa1cck/n213/tlbr5/tt0/tw0/tm3/td2/th1") #gets clock time

    if data.status_code != requests.codes.ok: #verifies if the GET was successful
        return 0
    
    soup = BeautifulSoup(data.text, "html.parser") #LET ME COOK!!
    clock = soup.find(id = "t1").get_text() #finds the tag and filter for content
    
    if len(clock) != 20 or type(clock) != type(str()): #verifies if the filtered content is valid
        return 0
    
    return formatdate(clock) #returns the formated date

if(__name__ == "__main__"):
    print(main())
