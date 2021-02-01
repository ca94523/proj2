from flask import request,jsonify
from flask_restx import Resource
from app.controller.api_utils.dto import Pdmodel
from app.services.Rfunctions import *

pd = Pdmodel.api
res = Pdmodel.res

@pd.route('/slik')
class CheckResult(Resource):
    @pd.doc('Get slik checking result')
    @pd.marshal_with(res)
    @pd.response(200,'SUCCESS')
    def post(self):
        data  = request.json
        print(data)
        result = {"ApplicationNumber": "J000011415",
    "GUID": "29af85bd-4951-4eba-b083-7c0e6a406357",
    "Name": "SYAIFUL FAUZI ",
    "MarketingCode": "AAN9999760NTB00000",
    "CustomerType": "ETB",
    "CIF": "000600007337835",
    "KTP": "3273031208810019",
    "PD_Original": 0.1628,
    "PD_Recodification": 0.1617}
        return result

@pd.route('/slikNTB')
class CheckFunction(Resource):
    @pd.doc('Return slik NTB pd score')
    @pd.response(200, 'SUCCESS')
    def post(self):
        data = request.json
        res = pdScoringHelper(data)
        slik_result = res.slik_ntb()
        return jsonify(slik_result.to_dict())

