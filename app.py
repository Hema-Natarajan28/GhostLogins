from flask import Flask, render_template
from database import initialize_database, get_all_logins
app = Flask(__name__)
initialize_database()
@app.route("/")
def dashboard():
    logins = get_all_logins()
    return render_template("index.html", logins=logins)
if __name__ == "__main__":
    app.run(debug=True)