from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "sigma sigma on the wall, who's the skibidiest of them all?"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "student_mgmt"

mysql = MySQL(app)


@app.route("/")
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template("index.html", students=data)


@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        flash("Data inserted successfully")
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO student_list (name, email, phone) VALUES (%s, %s, %s)",
            (name, email, phone),
        )
        mysql.connection.commit()

        return redirect(url_for("Index"))


@app.route("/delete/<string:id_date>", methods=["GET"])
def delete(id_data):
    flash("Data has been deleted")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student_list WHERE id=%s", (id_data))
    mysql.connection.commit()

    return redirect(url_for("Index"))


@app.route("/update", methods=["POST", "GET"])
def update():
    if request.method == "POST":
        flash("Data edited")
        id_data = request.form["id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        cur = mysql.connection.cursor()
        cur.execute(
            """UPDATE student_list SET name=%s, email=%s, phone=%s WHERE id=%s""",
            (name, email, phone, id_data),
        )
        mysql.connection.commit()

        return redirect(url_for("Index"))


if __name__ == "__main__":
    app.run(debug=True)
