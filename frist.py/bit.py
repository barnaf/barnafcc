import requests
from bs4 import BeautifulSoup
import lxml 
import csv


date = (input("plese enter the date in the  follwing fromat /MM/DD/YY:"))
bage = requests.get(f"https://www.yallakora.com/match-center/?date={date}")

def main(bage):
    src = bage.content
    soup = BeautifulSoup (src , "lxml")
    match_dittls=[]

    hampionship = soup.find_all("div", {'class': '2795 matchCard matchesList'})
    
    def get_match_info(hampionship):

        hampionship_tittle = hampionship.contents[1].find("h2").text.strip()
        print (hampionship_tittle)

    get_match_info(hampionship[0])
    

main(bage)