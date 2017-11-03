#The program can open multiple webpages at once


import webbrowser
import time

socialMediaUrls=["https://twitter.com/", "www.facebook.com", "www.linkedin.com", ]
techUrls= ["https://github.com/", "https: // www.udemy.com /"]


def open_tabs(url_list):
    for element in url_list:
        webbrowser.open_new_tab(element)


def main():
    webbrowser.open("",new=2, autoraise=False)
    time.sleep(5) #To wait the program to start after 5 seconds
    open_tabs(socialMediaUrls)
    open_tabs(techUrls)
main()



