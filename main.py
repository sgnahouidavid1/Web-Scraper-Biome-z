import requests  # pip install requests in terminal
from bs4 import BeautifulSoup  # pip install BeautifulSoup in terminal
import tkinter as WebScraper_articles # adding the tkinter libary
import random # use to generate random numbers random.randint() 
import webbrowser # allow to open a website
from tkinter import *
from PIL import Image, ImageTk # allow the import of images in to the Gui progarm
import pandas as pd  # pip install pandas in terminal
bg_color = "#3A9AF9" # background color 
def clear_data (frame):
    for widght in frame.winfo_children():
        widght.destroy()
def load_frame3():
    clear_data (Frame2)
    clear_data (Frame1)
    Frame3.tkraise()
     #Inputing an image into the progarm and setting it as the backgrond of the program.
    logo = Image.open('WebScraper_Images.png') # grabbing the image that will be use for thr progarm 
    logo = ImageTk.PhotoImage(logo) # give the image a assign variable 
    logo_label = WebScraper_articles.Label(Frame3,image = logo , bg = "#3A9AF9") # assigning logal_label tp the the image
    logo_label.image = logo
    logo_label.grid(columnspan= 8, rowspan= 6)
    WebScraper_articles.Button(Frame3, text = "See the Instructions" ,font = ("TkHeadingFont", 15) , bg = "springgreen", fg ="snow", activebackground = "#badee2", activeforeground = "black", command = lambda: load_frame2()).grid(column = 0, row = 6)
    WebScraper_articles.Button(Frame3, text = "BACK 'to main page'" ,font = ("TkHeadingFont", 15) , bg = "springgreen", fg ="snow", activebackground = "#badee2", activeforeground = "black", command = lambda: load_frame1()).grid(column = 7, row =6)
    # Link Button Nature
    wedsite_linkButton = WebScraper_articles.StringVar()
    link_button = WebScraper_articles.Button(Frame3, textvariable = wedsite_linkButton, command = lambda: [create_articleFile()] ,font = ("TkHeadingFont", 12) , bg = "springgreen", fg ="snow", height = 1, width = 12)
    wedsite_linkButton.set("Nature")  # create the Nature button
    link_button.grid(column = 0, row = 0)# positioning
    #Link button for PubMed            
    wedsite_linkButton2 = WebScraper_articles.StringVar()
    link_button2 = WebScraper_articles.Button(Frame3, textvariable = wedsite_linkButton2, font = ("TkHeadingFont", 12) ,command = lambda: create_articleFile2(),bg = "springgreen", fg ="snow", height = 1, width = 12   )
    wedsite_linkButton2.set("PubMed ") #creation of the PubMed button 
    link_button2.grid(column = 0, row = 1)
def load_frame1():
    clear_data (Frame2)
    clear_data (Frame3)
    Frame1.tkraise()
    Frame1.pack_propagate(False)
    #Inputing an image into the progarm and setting it as the backgrond of the program.
    logo = Image.open('WebScraper.png') # grabbing the image that will be use for thr progarm 
    logo = ImageTk.PhotoImage(logo) # give the image a assign variable 
    logo_label = WebScraper_articles.Label(Frame1,image = logo , bg = "#3A9AF9") # assigning logal_label tp the the image
    logo_label.image = logo
    logo_label.grid(columnspan= 5, rowspan= 5) # positioning the image 
    WebScraper_articles.Label(Frame1, text = "Lets start scraping some articles!", fg = "snow", bg = bg_color, font = ("TKMenuFont",14)).grid(column=2, row=4)
    WebScraper_articles.Button(Frame1, text = "See Instructions" ,font = ("TkHeadingFont", 15) , bg = "springgreen", fg ="snow", activebackground = "#badee2", activeforeground = "black", command = lambda: load_frame2()).grid(column=0, row=5)
    WebScraper_articles.Button(Frame1, text = "Lets start scraping" ,font = ("TkHeadingFont", 15) , bg = "springgreen", fg ="snow", activebackground = "#badee2", activeforeground = "black", command = lambda: load_frame3()).grid(column=4, row=5)
    
