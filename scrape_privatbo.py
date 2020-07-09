import requests
from bs4 import BeautifulSoup
from datetime import datetime
import logging
from tkinter import *


def main():
    now = datetime.utcnow()
    url = 'https://www.privatbo.dk/?id=95'

    time_ym = now.strftime('%y-%m')

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(
        filename=__file__.replace('.py', '{time}.log'.format(time=time_ym)), level=logging.DEBUG,
        format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    logging.info('Start scraping website')

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    p = soup.find_all('p')
    paragraphs = []
    for x in p:
        paragraphs.append(str(x))

    if 'Det er i øjeblikket ikke muligt at blive opnoteret' in paragraphs[1]:
        logging.info('Lists are not open yet.\n')
    else:
        logging.info('Lists are open.\n')
        alert_popup('LISTS IS OPEN', 'List is open, continue to: ', url)


def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()

if __name__ == '__main__':
    main()
