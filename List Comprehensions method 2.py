import argparse

parser = argparse.ArgumentParser(description='Search words including partial word')
parser.add_argument('snippet', help='partial (or complete) string to search in words')

args = parser.parse_args()
snippet = args.snippet.lower()

#words = open('/usr/share/dict/words').readlines()
with open('/usr/share/dict/words') as f:
    words = f.readlines()

#matches = []
#for word in words:
    #if snippet in word.lower():
        #matches.append(word)

matches = [word.strip() for word in words if snippet in word.lower()]

#we can also remove matches and pass output directly to print, like below and comment matches and print(matches)
#print([word.strip() for word in words if snippet in word.lower()])

print(matches)
