
import os
import re

from wordcloud import WordCloud
from textblob import TextBlob

#text_all = TextBlob("bad mean boring boring boring unfair waste never enjoy well another better bright bright")
text_all = TextBlob("happy productive joy smile wonderful optimism lovely bad depressed poop waste unfair lazy trash mean dumb stupid")
text_pos = ""
text_neg = ""

def clr(ob):
    if re.search("bad.",ob):
        return "Reds"
    else:
        return "Greens"

for words in text_all.words:
    parcel = TextBlob(words)
    if parcel.sentiment[0] > 0:
        text_pos = text_pos + " " + words
    elif parcel.sentiment[0] < 0:
        text_neg = text_neg + " " + words

print(text_pos)
print(text_neg)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt

w = 10
h = 10
#fig = plt.figure(figsize=(5, 5))
fig = plt.figure()
columns = 2
rows = 1

ax = []

wordcloud1 = WordCloud(width = 350, height = 350, colormap = "Reds").generate(text_neg)

wordcloud2 = WordCloud(width = 350, height = 350, colormap = "Greens").generate(text_pos)

wrdcldbundle = [wordcloud1,wordcloud2]

for i in range( columns*rows ):
    img = wrdcldbundle[i]
    # create subplot and append to ax
    ax.append( fig.add_subplot(rows, columns, i+1) )
    plt.axis("off")
    #ax[-1].set_title("ax:"+str(i))  # set title -- will change title later
    plt.imshow(img, alpha=0.5) # alpha sets color


#plt.imshow(wordcloud1, interpolation='bilinear')
#plt.axis("off")
#plt.imshow(wordcloud2, interpolation='bilinear')

plt.show()


# lower max_font_size -- test

#wordcloud = WordCloud(max_font_size=20).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")

