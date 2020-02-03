# import/download relevant packages
from solution.clean import Cleaner
import os

# get & print monkey learn api key
MonkeyLearnkey = (os.getenv('MONKEYLEARN_KEY')) 
print (MonkeyLearnkey)

# passes text to Cleaner
text = input("Raw text: ")
clean_text = Cleaner(text)
print(clean_text)