import requests
import psycopg2
from os import environ
from flask import Flask, jsonify, json

app = Flask(__name__)


def build_user(name, uuid, company_name, company_uuid):
    return {
        "name": name,
        "uuid": uuid,
        "company": {"name": company_name, "uuid": company_uuid},
    }


def get_user_from_a(uuid):
    host = environ.get("SERVICE_A_HOST", "localhost:8081")
    users_api = "api/v3/search"
    url = f"http://{host}/{users_api}"
    try:
        r = requests.get(url, params={"user_uuid": uuid})
    except requests.exceptions.ConnectionError:
        print(f"Failed to call System A at {r.requests.url}")
        return {}, False
    if not r.ok:
        print(f"Failed to get user ({uuid}) from System A")
        return {}, False
    try:
        user = r.json()["user"]
        name = user["name"]["first"] + " " + user["name"]["last"]
        uuid = user["uuid"]
        company_uuid = user["company"]["uuid"]
        return build_user(name, uuid, "", company_uuid), True
    except:
        print(f"Failed to parse user return from System A: {user.text}")
        return {}, False


def get_user_from_b(uuid):
    host = environ.get("SERVICE_B_HOST", "localhost:8082")
    users_api = "users"
    url = f"http://{host}/{users_api}"
    try:
        r = requests.get(f"{url}/{uuid}")
    except requests.exceptions.ConnectionError:
        print(f"Failed to call System B at {r.requests.url}")
        return {}, False
    if not r.ok:
        print(f"Failed to get user ({uuid}) from System B")
        return {}, False
    try:
        user = r.json()["user"]
        name = user["first"] + " " + user["last"]
        uuid = user["uuid"]
        company_uuid = user["company_id"]
        return build_user(name, uuid, "", company_uuid), True
    except:
        print(f"Failed to parse user return from System A: {user.text}")
        return {}, False


def get_user(uuid):
    user, succ = get_user_from_a(uuid)
    if not succ:
        user, succ = get_user_from_b(uuid)
    return user, succ


def get_company(uuid):
    host = environ.get("DB_HOST", "localhost")
    with psycopg2.connect(
        host=host, port="5432", dbname="root", user="root", password="pass"
    ) as db:
        with db.cursor() as cur:
            cur.execute(
                """
                SELECT companies.name
                FROM company_metadata
                LEFT JOIN companies ON company_metadata.id=companies.id 
                WHERE company_metadata.uuid=decode(replace(%s, '-', ''), 'hex');""",
                (uuid,),
            )
            company = cur.fetchone()
            if company is None:
                print(f"Failed to find company with {uuid}")
                return {}, False
            return {"uuid": uuid, "name": company[0]}, True


@app.route("/v1/users/<uuid>")
def get_user_by_uuid(uuid):
    print(f"Getting user by UUID: {uuid}")
    user, succ = get_user(uuid)
    if not succ:
        return ({}, 404)
    company, succ = get_company(user["company"]["uuid"])
    if not succ:
        return ({}, 404)
    user["company"] = company
    return jsonify(user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
