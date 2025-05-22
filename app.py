from flask import Flask, render_template, jsonify, request, make_response
import random
import psycopg2

def create_new_user(username): 
    conn = psycopg2.connect(
    dbname="courses",
    user="postgres",
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

def new_score(user_id, score): 
    conn = psycopg2.connect(
    dbname="courses",
    user="postgres",
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

def high_score(): 
    conn = psycopg2.connect(
    dbname="courses",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            u.name,
            MAX(s.score_value) AS max_score
        FROM users u
        JOIN scores s ON u.user_id = s.user_id
        GROUP BY u.user_id, u.name
        ORDER BY max_score DESC
        LIMIT 5;
    """)
    results = cur.fetchall()
    cur.close()
    conn.close()

    return results


app = Flask(__name__)
# List of random words (you can expand this or use a library)

refrence_course = []
def get_random_course():
    global refrence_course , assignment_course

    conn = psycopg2.connect(
        dbname="courses",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM KUcourses1 WHERE NOT course_id = %s ORDER BY RANDOM() LIMIT 1;",
                (refrence_course[0] if refrence_course and refrence_course[0] else "mock",))
    course = cur.fetchone()
    cur.close()
    conn.close()
    return course


@app.route("/", methods=['GET', 'POST'])
def home():
    # give two random courses to the html
    global refrence_course , assignment_course, score, player_id, nickname
    # Retrieve the nickname from the cookie if it exists
    nickname = request.cookies.get('nickname', '')
    if request.method == 'POST':
        nickname = request.form.get('nickname', '') 
        # TODO: add to the player db   
        player_id, nickname = create_new_user(nickname)
    print(nickname)

    if nickname:
        score = 0
        refrence_course = get_random_course()
        assignment_course = get_random_course()
        # Create a response with the rendered template
        response = make_response(render_template("home.html", 
                           Ref_Course_Title=refrence_course[1], Ref_Course_ID = refrence_course[0], Ref_Course_Descripition=refrence_course[7], Ref_Fail_Percentage=refrence_course[8],
                           Ass_Course_Title=assignment_course[1], Ass_Course_ID = assignment_course[0], Ass_Course_Descripition=assignment_course[7], Ass_Fail_Percentage=assignment_course[8], nickname = nickname))
        # Set the cookie with the nickname (expires in 30 days)
        response.set_cookie('nickname', nickname, max_age=30*24*60*60)
        return response
    else:
        response = make_response(render_template("home.html"))
        return response

@app.route('/get_random_word')
def get_random_word():
    # Get a new course and send it to js, together with the last course
    global refrence_course , assignment_course, score, player_id,nickname
    action = request.args.get('action', 'any')
    if (float(refrence_course[8]) <= float(assignment_course[8]) and action == "higher") or (float(refrence_course[8]) >= float(assignment_course[8]) and action == "lower"):
        refrence_course = assignment_course
        assignment_course = get_random_course()
        score += 1
        return jsonify({"score": score, "state": 1, "Ref_Course_Title": refrence_course[1], "Ref_Course_ID": refrence_course[0], "Ref_Course_Descripition": refrence_course[7], "Ref_Fail_Percentage": refrence_course[8],
         "Ass_Course_Title": assignment_course[1], "Ass_Course_ID": assignment_course[0], "Ass_Course_Descripition": assignment_course[7]})
    else:
        print(nickname)
        hscore = high_score()
        hscore.append((player_id, score))
        print(hscore)
        new_hscore = []
        new_score(player_id, score)
        for name, score1 in hscore:
            if score1 <= score:
                new_hscore.append([nickname,score])
            else:
                new_hscore.append([name, score1])
        print(new_hscore)
        # TODO: find the users rank
        # TODO: print the highscore, with highlight of user using jinja2
        score = 0
        return jsonify({"score": score, "state": 0, "Ref_Course_Title": refrence_course[1], "Ref_Course_ID": refrence_course[0], "Ref_Course_Descripition": refrence_course[7], "Ref_Fail_Percentage": refrence_course[8],
         "Ass_Course_Title": assignment_course[1], "Ass_Course_ID": assignment_course[0], "Ass_Course_Descripition": assignment_course[7], "hscore": new_hscore})


if __name__ == "__main__":
    app.run(debug=True, port=8001)

    