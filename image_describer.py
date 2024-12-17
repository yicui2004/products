import google.generativeai as genai
from function_call import electronics, sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques
from scraper import Xpath_from_HTML, extract_item_specifics, extract_image_url, description_Xpath, image_Xpath
from io import BytesIO
from PIL import Image
import requests

model_id = "gemini-1.5-pro-002"
product_classifier_system_instructions = """
Given a product image as input, extract relevant parameters and populate the arguments of a pre-defined function designed to process product information.
The model must understand the context of the image and accurately map visual features to function parameters."""
gemini_pro_002_FC = genai.GenerativeModel(model_name=model_id,
                                          system_instruction=product_classifier_system_instructions,
                                          tools = [electronics,  sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques])

gemini_pro_002_Prompt = genai.GenerativeModel(model_name=model_id,
                                          system_instruction=product_classifier_system_instructions,
                                          tools = [electronics,  sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques])

def gemini_embedding(input):
    return genai.embed_content(model="models/text-embedding-004", content=input)["embedding"]

def product_image_describer(product_image, model):
    prompt = "Help classify this image"
    response = model.generate_content([prompt, product_image])
    return response

def parse_output_FC_gemini(response):
    output = {}
    fn = response.parts[1].function_call
    for key, val in fn.args.items():
        output[key] = str(val)
    output["category"] = fn.name
    return output

def comparison_data_from_url(url, model, response_parser):
    description_content = Xpath_from_HTML(url, description_Xpath)
    item_specifics = extract_item_specifics(description_content)

    image_content = Xpath_from_HTML(url, image_Xpath)
    image_url = extract_image_url(image_content)

    img = Image.open(BytesIO(requests.get(image_url).content))
    response = product_image_describer(img, model)

    model_specifics = response_parser(response)

    return item_specifics, model_specifics
