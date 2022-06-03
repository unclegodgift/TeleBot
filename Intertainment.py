# Развлечения
import requests
import re
import bs4

# -----------------------------------------------------------------------
def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Прислать собаку":
        bot.send_message(chat_id, get_dog())

    elif ms_text == "Прислать анекдот":
        bot.send_message(chat_id, text=get_anekdot())


# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get("http://anekdotme.ru/random")
    soup = bs4.BeautifulSoup(req_anek.text, "parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]

# -----------------------------------------------------------------------
def get_dog():
    global url
    contents = requests.get('https://random.dog/woof.json').json()
    image_url = contents['url']
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = image_url
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url

# ---------------------------------------------------------------------
