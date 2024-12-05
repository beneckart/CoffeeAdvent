from openai_stuff import get_embeddings
import os
import numpy as np
import requests
from typing import List, Tuple, Any


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

def get_ngram_frequency(phrase: str, cache={}) -> float:
    """Get frequency from NGRAMS API with caching"""
    if phrase in cache:
        return cache[phrase]
        
    base_url = "https://api.ngrams.dev"
    corpus = "eng"
    
    url = f"{base_url}/{corpus}/search"
    params = {
        "query": phrase,
        "flags": "cr",
        "limit": 1
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data["ngrams"]:
            freq = data["ngrams"][0]["relTotalMatchCount"]
        else:
            freq = 1e-10  # Very small number for phrases not found
            
        cache[phrase] = freq
        return freq
            
    except Exception as e:
        print(f"Error getting frequency for '{phrase}': {str(e)}")
        return 1e-10

def compute_frequency_rarity(phrase: str) -> float:
    """Convert ngram frequency to rarity score"""
    freq = get_ngram_frequency(phrase)
    return 1 / (np.log(freq + 1e-10) + 0.1)

def get_flavor_wheel_embeddings(filename='flavor_wheel_embeddings.npz'):
    if os.path.exists(filename):
        terms, embeddings = load_flavor_wheel_embeddings(filename)
    else:
        embeddings = get_embeddings(flavor_wheel_terms)
        np.savez_compressed(filename, terms=flavor_wheel_terms, embeddings=embeddings)
    return flavor_wheel_terms, embeddings

def load_flavor_wheel_embeddings(filename='flavor_wheel_embeddings.npz'):
    data = np.load(filename, allow_pickle=True)
    terms = data['terms']
    embeddings = data['embeddings']
    return terms, embeddings

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

def get_rarity_scores(participants_notes, note_embeddings, semantic_weight=0.5, frequency_weight=0.5, print_info=False):
    #Compute combined rarity scores using both semantic distance and ngram frequency
    # Normalize weights
    total = semantic_weight + frequency_weight
    semantic_weight = semantic_weight / total
    frequency_weight = frequency_weight / total
    
    # Get semantic rarity scores
    min_distances, min_indices = compute_min_distances(note_embeddings, flavor_wheel_embeddings,
                                                     return_indices=True)
    closest_wheel_terms = [flavor_wheel_terms[index] for index in min_indices]
    semantic_scores = compute_weights(min_distances)
    
    # Get frequency-based rarity scores
    frequency_scores = [compute_frequency_rarity(note) for note in participants_notes]
    
    # Combine scores
    combined_scores = [
        semantic_weight * sem_score + frequency_weight * freq_score
        for sem_score, freq_score in zip(semantic_scores, frequency_scores)
    ]
    
    if print_info:
        for note, wheel_term, distance, sem_score, freq_score, combined in zip(
            participants_notes, closest_wheel_terms, min_distances, 
            semantic_scores, frequency_scores, combined_scores
        ):
            print(f"\nParticipant note: '{note}'")
            print(f"Closest flavor wheel term: '{wheel_term}'")
            print(f"Semantic distance: {distance:.4f}")
            print(f"Semantic rarity score: {sem_score:.4f}")
            print(f"Frequency rarity score: {freq_score:.4f}")
            print(f"Combined rarity score: {combined:.4f}")
    
    return [combined_scores, closest_wheel_terms, min_distances]

# Initialize global variables
flavor_wheel_terms, flavor_wheel_embeddings = get_flavor_wheel_embeddings()