import streamlit as st
import pandas as pd
from spellchecker import SpellChecker



MAX_LINES = 5
text = st.text_area("One URL per line (5 max)", height=120, key=1)
lines = text.split("\n")  # A list of lines
linesList = []
for x in lines:
    linesList.append(x)
linesList = list(dict.fromkeys(linesList))  # Remove dupes
linesList = list(filter(None, linesList))  # Remove empty

"linesList - Python list of URLs inputed in text area"
st.write(type(linesList))
st.write(len(linesList))
linesList

start_execution = st.button(" Run model! ✨ ")

if text and start_execution:
    pass
elif text and not start_execution:
    pass
elif not text and not start_execution:
    st.stop()
else:
    pass

result = []


df = pd.read_csv('mispellings.csv')
df

testList = df["wardobr"].to_list()
testList


# Create the pandas DataFrame
data = [["wardobr", 10], ["wardobt", 15], ["wardobz", 14]]
dftestCharly = pd.DataFrame(data, columns=["Keyword", "randomData"])
dftestCharly

testList = dftestCharly["Keyword"].to_list()
testList


from spellchecker import SpellChecker
spell = SpellChecker()

# find those words that may be misspelled

misspelled = spell.unknown(linesList)

#misspelled = spell.unknown(testList)

'''
searchVol = []
for i in DATAOnly:
    searchVol.append(i["vol"])
"searchVol"
searchVol
'''

#for i in DATAOnly:
"searchVol"
#searchVol

searchVol = []
for word in misspelled:
    # Get the one `most likely` answer
        searchVol.append(spell.correction(word))       
    #fixed = 
    #print(type(fixed))
    #print(fixed)

    # Get a list of `likely` options
    # print(spell.candidates(word))

searchVol

joinedList = pd.DataFrame(
    {"mispellings": linesList, "fixed": searchVol}
)
joinedList






