from comparison import comparison_data_from_url
from image_describer import gemini_pro_002_FC, parse_output_FC_gemini
from comparison import gemini_embedding, match_closest_keys, match_closest_keys, calculate_total_similarity

def main():
    # Fetch comparison data from URL
    dict1, dict2 = comparison_data_from_url(
        "https://www.ebay.com/itm/256132260987",
        gemini_pro_002_FC,
        parse_output_FC_gemini
    )

    # Print dictionary contents
    print("Dictionary 1 Contents:\n")
    for key, value in dict1.items():
        print(f"{key}: {value}")
    
    print("\nDictionary 2 Contents:\n")
    for key, value in dict2.items():
        print(f"{key}: {value}")

    # Match closest keys
    key_matches = match_closest_keys(dict1, dict2, gemini_embedding)

    # Calculate total similarity
    total_similarity = calculate_total_similarity(dict1, dict2, key_matches, gemini_embedding)

    # Print results
    print("\nResults:")
    print(f"Key Matches: {key_matches}")
    print(f"Total Similarity Score: {total_similarity:.4f}")

# Entry point
if __name__ == "__main__":
    main()
