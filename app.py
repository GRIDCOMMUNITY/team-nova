"""Civic Issue Tracker - Hack Day Haldia x GRID community starter. Build the core tasks from README.md."""
import os
import sqlite3

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder=None)
DB_PATH = os.path.join(app.root_path, "data.db")


def db():
    """SQLite connection whose rows behave like dicts. Use:  with db() as conn: ..."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as conn:
        conn.executescript("""
            -- TODO: create your tables here, for example:
            -- CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
        """)


init_db()


@app.get("/")
def home():
    return send_from_directory(app.root_path, "index.html")


@app.get("/api/health")
def health():
    return jsonify(ok=True)


# ---- TODO(core): fill these in ------------------------------------------
@app.route("/api/issues", methods=['GET', 'POST'])
def ep1_api_issues(**kwargs):
    # TODO(core): list (with filters) / report an issue
    return jsonify(error="not implemented"), 501


@app.route("/api/issues/<int:iid>", methods=['GET', 'PATCH'])
def ep2_api_issues_int_iid(**kwargs):
    # TODO(core): read the timeline / update status
    return jsonify(error="not implemented"), 501


@app.route("/api/stats", methods=['GET'])
def ep3_api_stats(**kwargs):
    # TODO(core): counts by category and status
    return jsonify(error="not implemented"), 501



if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
