#The program can open multiple webpage at once
#Author: Habibul

import webbrowser
import time

socialMediaUrls=["https://twitter.com/", "www.facebook.com", "www.linkedin.com", ]
techUrls= ["https://github.com/", "https: // www.udemy.com /"]


def open_tabs(url_list):
    for element in url_list:
        webbrowser.open_new_tab(element)


def main():
    webbrowser.open("",new=0, autoraise=False)
    time.sleep(1)
    open_tabs(socialMediaUrls)
    open_tabs(techUrls)
main()



