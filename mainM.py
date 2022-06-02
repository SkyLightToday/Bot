# from requests import get

# api_req = 'https://api.telegram.org/bot5456958811:AAHKLt2fiWYHzjzzDP2yaIZZ22FJvafY_Ug'

# updates = get(api_req + '/getUpdates?offset=-1').json()
# print(updates)
# m = updates['result'][0]['message']
# chat_id = m['from']['id']
# print(chat_id)
# text = m['text']
# send_msg = get(api_req + f'/sendMessage?chat_id={chat_id}&text={text}')