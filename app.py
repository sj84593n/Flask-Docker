from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
dbJsonData = json.loads(open('./customerdb.json').read())
dbData = dbJsonData["Customer"]


class getAllOrders(Resource):
    def get(self):
        print dbData
        result = []
        for item in dbData:
            print item
            result.append(item)
        myresult = jsonify(result)
        return myresult

class getCustomerRecord(Resource):
    def get(self, cid=''):
        result = []
        for item in dbData:
            if int(cid) == int(item['CID']):
                result.append(item)
        if not result:
            myresult = "Unable to Fetch Data, Please check input"
        else:
            myresult = jsonify(result)
        return myresult

class getCustomerOrders(Resource):
    def get(self, cid=''):
        result = []
        for item in dbData:
            if int(cid) == int(item['CID']):
                result.append(item['Orders'])
        if not result:
            myresult = "Unable to Fetch Data, Please check input"
        else:
            myresult = jsonify(result)
        return myresult

class getCustomerSpecificOrder(Resource):
    def get(self, cid='', oid=''):
        result = []
        for item in dbData:
            if int(cid) == int(item['CID']):
                for listitem in item['Orders']:
                    if int(listitem['OID']) == int(oid):
                        result.append(listitem)
        if not result:
            myresult = "Unable to Fetch Data, Please check input"
        else:
            myresult = jsonify(result)
        return myresult

api.add_resource(getAllOrders, '/getallorders')
api.add_resource(getCustomerRecord,'/cust/<string:cid>')
api.add_resource(getCustomerOrders,'/cust/<string:cid>/orders')
api.add_resource(getCustomerSpecificOrder,'/cust/<string:cid>/orders/<string:oid>')

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')
