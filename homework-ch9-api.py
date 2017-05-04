from instagram.client import InstagramAPI
access_token = "397790026.2df0ca9.025d01df64b3497ca9f5eac91be5fdfd"
client_secret = "a6081ef4c48a44c1a7b0c53a9fd21bdc "

api = InstagramAPI(access_token=access_token, client_secret=client_secret,)
user_id = api.user_search('t19960524')[0].id
recent_media, next_ = api.user_recent_media(user_id=user_id, count=5)

for media in recent_media:
   print (media.caption.text)
   print ('<img src="%s"/>' % media.images['thumbnail'].url)
