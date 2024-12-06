import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from collections import Counter
import re
import numpy as np

def process_raw_csv():
    # Load the CSV file
    file_path = './data/coffee_survey.csv'
    df = pd.read_csv(file_path, delimiter=',')

    # Columns that may contain tasting notes
    note_columns = [
        'coffee_a_notes', 'coffee_b_notes', 'coffee_c_notes', 'coffee_d_notes'
    ]

    # Extract tasting notes from the relevant columns
    def extract_tasting_notes(df, columns):
        tasting_notes = []
        for column in columns:
            if column in df.columns:
                notes = df[column].dropna().tolist()
                tasting_notes.extend(notes)
        return tasting_notes

    # Get all tasting notes
    tasting_notes = extract_tasting_notes(df, note_columns)

    # Remove any 'NA' values or blanks
    tasting_notes = [note for note in tasting_notes if note not in ['NA', '']]

    # Print all extracted tasting notes
    for note in tasting_notes:
        print(note)

    # Optionally, save to a file
    with open('./data/hoffman_tasting_notes.txt', 'w') as f:
        for note in tasting_notes:
            f.write(note + '\n')
        
    print(f"{len(tasting_notes)} different non-blank tasting notes")

# global
custom_stopwords = set(STOPWORDS).union({'coffee', 'flavor', 'taste', 'almost', 'much',
                                  'slightly', 'tasting', 'preference', 'felt',
                                  'remind', 'similar', 'think', 'really',
                                  'became', 'still', 'initially', 'enjoyed',
                                  'others', 'drink', 'coffees', 'thought',
                                  'note', 'mouth', 'started', 'easy', 'super',
                                  'favorite', 'slight', 'changed', 'love',
                                  'cooled', 'something', 'somewhat', 'maybe',
                                  'definitely', 'less', 'second', 'bit',
                                  'first', 'high', 'enjoy', 'best', 'way',
                                  'everyday', 'less', 'reminds','notes',
                                  'finish', 'tasted', 'liked'})

def create_wordcloud(tasting_notes):
    # Create a word cloud from the tasting notes
    all_notes_text = ' '.join(tasting_notes)

    wordcloud = WordCloud(
        width=400*2,
        height=600*2,
        background_color='white',
        stopwords=custom_stopwords
    ).generate(all_notes_text)

    # Display the word cloud
    plt.figure(figsize=(8, 12))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def basic_frequency_processing(tasting_notes):
    # Generate word frequencies using Counter

    all_notes_text = ' '.join(tasting_notes)
    words = re.findall(r'\w+', all_notes_text.lower())
    filtered_words = [word for word in words if word not in custom_stopwords]
    word_frequencies = Counter(filtered_words)

    # Print all word frequencies, including the long tail
    print("Raw word frequencies:")
    for i, (word, freq) in enumerate(sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)):
        print(f"{i:04d}. {word}: {freq}")

    print(f"musty score is {word_frequencies['musty']}")

    data = np.load("./data/our_tasting_notes_embeddings.npz", allow_pickle=True)
    our_notes = data['terms']

    our_scores = []
    for our_note in our_notes:
        freq = word_frequencies[our_note]
        our_scores.append(freq)

    print("*"*20 + " OUR RAREST NOTES " + "*"*20)
    for i, (word, freq) in enumerate(sorted(zip(our_notes, our_scores), key=lambda x: x[1], reverse=True)):
        print(f"{i:04d}. {word}: {freq}")

def structured_frequency_processing(tasting_notes):
    # Generate word frequencies using Counter, but keep phrases intact

    notes_flattened = []
    for notes in tasting_notes:
        note_lst = [x.strip() for x in notes.split(', ')]
        if note_lst[0] == '' and len(note_lst) == 1: continue
        notes_flattened.extend(note_lst)
    word_frequencies = Counter(notes_flattened)

    # Print all word frequencies, including the long tail
    print("Raw word/phrase frequencies:")
    for i, (word, freq) in enumerate(sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)):
        print(f"{i:04d}. {word}: {freq}")

    print(f"musty score is {word_frequencies['musty']}")

    data = np.load("./data/our_tasting_notes_embeddings.npz", allow_pickle=True)
    our_notes = data['terms']

    our_scores = []
    for our_note in our_notes:
        freq = word_frequencies[our_note]
        our_scores.append(freq)

    print("*"*20 + " OUR RAREST NOTES " + "*"*20)
    for i, (word, freq) in enumerate(sorted(zip(our_notes, our_scores), key=lambda x: x[1], reverse=True)):
        print(f"{i:04d}. {word}: {freq}")

    for word in ['chocolate', 'fruity', 'chamomile', 'musty', 'blue gatorade', 'cat litter']:
        print(f"{word}: {word_frequencies[word]}")

def ai_processing(tasting_notes):
    from openai_stuff import extract_tasting_notes

    ai_processed_notes = []
    for i in range(len(tasting_notes)):
        notes = extract_tasting_notes(tasting_notes[i])
        ai_processed_notes.append(notes)
        print(f"{i+1:4d}. {tasting_notes[i]}")
        print(', '.join(notes.notes).lower())
        print()

    with open('./data/hoffman_tasting_notes_AI_PROCESSED.txt', 'w') as f:
        for note in ai_processed_notes:
            f.write(', '.join(note.notes).lower() + '\n')


if __name__ == '__main__':
    #all_notes = open('./data/hoffman_tasting_notes.txt').readlines()
    #basic_frequency_processing(all_notes)
    #create_wordcloud(all_notes)
    #ai_processing(all_notes)
    ai_processed_notes = open('./data/hoffman_tasting_notes_AI_PROCESSED.txt').readlines()
    #create_wordcloud(ai_processed_notes)
    structured_frequency_processing(ai_processed_notes)