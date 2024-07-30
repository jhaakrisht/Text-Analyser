"""An application is being programmed here which uses Python commands to perform text analysis.
We seek to convert the text to lowercase and then find and count the frequency of all unique words, as well as a specified word."""

givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # removing punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # making text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # splitting text into words
        wordList = self.fmtText.split(' ')
        
        # Creating dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

analyzed = TextAnalyzer(givenstring)
print("Formatted Text:", analyzed.fmtText)
freqMap = analyzed.freqAll()
print(freqMap)
word = "lorem"
frequency = analyzed.freqOf(word)
print("The word",word,"appears",frequency,"times.")
