# reference https://thecleverprogrammer.com/2021/01/19/next-word-prediction-with-python/
import numpy as np

lexicon = {}

def update_lexicon(current : str, next_word : str) -> None:
    # Add the input word to the lexicon if it in there yet.
    if current not in lexicon:
        lexicon.update({current: {next_word: 1} })
        return

    # Recieve the probabilties of the input word.
    options = lexicon[current]

    # Check if the output word is in the propability list.
    if next_word not in options:
        options.update({next_word : 1})
    else:
        options.update({next_word : options[next_word] + 1})

    # Update the lexicon
    lexicon[current] = options
with open('gutenberg.txt', 'r') as dataset:
    for line in dataset:
        words = line.strip().split(' ')
        for i in range(len(words) - 1):
            update_lexicon(words[i], words[i+1])
for word, transition in lexicon.items():
    transition = dict((key, value / sum(transition.values())) for key, value in transition.items())
    lexicon[word] = transition

line = input('Enter incomplete sentence: ')
word = line.strip().split(' ')[-1]
if word not in lexicon:
    print('Word not found')
else:
    options = lexicon[word]
    #predicted = np.random.choice(list(options.keys()), p=list(options.values()))
    predicted=list(options.keys())
    print(line+' '+predicted[0])
    print('Other primary suggestions: ',predicted[1:])
    if predicted[0][-1]=='?':
      predicted[0]=predicted[0][:-1]
    secondaries=lexicon[predicted[0]]
    nextbest=list(secondaries.keys())
    if nextbest[0][-1]=='?':
      nextbest[0]=nextbest[0][:-1]
    tertiaries=lexicon[nextbest[0]]
    nextnextbest=list(tertiaries.keys())
    print('Further possibilities...')
    print(line+' '+predicted[0]+' '+nextbest[0])
    print('Secondary suggestions: ',nextbest)
    print(line+' '+predicted[0]+' '+nextbest[0]+' '+nextnextbest[0])
    print('Tertiary suggestions: ',nextnextbest)
