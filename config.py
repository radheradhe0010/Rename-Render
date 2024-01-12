# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "23657837")

API_HASH = os.environ.get("API_HASH", "d90bf753f0578c231a458fbb2d023e6f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6536440526:AAGocHlsIrnkEbtracgw63RphBkCNQQQh7c") 

FORCE_SUB = os.environ.get("FORCE_SUB", "hii_gais") 

             # Don't Remove Credit @hii_gais
             # Subscribe YouTube Channel For Join Group @radheradhe765
             # Ask Doubt on telegram @radheradhe765

DB_NAME = os.environ.get("DB_NAME", "Cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://RadheRadhe:RadheRadhe@cluster0.llykhla.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/98f2040093c999792de24.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5266213899').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
