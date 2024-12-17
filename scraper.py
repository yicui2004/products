import requests
from lxml import html

description_Xpath = '//*[@id="viTabs_0_is"]/div'
image_Xpath = '//*[@id="PicturePanel"]/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/img'

def Xpath_from_HTML(url, xpath):
    """Fetches HTML content from the URL and extracts elements based on XPath."""
    page = requests.get(url)
    tree = html.fromstring(page.content)
    elements = tree.xpath(xpath)
    return html.tostring(elements[0], pretty_print=True).decode()

def extract_item_specifics(html_content):
    """Extracts item specifics (key-value pairs) from the HTML content."""
    tree = html.fromstring(html_content)
    rows = tree.xpath('//dl[@data-testid="ux-labels-values"]')
    item_specifics = {}
    for row in rows:
        key = row.xpath('.//dt//span[@class="ux-textspans"]/text()')
        value = row.xpath('.//dd//span[@class="ux-textspans"]/text()')
        if key and value:
            item_specifics[key[0].strip()] = value[0].strip()
    return item_specifics

def extract_image_url(html_content):
    """Extracts the product image URL from the HTML content."""
    tree = html.fromstring(html_content)
    image_url = tree.xpath('//img/@data-zoom-src')
    return image_url[0] if image_url else None
