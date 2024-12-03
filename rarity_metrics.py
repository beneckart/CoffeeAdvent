from openai_stuff import get_embeddings
import os
import numpy as np


level_1 = ["Floral", "Fruity", "Sour", "Fermented", "Green", "Vegetative", "Other", "Roasted", "Spices", "Nutty", "Cocoa", "Sweet"]
level_2 = [
    "Black Tea", "Floral", "Berry", "Dried Fruit", "Other Fruit", "Citrus Fruit",
    "Sour", "Alcohol", "Fermented", "Olive Oil", "Raw", "Green", "Vegetative", "Beany",
    "Papery", "Musty", "Chemical", "Pipe Tobacco", "Tobacco", "Burnt", "Cereal",
    "Pungent", "Pepper", "Brown Spice", "Nutty", "Cocoa", "Brown Sugar", "Vanilla",
    "Vanillin", "Overall Sweet", "Sweet Aromatics"]
level_3 = [
    "Chamomile", "Rose", "Jasmine",
    "Blackberry", "Raspberry", "Blueberry", "Strawberry",
    "Raisin", "Prune",
    "Coconut", "Cherry", "Pomegranate", "Pineapple", "Grape", "Apple", "Peach", "Pear",
    "Grapefruit", "Orange", "Lemon", "Lime",
    "Sour Aromatics", "Acetic Acid", "Butyric Acid", "Isovaleric Acid", "Citric Acid", "Malic Acid",
    "Winey", "Whiskey", "Fermented", "Overripe",
    "Under-ripe", "Peapod", "Fresh", "Dark Green", "Vegetative", "Hay-like", "Herb-like",
    "Stale", "Cardboard", "Papery", "Woody", "Moldy", "Damp", "Musty", "Dusty", "Earthy",
    "Animalic", "Meaty", "Brothy", "Phenolic",
    "Bitter", "Salty", "Medicinal", "Petroleum", "Skunky", "Rubber",
    "Acrid", "Ashy", "Smoky", "Brown", "Roast", "Grain", "Malt",
    "Anise", "Nutmeg", "Cinnamon", "Clove",
    "Peanuts", "Hazelnut", "Almond",
    "Chocolate", "Dark Chocolate",
    "Molasses", "Maple Syrup", "Caramelized", "Honey"]
flavor_wheel_terms = level_1 + level_2 + level_3

# Saving embeddings to a NumPy file if doesn't exist already
def get_flavor_wheel_embeddings(filename = 'flavor_wheel_embeddings.npz'):
    if os.path.exists(filename):
        terms, embeddings = load_flavor_wheel_embeddings(filename)
    else:
        embeddings = get_embeddings(flavor_wheel_terms)
        np.savez_compressed(filename, terms=flavor_wheel_terms, embeddings=embeddings)
    return flavor_wheel_terms, embeddings

# Loading embeddings from a NumPy file
def load_flavor_wheel_embeddings(filename='flavor_wheel_embeddings.npz'):
    data = np.load(filename, allow_pickle=True)
    terms = data['terms']
    embeddings = data['embeddings']
    return terms, embeddings

flavor_wheel_terms, flavor_wheel_embeddings = get_flavor_wheel_embeddings()

def get_rarity_scores(participants_notes, note_embeddings):
    # Compute minimum distances and indices
    min_distances, min_indices = compute_min_distances(note_embeddings, flavor_wheel_embeddings,
                                                       return_indices=True)

    # Map indices to flavor wheel terms
    closest_wheel_terms = [flavor_wheel_terms[index] for index in min_indices]

    rarity_scores = compute_weights(min_distances)

    for note, wheel_term, distance, rarity in zip(participants_notes, closest_wheel_terms, min_distances, rarity_scores):
        print(f"Participant note: '{note}'")
        print(f"Closest flavor wheel term: '{wheel_term}'")
        print(f"Distance: {distance:.4f}\n")
        print(f"Rarity Score: {rarity:.4f}\n")

    return [rarity_scores, closest_wheel_terms, min_distances]

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    if np.linalg.norm(vec1) == 0 or np.linalg.norm(vec2) == 0:
        return 0.0
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def compute_min_distances(note_embeddings, wheel_embeddings, return_indices=False, metric='cosine'):
    min_distances = []
    min_indices = []
    for note_emb in note_embeddings:
        if metric == 'L2':
            distances = [np.linalg.norm(np.array(note_emb) - np.array(wheel_emb)) for wheel_emb in wheel_embeddings]
        elif metric == 'L1':
            distances = [np.linalg.norm(np.array(note_emb) - np.array(wheel_emb), 1) for wheel_emb in wheel_embeddings]
        else: # default to cosine (technically 1 - cosine)
            distances = [1 - cosine_similarity(note_emb, wheel_emb) for wheel_emb in wheel_embeddings]
        min_distance = min(distances)
        min_index = distances.index(min_distance)
        min_distances.append(min_distance)
        min_indices.append(min_index)
    if return_indices:
        return min_distances, min_indices
    else:
        return min_distances

def compute_weights(min_distances, scaling_const=1):
    # exponential scaling
    scaled_weights = np.array([np.exp(distance/scaling_const) for distance in min_distances])/np.exp(0)
    return scaled_weights

def compute_idf_UNUSED(all_notes):
    ''' discarded idea: not gonna use, unless can find large corpus of previous coffee tasting notes to create the frequencies '''
    note_counts = defaultdict(int)
    total_documents = len(all_notes)
    for notes in all_notes:
        unique_notes = set(notes.notes)
        for note in unique_notes:
            note_counts[note] += 1
    print(note_counts);
    idf_scores = {note: math.log(total_documents / count) for note, count in note_counts.items()}
    print(idf_scores); input()
    return idf_scores

