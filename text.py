pip install textblob
from textblob import TextBlob
tt=input("Type your sentence")
blob = TextBlob(tt)
dt=blob.detect_language()
print(dt)
tr=blob.translate(from_lang=dt, to ='en')
print(tr)
