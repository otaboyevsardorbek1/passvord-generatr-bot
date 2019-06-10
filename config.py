import os

TOKEN = os.environ.get("BOT_TOKEN_CYPHER")

sql_config = {
    "host": 'localhost',
    "user": os.environ.get("SQL_USER"),
    "password": os.environ.get("SQL_PASS"),
    "db": os.environ.get("SQL_DB"),
    "charset": 'utf8mb4'
}

Reviews_state = False
# Set Reviews_state = True for enabling opportunity to leave reviews (probably not needed)
review_channel = -1001443580761
admin_id = 362089194

Webhook_state = False

# Set Webhook_state = True for enabling Webhook.
WEBHOOK_PATH = f'/{TOKEN}'
WEBHOOK_HOST = os.environ.get("BOT_HOST")
WEBHOOK_URL = f"https://{WEBHOOK_HOST}{WEBHOOK_PATH}/"
WEBAPP_PORT = os.environ.get("BOT_PORT")
WEBAPP_HOST = '127.0.0.1'
