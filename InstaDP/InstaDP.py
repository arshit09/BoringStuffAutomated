import webbrowser
import easygui

username = easygui.enterbox("Instagram username: ")

url = 'https://www.instadp.com/instagram-tools/full-size-downloader/' + username

chrome_path = 'C://Program Files//Google//Chrome//Application//chrome.exe %s --incognito'

webbrowser.get(chrome_path).open_new(url)