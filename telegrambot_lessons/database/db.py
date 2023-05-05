from ..config import settings
import psycopg2

conn = psycopg2.connect(settings.DB_URL)
conn.autocommit = True
cur = conn.cursor()

