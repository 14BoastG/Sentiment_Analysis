# import/download relevant packages
from solution.clean import Cleaner

# passes text to Cleaner
text = input("Raw text: ")
clean_text = Cleaner(text)
print(clean_text)