import genai
from scipy.spatial.distance import euclidean

def gemini_embedding(input):
  return genai.embed_content(model="models/text-embedding-004", content=input)["embedding"]

def match_closest_keys(dict1, dict2, embedding_function):
    key_matches = {}

    dict1_keys_embeddings = {}
    dict2_keys_embeddings = {}

    for key in dict1.keys():
        dict1_keys_embeddings[key] = embedding_function(key)
        print(key, dict1_keys_embeddings[key])
    for key in dict2.keys():
        dict2_keys_embeddings[key] = embedding_function(key)
        print(key, dict2_keys_embeddings[key])

    for key1, emb1 in dict1_keys_embeddings.items():
        closest_key = None
        closest_distance = float('inf')
        for key2, emb2 in dict2_keys_embeddings.items():
            distance = euclidean(emb1, emb2)

            if distance < closest_distance:
                closest_distance = distance
                closest_key = key2
        key_matches[key1] = closest_key

    return key_matches

def calculate_total_similarity(dict1, dict2, key_matches, embedding_function):

    total_similarity = 0.0
    for key1, key2 in key_matches.items():
        value1 = dict1[key1]
        value2 = dict2[key2]
        emb1 = embedding_function(value1)
        emb2 = embedding_function(value2)
        distance = euclidean(emb1, emb2)
        similarity_score = 1 / (1 + distance)  # Inverse of distance for similarity
        total_similarity += similarity_score
        print(f"Matching '{value1}' with '{value2}': Value Similarity = {similarity_score:.4f}")

    return total_similarity

# Example embedding function
def my_embedding_function(text):
    """
    Dummy embedding function that converts a string into a list of floating-point numbers.
    Replace this with your actual embedding function.
    """
    # Example: Return ASCII values of characters in the string (normalized)
    return [ord(char) / 255.0 for char in text]