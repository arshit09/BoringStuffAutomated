import webbrowser
import easygui

pngname = easygui.enterbox("Image name: ")

url1 = 'https://favpng.com/png_search/' + pngname
url2 = 'https://www.cleanpng.com/free/' + pngname + '.html'
url3 = 'https://stickpng.com/search?q=' + pngname + '&page=1'
url4 = 'https://pngtree.com/so/' + pngname
url5 = 'https://purepng.com/search?q=' + pngname
url6 = 'https://www.pngwing.com/en/search?q=' + pngname
url7 = 'https://www.pngall.com/?s=' + pngname
url8 = 'https://www.pngitem.com/so/' + pngname + '/'

URLs = [url1, url2, url3, url4, url5, url6, url7, url8]

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(
    "C://Program Files//Google//Chrome//Application//chrome.exe"))

for i in range(0, 8):
    webbrowser.get('chrome').open(URLs[i])
