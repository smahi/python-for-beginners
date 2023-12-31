import requests
import eyed3
import os
from bs4 import BeautifulSoup   


download_path = 'Downloads'

if not os.path.exists(download_path):
    os.mkdir(download_path)
    


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
        
        
    for url in urls[-4:-1]:
        print(f"Downloading: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} - downloaded.")
            filename = url.split('/')[-1]
            file_path = f"{download_path}/{filename}"
            with open(file_path, 'wb') as f:
                f.write(response.content)
                audio_file = eyed3.load(file_path)
                title = audio_file.tag.title
                splitted_filename = filename.split('.')
                new_filename = f"{splitted_filename[0]}-{title}.{splitted_filename[1]}"
                new_file_path = f"{download_path}/{new_filename}"
                print(f"Rename {file_path} to {new_file_path}")
                os.rename(file_path, new_file_path)
                
        else:
            print(f"Unable to download {url}")
else:
    print("An error occurred.")


