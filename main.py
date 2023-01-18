import requests

webhook_url = 'webhook_url'
embed_desc = 'Description'
embed_name = 'Name'

def menu_ui():
    print(f"""                                
                                             
       _____  ______  _______ _______ _     _  ______ _     _ _______   _______  _____  _______ _______ _______ _______  ______      
      |     | |_____] |______ |       |     | |_____/ |     | |______   |______ |_____] |_____| |  |  | |  |  | |______ |_____/ 
      |_____| |_____] ______| |_____  |_____| |    \_ |_____| ______| . ______| |       |     | |  |  | |  |  | |______ |    \_     
                                                                                                                                     
                                          Made with <3 by burnt.chipset@obscurus.network


    Current Config:
    -webhook url = {webhook_url}
    -embed name  = {embed_name}
    -embed desc  = {embed_desc}

    """)

menu_ui()

#embed
spam_content_req = {
}

spam_content_req["embeds"] = [
                {
                    'author': {
                        'name': f'{embed_name}'
                    },
                    'description': f'''{embed_desc}''',
                        
            }
]


HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/45.0.2454.101 Safari/537.36'),
                          'referer': 'http://stats.nba.com/scores/'}

def start_spam():
    #post
    print("starting to spam, press CTRL + C to stop")
    for x in range(10):
        spam_url = requests.post(webhook_url, headers=HEADERS, json = spam_content_req)
        if spam_url == '200':
            print("didnt return 200")
        else:
            print("returned 200")
    
start_spam()
    

