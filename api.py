import paralleldots
paralleldots.set_api_key('OFZ8br21FVopzCcubAmY0edQsLcPcazAvdC4JQ6lblY')

def ner(text):
    ner = paralleldots.ner(text)
    return ner

def sentiment_analysis(text):
    sentiment_result = paralleldots.sentiment(text)
    return sentiment_result

def abuse_detection(text):
    abuse_result = paralleldots.abuse(text)
    return abuse_result
