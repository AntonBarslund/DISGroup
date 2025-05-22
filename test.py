import psycopg2

def create_new_user(username): 
    conn = psycopg2.connect(
    dbname="courses",
    user="jeppebondebakkensen",
    password="admin",
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING user_id, name;", 
                (username,))
    
    new_user = cur.fetchall()[0]
    conn.commit()
    cur.close()
    conn.close()

    return new_user

id, name = create_new_user("test")
print(f"id: {id}, name: {name}")

def new_score(user_id, score): 
    conn = psycopg2.connect(
    dbname="courses",
    user="jeppebondebakkensen",
    password="admin",
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO scores (user_id, score_value) VALUES (%s, %s) RETURNING score_id, user_id;",
        (user_id, score)
    )
    new_score = cur.fetchall()[0]
    conn.commit()
    cur.close()
    conn.close()

    return new_score

def get_all_users_and_scores(): 
    conn = psycopg2.connect(
        dbname="courses",
        user="jeppebondebakkensen",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    cur.execute("SELECT user_id, name FROM users")
    users = cur.fetchall()  # Fetches all rows as a list of tuples
    
    cur.execute("SELECT user_id, score_value FROM scores")
    scores = cur.fetchall() # Fetches all rows as a list of tuples
    cur.close()
    conn.close()
    
    return users, scores

# create_new_user("Mister Mistro")
# new_score (5, 4)
        
"""
users, scores = get_all_users_and_scores()

for score in scores: 
    user_id, score = score
    print(f"User ID: {user_id}, Score: {score}")
# Print users nicely
for user in users:
    user_id, name = user
    print(f"User ID: {user_id}, Name: {name}")
 """


def high_score(): 
    conn = psycopg2.connect(
        dbname="courses",
        user="jeppebondebakkensen",
        password="admin",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            u.user_id,
            u.name,
            MAX(s.score_value) AS max_score
        FROM users u
        JOIN scores s ON u.user_id = s.user_id
        GROUP BY u.user_id, u.name
        ORDER BY max_score ASC;
    """)

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results


high_score = high_score()

for id, name, score in high_score: 
    print(f"ID: {id}, username: {name}, score: {score}")