from textblob import TextBlob

x = input("Hi! I recently made a product, Please provide the feedback of my product. How was it for you? ")
y = TextBlob(x)
z = y.sentiment.polarity

if z<0:
    x1 = input("Awesome! Would you like to give in more details about your experience in person!")
    y1 = TextBlob(x1)
    z1 = y1.sentiment.polarity

    if z1<0:
        print("Thank you for the feedback")
    elif z1==0:
        print("Great! Awesome feedback")
    elif z1>0 and z1<=1:
        print("Great! Thank you!")

elif z==0:
    print("Oh! Thank you for your time!")

elif z>0 and z<=1:
    print("Great! Thank you so much for your valuable feedback!")
