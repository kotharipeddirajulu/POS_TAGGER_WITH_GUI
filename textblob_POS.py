# import all functions / classes from the tkinter
from tkinter import *

from textblob import TextBlob


# Function to clear both the text entry boxes
def clearAll():
    # whole content of text entry area is deleted
    text1_field.delete(0, END)
    text2_field.delete(1.0, END)


# Function to get a corrected word
def correction():
    # get a content from entry box
    input_text = text1_field.get()

    # create a TextBlob object
    blob_obj = TextBlob(input_text)

    # get a corrected word
    POS_text = str(blob_obj.tags)

    # insert method inserting the
    # value in the text entry box.
    text2_field.insert(END, POS_text)


# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='light grey')

    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("1200x900")

    # set the name of tkinter GUI window
    root.title("POS_TAGGER_ENGLISH")

    # Create Welcome to Spell Corrector Application: label
    headlabel = Label(root, text='Welcome to POS_TAGGER Application',
                      fg='white', bg="purple")

    # Create a "Input Word": label
    label1 = Label(root, text="Input Text",
                   bg='slate gray', fg='white')

    # Create a "Corrected Word": label
    label2 = Label(root, text="POS-TAGGED",
                   bg='slate gray', fg='white')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row=1, column=1)
    # Adding Footer Label
    footer_label = Label(root, text="", background="light grey")
    footer_label.grid(column=1, row=8)
    footer_label = Label(root, text="Done By:- B218019,B218020,B218021,B218022", background="light grey")
    footer_label.grid(column=1, row=9)
    scroll_label = Label(root, text="", background="light grey")
    scroll_label.grid(column=1, row=4)

    # padx keyword argument used to set paading along x-axis .
    # pady keyword argument used to set paading along y-axis .
    label1.grid(row=2, column=0, padx=20, pady=20)
    label2.grid(row=6, column=0, padx=20, pady=20)

    # Create a text entry box
    # for filling or typing the information.

    # Adding scroll bars

    # adding scroll bar to input text
    xscrollbar = Scrollbar(root, orient='horizontal')
    xscrollbar.grid(row=3, column=1, sticky=E + W)
    text1_field = Entry(root, xscrollcommand=xscrollbar.set, width=50)
    xscrollbar.config(command=text1_field.xview)
    # Adding Scroll bars to output Text
    scr = Scrollbar(root)
    scr.grid(row=6, column=2, sticky=N + S)
    text2_field = Text(root, height=15, width=70, wrap='word', yscrollcommand=scr.set, )
    scr.config(command=text2_field.yview)

    # padx keyword argument used to set paading along x-axis .
    # pady keyword argument used to set paading along y-axis .
    text1_field.grid(row=2, column=1, padx=10, pady=10, sticky=N + S + E + W)
    text2_field.grid(row=6, column=1, padx=10, pady=10, sticky=N + S + E + W)

    # Create a Correction Button and attached
    # with correction function
    button1 = Button(root, text="RUN_POS_TAGGER", bg="green", fg="white",
                     command=correction)

    button1.grid(row=5, column=1)

    # Create a Clear Button and attached
    # with clearAll function
    button2 = Button(root, text="Clear", bg="red",
                     fg="black", command=clearAll)

    button2.grid(row=7, column=1)

    # Creating a Text reference of the Tags used

    label3 = Label(root, text="CC -coordinating conjunction\nCD -cardinal digit\nDT -determiner\nEX -existential there (like: “there is” … think of it like “there exists”)\nFW -foreign word\nIN -preposition/subordinating conjunction\nJJ -adjective ‘big’\nJJR -adjective, comparative ‘bigger’\nJJS -adjective, superlative ‘biggest’\nLS -list marker 1)\nMD -modal could, will\nNN -noun, singular ‘desk’\nNNS -noun plural ‘desks’\nNNP -proper noun, singular ‘Harrison’\nNNPS -proper noun, plural ‘Americans’\nPDT -predeterminer ‘all the kids’\nPOS -possessive ending parent‘s\nPRP -personal pronoun I, he, she\nPRP$ -possessive pronoun my, his, hers\nRB -adverb very, silently,\nRBR -adverb, comparative better\nRBS -adverb, superlative best\nRP -particle give up\nTO -to go ‘to‘ the store.\nUH -interjection errrrrrrrm\nVB verb, base form take\nVBD -verb, past tense took\nVBG -verb, gerund/present participle taking\nVBN -verb, past participle taken\nVBP -verb, sing. present, non-3d take\nVBZ- verb, 3rd person sing. present takes\nWDT -wh-determiner which\nWP -wh-pronoun who, what\nWP$ -possessive wh-pronoun whose\nWRB -wh-abverb where, when",
                   bg='black', fg='white', relief=SUNKEN)

    label3.grid(row=6, column=4, padx=10, pady=10)
    # Start the GUI
    root.mainloop()


    #Done by Kothari PeddiRajulu
    #gmail:- uppykots@gmail.com