def load_frame2():
    clear_data (Frame1)
    clear_data (Frame3)
    Frame2.tkraise()
    logo = Image.open('preview.png') # grabbing the image that will be use for thr progarm 
    logo = ImageTk.PhotoImage(logo) # give the image a assign variable 
    logo_label = WebScraper_articles.Label(Frame2,image = logo , bg = "#3A9AF9") # assigning logal_label tp the the image
    logo_label.image = logo
    logo_label.pack( side = BOTTOM) # positioning the image
    WebScraper_articles.Label(Frame2, text = "Perview:", fg = "snow", bg = bg_color, font = ("TKMenuFont",14)).pack(side = BOTTOM)
    WebScraper_articles.Label(Frame2, text = "Instructions:", fg = "snow", bg = bg_color, font = ("TKMenuFont",14)).pack()
    WebScraper_articles.Button(Frame2, text = "BACK to main page",font = ("TkHeadingFont", 10) , bg = "springgreen", fg ="snow", activebackground = "#badee2", activeforeground = "black", command = lambda: load_frame1()).pack( side = BOTTOM ,anchor = 'w')
    WebScraper_articles.Button(Frame2, text = "Lets start scraping  " ,font = ("TkHeadingFont", 10)  ,bg = "springgreen", fg ="snow", activebackground = "#badee2", activeforeground = "black", command = lambda: load_frame3()).pack( side = BOTTOM ,anchor = 'w')
    WebScraper_articles.Label(Frame2, text = "Click on the Website you would like to use to search for articles. Once you find\n the article your looking for copy the URL and place in the input box. \n Press the button WEB-Scrape to have the chosen article information scrape.\n   you'll now have an text file of the article scrape infromation", fg = "snow", bg = bg_color, font = ("TKMenuFont",12)).pack(anchor = "center")
# Creating the Gui 
root = WebScraper_articles.Tk() # WebScraper_articles.Tk creating the gui and (className= "webscraper_articles") is change the name of the Gui to webscraper_articles. seting it equal to root, set root to hold the gui canvas before any chances are made 
root.title("WEB-Scraper")
root.eval("tk::PlaceWindow . center")


Frame1 = WebScraper_articles.Frame(root, width = 644, height = 445, bg = bg_color) # WebScraper_articles.Canvas change the size of the gui program
Frame2 = WebScraper_articles.Frame(root, width = 644, height = 445,bg = bg_color) # WebScraper_articles.Canvas change the size of the gui program
Frame3 = WebScraper_articles.Frame(root, width = 644, height = 445,bg = bg_color) # WebScraper_articles.Canvas change the size of the gui program

for frame in (Frame1, Frame2, Frame3):
    frame.grid(row = 0, column = 0, sticky = "nesw" )
    
load_frame1()





