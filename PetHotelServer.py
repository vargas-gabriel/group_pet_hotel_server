# Where our server requests will be

#flask imports
from flask import Flask, request, jsonify
#import con from connectionFunction.py
from connFunction import con
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'


@app.route('/pets', methods=['GET', 'POST'])
def get_pets():
  if (request.method == 'GET'):
    querytext = 'SELECT "pets"."id", "pets"."petName", "pets"."breed", "pets"."color", "pets"."isCheckedIn", "owners"."name" AS "ownerName" FROM "pets" JOIN "owners" ON "pets"."owner_id" = "owners"."id";'
    cur = con.cursor()
    cur.execute(querytext)
    rows = cur.fetchall()
    print(rows)
    return jsonify(rows), 201

@app.route('/owners', methods=['GET', 'POST'])
def get_owners():
  if (request.method == 'GET'):
    querytext = 'SELECT "owners"."id", "owners"."name", COUNT("pets"."owner_id") FROM "pets" JOIN "owners" ON "owners"."id" = "pets"."owner_id" GROUP BY "owners"."id";'
    cur = con.cursor()
    cur.execute(querytext)
    rows = cur.fetchall()
    print(rows)
    return jsonify(rows), 201
  elif (request.method == 'POST'):
    print (request.is_json)
    content = request.get_json()
    print (content)
    return 'created', 201