import cv2
import os

def extract_features(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return None
    sift = cv2.SIFT_create()
    _, descriptors = sift.detectAndCompute(image, None)
    return descriptors

def match_features(descriptors1, descriptors2):
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches

def find_most_similar_image(query_image_path, database_folder):
    query_descriptors = extract_features(query_image_path)
    if query_descriptors is None:
        raise ValueError(f"Could not extract features from query image: {query_image_path}")
    
    best_match_image = None
    best_match_count = 0
    
    for image_name in os.listdir(database_folder):
        image_path = os.path.join(database_folder, image_name)
        _, db_descriptors = extract_features(image_path)
        
        if db_descriptors is None:
            continue
        
        matches = match_features(query_descriptors, db_descriptors)
        match_count = len(matches)
        
        if match_count > best_match_count:
            best_match_count = match_count
            best_match_image = image_path
    
    return best_match_image


query_image_path = 'querry.jpg'
database_folder = 'database'

most_similar_image = find_most_similar_image(query_image_path, database_folder)
print(f"The most similar image is: {most_similar_image}")
