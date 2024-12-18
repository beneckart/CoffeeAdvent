import unittest
from collections import defaultdict

def parse_daily_scores(data_text):
    """Parse the raw data text into structured daily scores."""
    current_day = None
    daily_rankings = []
    lines = data_text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('Day '):
            current_day = int(line.split(' ')[1])
        elif line.startswith('Scores to Official Notes:'):
            current_scores = []
            i += 1  # Move to the first score
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('Pairwise'):
                parts = lines[i].strip().split(': ')
                if len(parts) == 2:
                    name = parts[0].split('. ')[1]
                    score = float(parts[1])
                    current_scores.append((name, score))
                i += 1
            if current_scores:
                daily_rankings.append((current_day, current_scores))
            continue  # Skip the i += 1 at the end since we've already advanced i
        i += 1

    return daily_rankings

def parse_taster_similarity(data_text):
    """Parse the raw data text into taster similarity scores."""
    current_day = None
    similarity_scores = defaultdict(list)
    lines = data_text.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('Day '):
            current_day = int(line.split(' ')[1])
        elif line.startswith('Pairwise Agreement Scores:'):
            i += 1  # Move to first pairwise score
            while i < len(lines) and lines[i].strip() and not lines[i].startswith('Day'):
                parts = lines[i].strip().split(': ')
                if len(parts) == 2:
                    names = parts[0].split('. ')[1].split(' and ')
                    score = float(parts[1])
                    if 'Taster' in names:
                        other_person = names[0] if names[1] == 'Taster' else names[1]
                        similarity_scores[other_person].append(score)
                i += 1
            continue  # Skip the i += 1 at the end since we've already advanced i
        i += 1
    
    return similarity_scores

if __name__ == '__main__':
    # This would be your raw data text
    raw_data = open("output_results_day1-12.txt").read()  # Replace with actual data
    dr = daily_rankings = parse_daily_scores(raw_data)
    ts = taster_similarity = parse_taster_similarity(raw_data)   
    

    """Test the points calculation (3 for 1st, 2 for 2nd, 1 for 3rd)"""
    print("\n\nTOTAL POINTS")
    points = defaultdict(int)
    for day, rankings in dr:
        for i, (name, _) in enumerate(rankings[:3]):
            points[name] += 3 - i
    
     
    for name, pts in sorted(points.items(), key=lambda x: x[1], reverse=True):
        print(name, pts)
        
    scores = defaultdict(list)
    for day, rankings in dr:
        for name, score in rankings:
            #print(f"{name}: {score:.3f}")  
            scores[name].append(score)
    
    averages = {name: sum(s)/len(s) for name, s in scores.items()}    
    
    print("\n\nDAILY AVERAGES")
    for name, pts in sorted(averages.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {pts:.3f}")   
        
    print("\n\nPROFESSIONAL TASTER AVG SIMILARITY")
    
    ts_averages = {name: sum(s)/len(s) for name, s in ts.items()}    
    for name, pts in sorted(ts_averages.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {pts:.3f}")    
