import json
from typing import List

def electronics(
    brand: str,
    model: str,
    storage_capacity: str,
    processor: str,
    ram: str,
    condition: str,
    accessories: List[str],
    release_date: str
) -> str:
    """
    Generate a JSON object containing details about an electronic item.

    Args:
      brand (str): The brand of the electronic device (e.g., "Apple").
      model (str): The specific model of the device (e.g., "iPhone 13").
      storage_capacity (str): The storage capacity of the device (e.g., "256GB").
      processor (str): The type of processor in the device (e.g., "A15 Bionic").
      ram (str): The amount of RAM in the device (e.g., "4GB").
      condition (str): The condition of the device (e.g., "Used", "New").
      accessories (List[str]): A list of included accessories (e.g., ["Charger", "Earphones"]).
      release_date (str): The release date of the device (e.g., "2021-09-24").

    Returns:
      str: A JSON string containing the category and details of the electronic item.
    """
    return json.dumps({
        "category": "Electronics",
        "details": {
            "Brand": brand,
            "Model": model,
            "Storage capacity": storage_capacity,
            "Processor": processor,
            "RAM": ram,
            "Condition": condition,
            "Accessories": accessories,
            "Release date": release_date
        }
    }, indent=4)

def clothing_shoes_accessories(
    brand: str,
    size: str,
    condition: str,
    material: str,
    color: str,
    style: str
) -> str:
    """
    Generate a JSON object containing details about a clothing, shoe, or accessory item.

    Args:
      brand (str): The brand of the item (e.g., "Nike").
      size (str): The size of the item (e.g., "M", "9", "Large").
      condition (str): The condition of the item (e.g., "New with tags", "Used").
      material (str): The primary material of the item (e.g., "Cotton").
      color (str): The color of the item (e.g., "Red").
      style (str): The style of the item (e.g., "Casual", "Formal").

    Returns:
      str: A JSON string containing the category and details of the clothing, shoe, or accessory item.
    """
    return json.dumps({
        "category": "Clothing, Shoes & Accessories",
        "details": {
            "Brand": brand,
            "Size": size,
            "Condition": condition,
            "Material": material,
            "Color": color,
            "Style": style
        }
    }, indent=4)

def home_garden(
    item_name: str,
    condition: str,
    brand: str,
    material: str,
    size_dimensions: str,
    features: List[str],
    age_year_of_manufacture: str
) -> str:
    """
    Generate a JSON object containing details about a home or garden item.

    Args:
      item_name (str): The name of the item (e.g., "Sofa").
      condition (str): The condition of the item (e.g., "New", "Used").
      brand (str): The brand of the item (e.g., "IKEA").
      material (str): The primary material of the item (e.g., "Wood").
      size_dimensions (str): The size or dimensions of the item (e.g., "6x4 feet").
      features (List[str]): A list of features of the item (e.g., ["Foldable", "Waterproof"]).
      age_year_of_manufacture (str): The age or year of manufacture of the item (e.g., "2020").

    Returns:
      str: A JSON string containing the category and details of the home or garden item.
    """
    return json.dumps({
        "category": "Home & Garden",
        "details": {
            "Item Name": item_name,
            "Condition": condition,
            "Brand": brand,
            "Material": material,
            "Size/Dimensions": size_dimensions,
            "Features": features,
            "Age/Year of Manufacture": age_year_of_manufacture
        }
    }, indent=4)

def sporting_goods(
    brand: str,
    condition: str,
    size: str,
    material: str,
    model: str,
    features: List[str]
) -> str:
    """
    Generate a JSON object containing details about a sporting good.

    Args:
      brand (str): The brand of the sporting good (e.g., "Wilson").
      condition (str): The condition of the item (e.g., "New", "Used").
      size (str): The size of the item (e.g., "Standard", "12 inches").
      material (str): The primary material of the item (e.g., "Leather").
      model (str): The model of the sporting good (e.g., "ProStaff 97").
      features (List[str]): A list of features of the item (e.g., ["Lightweight", "Durable"]).

    Returns:
      str: A JSON string containing the category and details of the sporting good.
    """
    return json.dumps({
        "category": "Sporting Goods",
        "details": {
            "Brand": brand,
            "Condition": condition,
            "Size": size,
            "Material": material,
            "Model": model,
            "Features": features
        }
    }, indent=4)

def toys_hobbies(
    brand: str,
    condition: str,
    age_recommendation: str,
    features: List[str],
    character_theme: str
) -> str:
    """
    Generate a JSON object containing details about a toy or hobby item.

    Args:
      brand (str): The brand of the toy or hobby item (e.g., "Lego").
      condition (str): The condition of the item (e.g., "New", "Used").
      age_recommendation (str): The recommended age group for the item (e.g., "3+").
      features (List[str]): A list of features of the item (e.g., ["Interactive", "Educational"]).
      character_theme (str): The character or theme associated with the item (e.g., "Batman").

    Returns:
      str: A JSON string containing the category and details of the toy or hobby item.
    """
    return json.dumps({
        "category": "Toys & Hobbies",
        "details": {
            "Brand": brand,
            "Condition": condition,
            "Age recommendation": age_recommendation,
            "Features": features,
            "Character/Theme": character_theme
        }
    }, indent=4)

def collectibles_antiques(
    age: str,
    authenticity: str,
    condition: str,
    rarity: str,
    origin_provenance: str
) -> str:
    """
    Generate a JSON object containing details about a collectible or antique item.

    Args:
      age (str): The age of the item (e.g., "19th Century").
      authenticity (str): The authenticity of the item (e.g., "Original", "Reproduction").
      condition (str): The condition of the item (e.g., "Good", "Poor").
      rarity (str): The rarity of the item (e.g., "Rare", "Common").
      origin_provenance (str): The origin or provenance of the item (e.g., "France").

    Returns:
      str: A JSON string containing the category and details of the collectible or antique item.
    """
    return json.dumps({
        "category": "Collectibles & Antiques",
        "details": {
            "Age": age,
            "Authenticity": authenticity,
            "Condition": condition,
            "Rarity": rarity,
            "Origin/Provenance": origin_provenance
        }
    }, indent=4)
