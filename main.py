from tkinter import  ttk
from tkinter import *
from tkinter import messagebox
import os.path
from os import path
from bs4 import BeautifulSoup  # pip install BeautifulSoup in terminal
import requests  # pip install requests in terminal
import webbrowser # allow to open a website
import re # allow the program to use findall word in a string ignoring spaces and puting it in a list.
import json # Json libary allow the text file to covert to a joson file
from tkinter import filedialog # allows to browse the computer to find files 
import os, glob # help the program find the path if a file 
from tkinter.filedialog import askdirectory
class Root(Tk):
    def __init__(self):
       super(Root,self).__init__()
       self.title("Biome-Z GUI")
       self.geometry("1150x500")
       #self.configure(background = "gray")
       tabControl = ttk.Notebook(self)
       self.tab1 = ttk.Frame(tabControl)
       tabControl.add(self.tab1, text = "WEB-Scraper")
       self.tab2 = ttk.Frame(tabControl)
       tabControl.add(self.tab2, text = "Mannual")
       tabControl.pack(expand = 1, fill = "both")
       self.addingWidgets()
    

       

    def addingWidgets(self):
        def create_articleFile():
            webbrowser.open('https://www.nature.com/search?order=relevance')
            URL_label = Label(labelFrame2, text = "Article URL:",font = ("TkHeadingFont", 12))
            URL_label.place(y = 25)
            URL_input = Entry(labelFrame2,font = ("TkHeadingFont", 12), width = 44 )
            URL_input.place(y = 25, x = 90)
            Web_scrape = Button(labelFrame2, text = " WEB-Scrape" ,font = ("TkHeadingFont", 12), command = lambda: WebScraping(), width = 12)
            Web_scrape.place( x = 190, y = 85)
            def WebScraping():
                
                Fileperview = Text(labelFrame3,height = 28, width = 76, bg = "lightgray")
                Fileperview.place(x = 0, y = 0)
                
                Link = URL_input.get()
                url = Link
                response = requests.get(url) # requesting the html infomation for the website # check if the request response ( if response.status_code equal  200 then he website allow permission to scrape the website)
                if response.status_code == 200:
                    print("Successfully opened the web page \n")
                    soup = BeautifulSoup(response.text, 'html.parser') # accessing the hmtl of the the website 
                    texts = soup.find_all('h1', class_="c-article-title") # getting the article title infomation
                    for title in texts: 
                        title_text = title.get_text()
                    json_file_name = title_text.replace(' ','_')
                    json_file_name = json_file_name.replace('/', '_')
                    fileExist("{0}.txt".format(json_file_name))
                    file = open("{0}.txt".format(json_file_name), "x")
                    file.write("Title: ")
                    Fileperview.insert('end', "Title: \n")
                    texts = soup.find_all('h1', class_="c-article-title") # getting the article title infomation
                    if texts == []: # if:  there no title for the article print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else: # else: print the article's title 
                        for title in texts: 
                            title_text = title.get_text()
                            file.write(title_text)
                            Fileperview.insert('end', title_text)

                    file.write("\n Publication: ")
                    Fileperview.insert('end', "\nPublication:\n")
                    texts = soup.find('i', attrs = {'data-test' : "journal-title"}) # getting the article publication info
                    if texts == []: # if:  there no publication for the article print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else: # else: prints the article's Publication info
                        for public in texts:
                            publications = public.get_text()
                            file.write(publications)
                            Fileperview.insert('end', publications)
                    file.write("\n Publication-Year: ")
                    Fileperview.insert('end', "\nPublication-Year: \n")
                    texts = soup.find('a', href="#article-info") # getting the Publication Year 
                    if texts == []:  # if:  there no publication year for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else: # else: prints the article's Publication year 
                        for publication in texts.find('time'):
                            publication_year = publication.get_text()
                            file.write(publication_year)
                            Fileperview.insert('end', publication_year)
                    file.write("\n Authors: ")
                    Fileperview.insert('end',"\nAuthors: \n" )
                    texts = soup.find_all('a', attrs = {'data-test': 'author-name'}) # getting all the author for the article 
                    if texts == []:  # if:  there no author for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else: # else: prints the article's authors
                        for names in texts: 
                            author_text = names.get_text()
                            file.write(author_text)
                            file.write(',')
                            Fileperview.insert('end',author_text)
                            Fileperview.insert('end', ",")

                    file.write("\n Abstract: ")
                    Fileperview.insert('end',"\nAbstract:\n")
                    texts = soup.find_all('div', class_='c-article-section__content', id='Abs1-content') # getting the abtract infomatiom
                    if texts == []: # if:  there no abstract for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else: # else:prints the article's abstract
                        for abstract in texts: 
                            abstract_text = abstract.get_text()
                            file.write(abstract_text)
                            Fileperview.insert('end', abstract_text)


                    file.write("\n DOI: ")
                    Fileperview.insert('end', "\nDOI: \n")
                    # gettig the DOI information from the article
                    texts = soup.find('li', class_='c-bibliographic-information__list-item c-bibliographic-information__list-item--doi')
                    if texts == []: # if:  there no DOI for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else: # else: print the article's DOI
                        for DOI in texts.find("span", class_='c-bibliographic-information__value'):
                            DOI_text = DOI.get_text()
                            file.write(DOI_text)
                            Fileperview.insert('end',DOI_text)


                    file.write("\n URL: ")
                    Fileperview.insert('end',"\nURL: \n")
                    file.write(url)
                    Fileperview.insert('end',url)
                    file.write("\n Keywords: ")
                    Fileperview.insert('end',"\nKeywords: \n")
                    texts = soup.find_all('li', class_ = "c-article-subject-list__subject")
                    if texts == []: # if:  there no DOI for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                    else:
                        for key in texts:
                            keywords = key.get_text()
                            file.write(keywords)
                            file.write(", ")
                            Fileperview.insert('end', keywords)
                            Fileperview.insert('end', ", ")
                    Fileperview.config(state ='disabled')  
        def create_articleFile2():
            webbrowser.open('https://pubmed.ncbi.nlm.nih.gov/advanced/')
            URL_label = Label(labelFrame2, text = "Article URL:",font = ("TkHeadingFont", 12))
            URL_label.place(y = 25)
            URL_input = Entry(labelFrame2,font = ("TkHeadingFont", 12), width = 44 )
            URL_input.place(y = 25, x = 90)
            Web_scrape = Button(labelFrame2, text = " WEB-Scrape" ,font = ("TkHeadingFont", 12),command = lambda: WebScraping2(), width = 12)
            Web_scrape.place( x = 190, y = 85)
            def WebScraping2 ():
                Fileperview = Text(labelFrame3,height = 28, width = 76, bg = "lightgray")
                Fileperview.place(x = 0, y = 0)
                Link = URL_input.get()
                url = Link
                response = requests.get(url)
                if response.status_code == 200:
                    print("Successfully opened the web page \n")
                    soup = BeautifulSoup(response.text, 'html.parser')
                    texts = soup.find("h1" , class_ = "heading-title")
                    for title in texts:
                        title_text = title.get_text()
                    json_file_name = ""
                    word = title_text.replace('\n','')
                    word = re.findall(r'\w+' , word)
                    for list in word:
                        json_file_name = json_file_name + " " + list
                    json_file_name = json_file_name.replace(" ","_")
                    fileExist("{0}.txt".format(json_file_name))
                    file = open("{0}.txt".format(json_file_name), "x")
                    file.write("Title: ")
                    Fileperview.insert('end',"Title: \n")
                    texts = soup.find("h1" , class_ = "heading-title")
                    if texts == None:
                        file.write("Empty")
                        Fileperview.insert('end',"Empty")
                    else:
                        for title in texts:
                            title_text = title.get_text()
                            json_file_name = " "
                            word = title_text.replace('\n','')
                            word = re.findall(r'\w+' , word)
                            for list in word:
                                json_file_name = json_file_name + " " + list 
                            file.write(json_file_name)
                            Fileperview.insert('end', json_file_name)
                    file.write("\n Author:  ")
                    Fileperview.insert('end', "\nAuthor: \n")
                    texts = soup.find_all('a', class_="full-name")
                    if texts == []:
                        file.write("Empty ")
                        Fileperview.insert('end',"Empty")
                    else:
                        for Author in texts:
                            Author_name = Author.get_text()
                            file.write(Author_name)
                            file.write(",  ")
                            Fileperview.insert('end', Author_name)
                            Fileperview.insert('end',",")
                    file.write("\n Publication: ")
                    Fileperview.insert('end', "\nPublication: \n")
                    texts = soup.find('p', class_ = 'literature-footer-text')  
                    if texts == []:
                        file.write("Empty")
                        file.write("Empty ")
                    else:
                        for publication  in texts :
                            publication_text = publication.get_text()
                            file.write(publication_text)
                            Fileperview.insert('end', publication_text)
                    file.write("\n Publication-Year: ") 
                    Fileperview.insert('end',"\nPublication-Year: \n")
                    texts = soup.find("span", class_ = "cit")
                    if texts == []:
                        file.write("Empty")
                        Fileperview.insert('end',"Empty")
                    else:
                        for pub_year in texts :
                            year = pub_year.get_text()
                            file.write(year)
                            Fileperview.insert('end', year)
                    file.write("\n Abstract: ")
                    Fileperview.insert('end',"\nAbstract: \n")
                    texts = soup.find("div", class_ = "abstract-content selected")
                    if texts == []:
                        file.write("Empty")
                        Fileperview.insert('end', "Empty")
                    else:
                        for abstract_text in texts:
                            abstract = abstract_text.get_text()
                            abstract_word = " "
                            word = abstract.replace('\n'," ")
                            word = re.findall(r'\w+', word)
                            for list in word:
                                abstract_word = abstract_word + " " + list
                            file.write(abstract_word)
                            Fileperview.insert('end', abstract_word)
                    file.write("\n DOI: ")
                    Fileperview.insert('end', "\nDOI: \n")
                    texts  = soup.find("a", class_ = "id-link" , target = "_blank")
                    if texts == []:
                        file.write("Empty")
                        Fileperview.insert('end', "Empty" )
                    else: 
                        for DOI in texts:
                            DOI_text = DOI.get_text()
                            DOI_word = " "
                            word = DOI_text.replace('\n', " ")
                            word = re.findall(r'\w+', word)
                            for list in word:
                                DOI_word = DOI_word + " " + list
                            file.write(DOI_word)
                            Fileperview.insert('end', DOI_word)
                            
                    file.write("\n URL: ")
                    Fileperview.insert('end', "\nURL: \n")
                    file.write(url)
                    Fileperview.insert('end',url)
                    Fileperview.config(state ='disabled')
        def create_articleFile3():
            webbrowser.open('https://link.springer.com/')
            URL_label = Label(labelFrame2, text = "Article URL:",font = ("TkHeadingFont", 12))
            URL_label.place(y = 25)
            URL_input = Entry(labelFrame2,font = ("TkHeadingFont", 12), width = 44 )
            URL_input.place(y = 25, x = 90)
            Web_scrape = Button(labelFrame2, text = " WEB-Scrape" ,font = ("TkHeadingFont", 12),command = lambda: WebScraping3(), width = 12)
            Web_scrape.place( x = 190, y = 85)
            def WebScraping3 ():
                Fileperview = Text(labelFrame3,height = 28, width = 76, bg = "lightgray")
                Fileperview.place(x = 0, y = 0)
                Link = URL_input.get()
                url = Link
                response = requests.get(url)
                if response.status_code == 200:
                   print("Successfully opened the web page \n")
                   soup = BeautifulSoup(response.text, 'html.parser') # accessing the hmtl of the the website 
                   texts = soup.find("h1", class_= "c-article-title")
                   for title in texts:
                        title_text = title.get_text()
                   json_file_name = title_text.replace(' ','_')
                   fileExist("{0}.txt".format(json_file_name))
                   file = open("{0}.txt".format(json_file_name),"x")
                   file.write("Title: ")
                   Fileperview.insert('end',"Title: \n" )
                   texts = soup.find("h1", class_= "c-article-title")
                   if texts == []:
                       file.write("Empty ")
                       Fileperview.insert('end', "Empty")
                   else:
                       for title in texts: 
                            title_text = title.get_text()
                            file.write(title_text)
                            Fileperview.insert('end', title_text)
                   file.write("\n Publication: ")
                   Fileperview.insert('end', "\nPublication:\n")
                   texts = soup.find("a", class_ = "app-footer__parent-logo")
                   if texts == []: 
                       file.write("Empty ")
                       Fileperview.insert('end',"Empty " )
                   else:
                       for public in texts.find("span", class_ = "u-visually-hidden"):
                            publications = public.get_text()
                            file.write(publications)
                            Fileperview.insert('end', publications)
                   file.write("\n Publication-Year: ")
                   Fileperview.insert('end', "\nPublication-Year: \n")
                   texts = soup.find('a', attrs = {'data-track-action' : "publication date"})
                   if texts == []: 
                       file.write("Empty ")
                       Fileperview.insert('end',"Empty " )
                   else:
                       for publication in texts.find('time'):
                            publication_year = publication.get_text()
                            file.write(publication_year)
                            Fileperview.insert('end', publication_year)
                   file.write("\n Authors: ")
                   Fileperview.insert('end',"\nAuthors: \n" )
                   texts = soup.find_all('a', attrs ={ 'data-test' : "author-name"})
                   if texts == []:  # if:  there no author for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                   else: # else: prints the article's authors
                        for names in texts: 
                            author_text = names.get_text()
                            file.write(author_text)
                            file.write(',')
                            Fileperview.insert('end',author_text)
                            Fileperview.insert('end', ",")
                   file.write("\n Abstract: ")
                   Fileperview.insert('end',"\nAbstract:\n")
                   texts = soup.find('div' , class_ = "c-article-section__content")
                   if texts == []: # if:  there no abstract for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                   else: # else:prints the article's abstract
                        for abstract in texts.find("p"): 
                            abstract_text = abstract.get_text()
                            file.write(abstract_text)
                            Fileperview.insert('end', abstract_text)
                   file.write("\n DOI: ")
                   Fileperview.insert('end', "\nDOI: \n")
                   texts = soup.find('li', class_ = "c-bibliographic-information__list-item c-bibliographic-information__list-item--doi")
                   if texts == []: # if:  there no DOI for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                   else: # else: print the article's DOI
                        for DOI in texts.find('span', class_ = "c-bibliographic-information__value"):
                            DOI_text = DOI.get_text()
                            file.write(DOI_text)
                            Fileperview.insert('end',DOI_text)
                   file.write("\n URL: ")
                   Fileperview.insert('end',"\nURL: \n")
                   file.write(url)
                   Fileperview.insert('end',url)
                   file.write("\n Keywords: ")
                   Fileperview.insert('end', "\nKeywords: \n")
                   texts = soup.find_all('li', class_ = "c-article-subject-list__subject")
                   if texts == []: # if:  there no DOI for the article, print nothing
                        file.write("Empty ")
                        Fileperview.insert('end', "Empty")
                   else:
                       for key in texts:
                            keywords = key.get_text()
                            file.write(keywords)
                            file.write(", ")
                            Fileperview.insert('end', keywords)
                            Fileperview.insert('end', ", ")
                    
                   Fileperview.config(state ='disabled')
                       

                   
        message ='''
Dear Reader,

    Don't let this situation
    blind your future. We at
    PythonGuides write tutorials
    with real life examples to 
    make you understand the concept
    in best possible way.

Thanks & Regards,
Team PythonGuides '''
        labelFrame = ttk.LabelFrame(self.tab1, text = "Website:" ,width=500,height=140)
        labelFrame.pack(side = LEFT ,anchor = "n" )
        Mannual_box = Text(self.tab2, height = 13, width = 40, bg = "lightgray")
        Mannual_box.insert('end', message)
        Mannual_box.pack(expand=True)
        Mannual_box.config(state='disabled')
        wedsite_linkButton = StringVar()
        wedsite_linkButton2 = StringVar()
        NatureButton = Button(labelFrame, textvariable = wedsite_linkButton, command = lambda: create_articleFile(),font = ("TkHeadingFont", 12), width = 10)
        wedsite_linkButton.set("Nature")
        NatureButton.place(y = 0, x = 0)
        PUBMButton = Button(labelFrame, textvariable = wedsite_linkButton2, command = lambda: create_articleFile2(),font = ("TkHeadingFont", 12), width = 10)
        wedsite_linkButton2.set("PubMed")
        PUBMButton.place( y = 40)
        wedsite_linkButton3 = StringVar()
        ScienceButton = Button(labelFrame, textvariable = wedsite_linkButton3, command = lambda: create_articleFile3(),font = ("TkHeadingFont", 12), width = 10)
        wedsite_linkButton3.set("Springer")
        ScienceButton.place(y = 80)
        labelFrame2 = ttk.LabelFrame(self.tab1, text ="Paste URL:" ,width=500,height=140 )
        labelFrame2.place(y = 200)
        labelFrame3 = ttk.LabelFrame(self.tab1, text ="Preview Text File:" ,width=620,height=475)
        labelFrame3.place(x = 525)
        ConvertJson = Button(self.tab1, text = "Convert text File to Json", command = lambda: convert_json(),font = ("TkHeadingFont", 12), width = 23)
        ConvertJson.place(y = 410)
        ConvertALLJson = Button(self.tab1, text = "Convert all text File to Json", command = lambda: convertAll_json(), font = ("TkHeadingFont", 12), width = 23)
        ConvertALLJson.place(y = 445)
        
        
def convert_json():                 
    json_file = filedialog.askopenfilename(parent=root ,filetypes = [("Text file", "*.txt")])
    name = os.path.abspath(json_file)
    file_name =  os.path.splitext(name)
    if json_file:
        print("file was sucessfuly loaded")
    dict = {}
    with open(json_file) as fn:
        for dictionary in fn:
            key, desc = dictionary.strip().split(None, 1)
            dict[key] = desc.strip()
                    
    outfile = open("{0}.json".format(file_name[0]), "w")
    json.dump(dict,outfile )
    outfile.close()        
        
        
def convertAll_json():
    path = askdirectory() 
    os.chdir(path)
    for file in glob.glob("*.txt"):
        file_name = os.path.splitext(file)
        dict = {}
        with open(file) as fn:
            for dictionary in fn:
                key, desc = dictionary.strip().split(None, 1)
                dict[key] = desc.strip()
                    
        outfile = open("{0}.json".format(file_name[0]), "w")
        json.dump(dict,outfile )
        outfile.close() 
def fileExist (file):
        if path.exists(file) == True:
            messagebox.showerror('File Duplication Error','Error: Text file was already created for this article! (File Override Error)')
    
if __name__ == '__main__':   
    root = Root()



root.mainloop()