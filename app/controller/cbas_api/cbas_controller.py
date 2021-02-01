from flask import request
from flask_restx import  Resource
from app.controller.api_utils.dto import CbasApi

tot = CbasApi.api
res = CbasApi.res

@tot.route('/checkres')
class CheckResult(Resource):
    @tot.doc('Get slik checking result')
    @tot.marshal_with(res)
    @tot.response(200,'SUCCESS')
    def post(self):
        data  = request.json
        print(data)
        result = {'ref_number': '123','result':'OK'}
        return result
