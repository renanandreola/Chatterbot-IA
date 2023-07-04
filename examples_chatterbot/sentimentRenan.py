from textblob import TextBlob
import matplotlib.pyplot as plt

def percentage(parte, total):
    return 100*float(parte)/float(total)

positivo = 0
negativo = 0
neutro = 0
polaridade = 0

contents = []
contents.append(TextBlob("I'm sad because my dog ​died"))
contents.append(TextBlob("I'm having a bad day, I'm sad and moody"))
contents.append(TextBlob("Hello, how are you?"))
contents.append(TextBlob("I am very happy today"))

for item in contents:
    polaridade += item.sentiment.polarity
    print(item, "\n", item.sentiment)
    
    if(item.sentiment.polarity == 0):
        neutro += 1
    elif(item.sentiment.polarity < 0):
        negativo += 1
    elif(item.sentiment.polarity > 0):
        positivo += 1
        
positivo = format(percentage(positivo, len(contents)), '.2f')
negativo = format(percentage(negativo, len(contents)), '.2f')
neutro = format(percentage(neutro, len(contents)), '.2f')

labels = ['Positivo [' + str(positivo) + '%]', 'Neutro [' + str(neutro) + '%]', 'Negativo [' + str(negativo) + '%]']
sizes = [positivo, neutro, negativo]
colors = ['green', 'lightgray', 'red']
patches,texts = plt.pie(sizes, colors=colors, startangle=90)

plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()