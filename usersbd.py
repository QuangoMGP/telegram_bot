import psycopg2
conn = psycopg2.connect(database="telegram",
                        user="postgres",
                        password="1304",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


def StealIDbd(message):
    add_user_quary = f"""INSERT INTO tusers(id, first_name, second_name, username) VALUES ('{message.chat.id}', '{str(message.chat.first_name)}', '{str(message.chat.last_name)}', '{str(message.chat.username)}')"""
    try:
        cursor.execute(add_user_quary)
    except:
        print("quary error")
    conn.commit()