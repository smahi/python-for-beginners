import requests
from bs4 import BeautifulSoup



# the script will try to download mp3 files from: https://server7.mp3quran.net/shur/
# after downloading a file it rename the from eg: 001.mp3 001-alfatiha.mp3
# to download the html code we will be using : https://requests.readthedocs.io/en/latest/
# for web page scrapping we will be using beautifulsoup4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# for reading the mp3 metadata we will be using: https://pypi.org/project/eyed3/

# read the html code
response = requests.get("https://server7.mp3quran.net/shur/")

if(response.status_code == 200):
    html_doc = response.content
    soup = BeautifulSoup(html_doc, 'html.parser')
    my_list = soup.find_all('a')[3:]
    
    urls = []

    for a_tag in my_list:
        url = f"https://server7.mp3quran.net/shur/{a_tag.contents[0]}"
        urls.append(url)
        
        
    print(urls[0])
else:
    print("An error occurred.")


