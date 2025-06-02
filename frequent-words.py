#Program to find the top two words in a given string

import heapq
from collections import Counter

def find_top_two_words(text):
  words = text.lower().split()
  word_counts = Counter(words)
  top_two = heapq.nlargest(2,word_counts.items(), key=lambda item:item[1])
  return top_two

text = "The 2025 Indian Premier League, also known as IPL 18 and branded as TATA IPL 2025, is the 18th edition of the Indian Premier League. The tournament features 10 teams competing in 74 matches. It began on 22 March and was held across 13 venues before being suspended on 9 May due to the 2025 India–Pakistan crisis. The matches resumed from 17 May across six venues, and the final was rescheduled from 25 May to 3 June."
top_words = find_top_two_words(text)  
print(f"The top two words are : {two_words}")
