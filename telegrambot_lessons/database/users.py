from telegrambot_lessons.database.db import cur


def insert_user(user_id, first_name, last_name, username):
    query = "INSERT INTO users (user_id, first_name, last_name, username) VALUES (%s, %s, %s, %s);"

    cur.execute(query, (user_id, first_name, last_name, username))
