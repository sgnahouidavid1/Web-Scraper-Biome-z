from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient
import yaml
import certifi
import math

from os import path
from bs4 import BeautifulSoup  # pip install BeautifulSoup in terminal
import requests  # pip install requests in terminal
import webbrowser  # allow to open a website
# allow the program to use findall word in a string ignoring spaces and puting it in a list.
import json  # Json libary allow the text file to covert to a joson file
from tkinter import filedialog  # allows to browse the computer to find files
from tkinter.filedialog import askdirectory
running = True  # Global flag
# Mongo DB connection

config = yaml.safe_load(open('db.yaml'))
client = MongoClient(config['uri'], tlsCAFile = certifi.where())
db = client['biomez']
collection = db.raw_records



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Biome-Z GUI")
        self.geometry("1150x500")
        # self.configure(background = "gray")
        tabControl = ttk.Notebook(self)
        self.tab2 = ttk.Frame(tabControl)
        tabControl.add(self.tab2, text="Mannual")
        self.tab3 = ttk.Frame(tabControl)
        tabControl.add(self.tab3, text="WEB-Scrape")
        tabControl.pack(expand=1, fill="both")

        self.addingWidgets()

    def addingWidgets(self):
        def update(data):
            List_box.delete(0, END)
            # add articles to Listbox
            for item in data:
                List_box.insert(END, item)

        def fillout(e):
            # Delete whatever is in the entry box
            Article_input.delete(0, END)
            # add clicked list item to entry box
            Article_input.insert(0, List_box.get(ANCHOR))
        message = ''' Luke I am your Father'''
        Mannual_box = Text(self.tab2, height=13, width=40, bg="lightgray")
        Mannual_box.insert('end', message)
        Mannual_box.pack(expand=True)
        Mannual_box.config(state='disabled')
        wedsite_linkButton3 = StringVar()
        wedsite_linkButton = StringVar()
        wedsite_linkButton2 = StringVar()
        labelFrame4 = ttk.LabelFrame(
            self.tab3, text="Website:", width=300, height=140)
        labelFrame4.pack(side=LEFT, anchor="n")
        NatureButton = Button(labelFrame4, textvariable=wedsite_linkButton,
                              command=lambda: article_search_natural(), font=("TkHeadingFont", 12), width=10)
        wedsite_linkButton.set("Nature")
        NatureButton.place(y=0, x=0)
        PUBMButton = Button(labelFrame4, textvariable=wedsite_linkButton2, font=(
            "TkHeadingFont", 12), width=10)
        wedsite_linkButton2.set("PubMed")
        PUBMButton.place(y=40)
        wedsite_linkButton3 = StringVar()
        ScienceButton = Button(labelFrame4, textvariable=wedsite_linkButton3, font=(
            "TkHeadingFont", 12), width=10)
        wedsite_linkButton3.set("Springer")
        ScienceButton.place(y=80)
        labelFrame5 = ttk.LabelFrame(
            self.tab3, text="Search Term:", width=300, height=140)
        labelFrame5.place(y=160)
        labelFrame6 = ttk.LabelFrame(
            self.tab3, text="Article Search:", width=820, height=475)
        labelFrame6.place(x=325)
        Art_label = Label(labelFrame6, text="Choose article: ",
                          font=("TkHeadingFont", 12))
        Art_label.place(y=30, x=15)
        Article_input = Entry(labelFrame6, font=(
            "TkHeadingFont", 12), width=73)
        Article_input.place(y=30, x=150)
        List_box = Listbox(labelFrame6, font=(
            "TkHeadingFont", 13), height=19, width=73)
        List_box.place(y=70, x=150)
        List_box.bind("<<ListboxSelect>>", fillout)
        def article_search_natural():
            search_term = Label(
                labelFrame5, text="Input term:", font=("TkHeadingFont", 12))
            search_term.place(y=25)
            Term_searchbox = Entry(labelFrame5, font=(
                "TkHeadingFont", 12), width=20)
            Term_searchbox.place(y=25, x=90)
            Gen_articles = Button(labelFrame5, text="Generate articles", command=lambda:  generate_articles_natural(), font=("TkHeadingFont", 12), width=14)
            Gen_articles.place(y=65)
            Webscrape_byterm = Button(labelFrame5, text="Scrape by term", command=lambda:  ScrapeArticle_byterm(), font=("TkHeadingFont", 12), width=14)
            Webscrape_byterm.place(x=150, y=65)
            def generate_articles_natural():
                dicts = {}
                Article_list = []
                term = Term_searchbox.get()
                url = "https://www.nature.com/search?q={}".format(term)
                response = requests.get(url)
                if response.status_code == 200:
                    print("Successfully opened the web page \n")
                    soup = BeautifulSoup(response.text, 'html.parser')
                    texts = soup.find_all(
                        'a', class_="c-card__link u-link-inherit")
                    for articles in texts:
                        articles_text = articles.get_text()
                        articles_links = articles.get('href')
                        dicts[articles_text] = articles_links
                    for key in dicts.keys():
                        Article_list.append(key)
                    update(Article_list)
                View_Art = Button(labelFrame6, text="View Article", font=( "TkHeadingFont", 12), command=lambda: view_article(), width=13)
                View_Art.place(y=80, x=15)
                def view_article():
                    article = Article_input.get()
                    webbrowser.open("https://www.nature.com{0}".format(dicts[article]))
            def ScrapeArticle_byterm():
                dicts = {}
                Article_list = []
                articlesNO_scrape = []
                articles_dicts = {}
                articles_list = []
                term = Term_searchbox.get()
                outfile = open("{}_articles.json".format(term), "w", encoding="utf-8")
                url = "https://www.nature.com/search?q={}".format(term)
                response = requests.get(url)
                if response.status_code == 200:
                    print("Successfully opened the web page \n")
                    soup = BeautifulSoup(response.text, 'html.parser')
                    texts = soup.find_all('a', class_="c-card__link u-link-inherit")
                    for articles in texts:
                        articles_text = articles.get_text()
                        articles_links = articles.get('href')
                        dicts[articles_text] = articles_links
                    for key in dicts.keys():
                        Article_list.append(key)
                    labelFrame7 =ttk.LabelFrame(self.tab3, text = "Articles scraping progress bar: " , width=300, height=90)
                    labelFrame7.place(y=315)
                    articles_progress = ttk.Progressbar(labelFrame7, orient = HORIZONTAL, length = 290, mode = 'determinate')
                    articles_progress.place(y = 10)
                    progress_label = Label(labelFrame7, text ="")
                    precent_label = Label(labelFrame7, text = "%")
                    precent_label.place(y = 35, x =  146)
                    progress_label.place(y = 35, x = 125)
                    numOfarticle = len(Article_list)
                    progess = 100/numOfarticle
                    for articles in dicts.keys():
                        url = "https://www.nature.com{0}".format(dicts[articles])
                        response = requests.get(url)
                        if response.status_code == 200:
                            print("Successfully opened the web page \n")
                            # accessing the hmtl of the the website
                            soup = BeautifulSoup(response.text, 'html.parser')
                        abstracts = soup.find_all('div', class_='c-article-section__content', id='Abs1-content')
                        if abstracts == []:
                            articlesNO_scrape.append(articles)
                        else:
                            articles_dicts["_id:"] = "None"
                            articles_dicts["itemType:"] = "None"
                            # getting the Publication Year
                            texts = soup.find('a', href="#article-info")
                            if texts == []:  # if:  there no publication year for the article, print nothing
                                print("No Publication Year for: ", articles)
                            else:  # else: prints the article's Publication year
                                for publication in texts.find('time'):
                                    publication_year = publication.get_text()
                                articles_dicts["pubYear:"] = publication_year
                                # getting all the author for the article
                            texts = soup.find_all('a', attrs={'data-test': 'author-name'})
                            if texts == []:  # if:  there no author for the article, print nothing
                                print("No Authors names for: ", articles)
                            else:  # else: prints the article's articles_texts
                                articles_texts = ''
                                for names in texts:
                                    author_text = names.get_text()
                                    articles_texts = articles_texts + author_text + " ,"
                                    articles_texts = articles_texts.encode("ascii", 'ignore')
                                    articles_texts = articles_texts.decode()
                                articles_dicts["author:"] = articles_texts
                            # getting the article title infomation
                            texts = soup.find_all('h1', class_="c-article-title")
                            for title in texts:
                                title_text = title.get_text()
                            articles_dicts["title:"] = title_text
                        # getting the article publication info
                            texts = soup.find('i', attrs={'data-test': "journal-title"})
                            if texts == []:  # if:  there no publication for the article print nothing
                                print("No Publication for: ", articles)
                            else:  # else: prints the article's Publication info
                                for public in texts:
                                    publications = public.get_text()
                                articles_dicts["pubTitle:"] = publications
                            articles_dicts["issn:"] = "None"
                            # gettig the DOI information from the article
                            texts = soup.find('li', class_='c-bibliographic-information__list-item c-bibliographic-information__list-item--doi')
                            if texts == []:  # if:  there no DOI for the article, print nothing
                                print("No DOI for: ", articles)
                            else:  # else: print the article's DOI
                                for DOI in texts.find("span", class_='c-bibliographic-information__value'):
                                    DOI_text = DOI.get_text()
                                articles_dicts["doi:"] = DOI_text
                            articles_dicts["url:"] = url
                            # getting the abtract infomatiom
                            texts = soup.find_all('div', class_='c-article-section__content', id='Abs1-content')
                                # else:prints the article's abstract
                            articles_texts = ''
                            for abstract in texts:
                                abstract_text = abstract.get_text()
                                abstract_text = abstract_text.replace('\u2009', " ")
                                abstract_text = abstract_text.replace('\n', " ")
                                articles_texts = articles_texts  + abstract_text + " "
                                articles_texts = articles_texts.encode("ascii", 'ignore')
                                articles_texts = articles_texts.decode()
                            articles_dicts["abstract:"] = articles_texts
                            articles_dicts["date:"] = "None"
                            articles_dicts["issue:"] = "None"
                            articles_dicts["volume:"] = "None"
                            articles_dicts["libCatalog:"] = "None"
                            articles_dicts["manualTags:"] = "None"
                            articles_dicts["autoTags:"] = "None"
                            texts = soup.find_all('li', class_="c-article-subject-list__subject")
                            if texts == []:  # if:  there no DOI for the article, print nothing
                                print("No Keywords for: ", articles)

                            else:
                                articles_texts = ''
                                for key in texts:
                                    keywords = key.get_text()
                                    articles_texts = articles_texts  + keywords + " ,"
                                articles_dicts["keywords:"] = articles_texts
                            articles_list.append(articles_dicts.copy())
                        articles_progress["value"] += progess
                        self.update_idletasks()
                        progress_label.config(text = math.trunc(articles_progress["value"])) 
                    outfile.write(json.dumps(articles_list, indent = 0))
                    outfile.write("\n")
                    NO_scrape = ' '.join([str(elem) for elem in articlesNO_scrape])
                    Cant_Scrape(NO_scrape)
                    
                            
                                


def fileExist(file):
    messagebox.showinfo('File Duplication Error', file)


def Cant_Scrape(article_names):
    messagebox.showinfo(
        "Articles that can't be scape of information because no abstract was found", article_names)


if __name__ == '__main__':
    root = Root()


root.mainloop()