# # Instruction:
# ########################################################
# # Instruction = WebScraper_articles.Label: The instruction of the app
# # Instruction['bg'] = "mediumaquamarine": setting the backgrond  color of the the labal
# # root['bg'] = "mediumaquamarine": setting the background color of the application 
# ########################################################
# Instruction = WebScraper_articles.Label(root, text = "Click on the Website you would like to use to search for articles. Next paste in copied URL on your clipboard to a new tab on your web browser. \n Now search for the article and paste the article URL in the Input box. \n Lastly click  the button called WEB-Scrape to have you article scrape of its infromation and have the infromation stored in a file called Article(some number).txt  ", font = "Raleway" )
# Instruction.grid(columnspan = 2, column = 0, row = 5)
# Instruction['bg'] = "mediumaquamarine"
# root['bg'] = "mediumaquamarine"
# # create_articleFile function no input perameters 
# ####################################################################################################################
# # This function will open a new tab the link the website search page 
# # Then the funcation creates an input box. The input box will be use to to enter in the URL of the article location
# # The function will createa button call WEB-Scrape and when click is will call the the function WebScraping()
# ####################################################################################################################
def create_articleFile():
    webbrowser.open('https://www.nature.com/search?order=relevance')
    Input_box = WebScraper_articles.Entry(Frame3, width = 40, font = ("TkHeadingFont", 12))
    Input_box.grid(column=6, row=4) # positioning of the input box
    input_linkButton = WebScraper_articles.StringVar()
    input_button = WebScraper_articles.Button(Frame3, textvariable = input_linkButton,command = lambda: WebScraping(),font = ("TkHeadingFont", 12) , bg = "mediumaquamarine", fg ="snow", height = 1, width = 12)
    input_linkButton.set("WEB-Scrap") # setting the name of the button 
    input_button.grid(column=6, row=5)  # positioning of the WEB-Scrape button 
    # WebScraping function on input perameters
    #############################################################################################################
    # the function gets the information that is enter in the input box 
    # create an article the the scrape infomation will be place 
    # the funcation will check if the article in infomation can be scrape
    # lastly the func will scrape infomatin like the Author, title, abtract etc to a text file 
    #############################################################################################################
    def WebScraping():
        Link = Input_box.get() # getting the infomation fron the input bot and assiging it to the variable called Link
        url = Link
        index = random.randint(1,100)
        file = open("Article{0}.txt".format(index), "x")
        response = requests.get(url) # requesting the html infomation for the website
        if response.status_code == 200: # check if the request response ( if response.status_code equal  200 then he website allow permission to scrape the website)
            print("Successfully opened the web page \n")
            soup = BeautifulSoup(response.text, 'html.parser') # accessing the hmtl of the the website 
            file.write("Title: \n")
            texts = soup.find_all('h1', class_="c-article-title") # getting the article title infomation
            if texts == None: # if:  there no title for the article print nothing
                file.write(" ")
            else: # else: print the article's title 
                for title in texts: 
                    title_text = title.get_text()
                    file.write(title_text)

            file.write("\n Publication: \n")
            texts = soup.find('span', class_="c-meta__item") # getting the article publication info
            if texts == None: # if:  there no publication for the article print nothing
                file.write(" ")
            else: # else: prints the article's Publication info
                for public in texts.find("i"):
                    publications = public.get_text()
                    file.write(publications)
            file.write("\n Publication Year: \n")
            texts = soup.find('a', href="#article-info") # getting the Publication Year 
            if texts == None:  # if:  there no publication year for the article, print nothing
                file.write(" ")
            else: # else: prints the article's Publication year 
                for publication in texts.find('time'):
                    publication_year = publication.get_text()
                    file.write(publication_year)
            file.write("\n Authors: \n")
            texts = soup.find_all('a', attrs = {'data-test': 'author-name'}) # getting all the author for the article 
            if texts == None:  # if:  there no author for the article, print nothing
                file.write(" ")
            else: # else: prints the article's authors
                for names in texts: 
                    author_text = names.get_text()
                    file.write(author_text)
                    file.write(' ')

            file.write("\n Abstract \n")
            texts = soup.find_all('div', class_='c-article-section__content', id='Abs1-content') # getting the abtract infomatiom
            if texts == None: # if:  there no abstract for the article, print nothing
                file.write(" ")
            else: # else:prints the article's abstract
                for abstract in texts: 
                    abstract_text = abstract.get_text()
                    file.write(abstract_text)

            file.write("\n DOI \n") 
            # gettig the DOI information from the article
            texts = soup.find('li', class_='c-bibliographic-information__list-item c-bibliographic-information__list-item--doi')
            if texts == None: # if:  there no DOI for the article, print nothing
                file.write(" ")
            else: # else: print the article's DOI
                for DOI in texts.find("span", class_='c-bibliographic-information__value'):
                    DOI_text = DOI.get_text()
                    file.write(DOI_text)

            file.write("\n ISSN \n")
            texts = soup.find('span', itemprop='onlineIssn') # getting the ISSN for the article 
            if texts == None: # if:  there no ISSN for the article, print nothing
                file.write(" ")
            else: # else: print the article's ISSN
                for ISSN in texts:
                    ISSN_num = ISSN.get_text()
                    file.write(ISSN_num)

            file.write("\n URL \n")
            file.write(url)
            input_linkButton.set("WEB-Scrap")
            

def create_articleFile2 ():
    webbrowser.open('https://pubmed.ncbi.nlm.nih.gov/advanced/')
    Input_box2= WebScraper_articles.Entry(Frame3, width = 40, font = ("TkHeadingFont", 12))
    Input_box2.grid(column=6, row=4)
    input_linkButton = WebScraper_articles.StringVar()
    input_button = WebScraper_articles.Button(Frame3, textvariable = input_linkButton,command = lambda: WebScraping2(),font = ("TkHeadingFont", 12), bg = "mediumaquamarine", fg ="snow", height = 1, width = 12)
    input_linkButton.set("WEB-Scrap")
    input_button.grid(column=6, row=5)   
    def WebScraping2():
        Link = Input_box2.get()
        url = Link
        index = random.randint(1,100)
        file = open("Article{0}.txt".format(index), "x")
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully opened the web page \n")
            soup = BeautifulSoup(response.text, 'html.parser')
            file.write("Title: ")
            texts = soup.find('div', class_="full-view" , id = "full-view-heading")
            if texts == None:
                file.write(" ")
            else:
                for title in texts.find("h1" , class_ = "heading-title"):
                    title_text = title.get_text()
                    file.write(title_text)
                    
            file.write("\n Author: \n ")
            texts = soup.find_all('a', class_="full-name")
            if texts == None:
                file.write(" ")
            else:
                for Author in texts:
                    Author_name = Author.get_text()
                    file.write(Author_name)
                    file.write(",  ")
            file.write("\n Publication \n")
            texts = soup.find('p', class_ = 'literature-footer-text')  
            if texts == None:
                file.write(" ")
            else:
                for publication  in texts :
                    publication_text = publication.get_text()
                    file.write(" ")
                    file.write(publication_text)
root.mainloop()

