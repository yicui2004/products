import google.generativeai as genai
from function_call import electronics, sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques

product_classifier_system_instructions = """
Given a product image as input, extract relevant parameters and populate the arguments of a pre-defined function designed to process product information.
The model must understand the context of the image and accurately map visual features to function parameters."""

# https://ai.google.dev/gemini-api/docs/models/experimental-models
gemini_pro_002_FC = genai.GenerativeModel(model_name="gemini-1.5-pro-002",
                                          system_instruction=product_classifier_system_instructions,
                                          tools = [electronics,  sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques])

gemini_exp_1206_FC = genai.GenerativeModel(model_name="gemini-exp-1206",
                                          system_instruction=product_classifier_system_instructions,
                                          tools = [electronics,  sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques])

gemini2_flash_exp = genai.GenerativeModel(model_name="gemini-2.0-flash-exp",
                                          system_instruction=product_classifier_system_instructions,
                                          tools = [electronics,  sporting_goods, clothing_shoes_accessories, home_garden, toys_hobbies, collectibles_antiques])

def gemini_embedding(input):
    return genai.embed_content(model="models/text-embedding-004", content=input)["embedding"]

def product_image_describer(product_image, model):
    prompt = "Help classify this image"

    if isinstance(model, genai.GenerativeModel):
        return model.generate_content([prompt, product_image])
    elif isinstance(model, genai.GenerativeModel):
        return model.generate_content([prompt, product_image])

    return None

def parse_output_FC_gemini(response):
    output = {}
    fn = response.parts[1].function_call
    for key, val in fn.args.items():
        output[key] = str(val)
    output["category"] = fn.name
    return output