# Obscurus.spammer
Simple discord webhook spammer


to config just edit the following in the file:

               webhook_url = 'webhook_url'
               embed_desc = 'Description'
               embed_name = 'Name'

to edit the amount of embeds you want to send you need to edit the range() in this part of code:

                     for x in range(10):
                         spam_url = requests.post(webhook_url, headers=HEADERS, json = spam_content_req)

be default its set to 10




i wont be updating this because i made this while i was bored and had nothing to do

bye -burnt.chipset
