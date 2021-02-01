from flask_restx import Namespace,fields

class CbasApi:
    api = Namespace('cbas_api',description='Slik related operations')
    res = api.model('result', {
        'ref_number': fields.String(required = True, description= "application reference number" ),
        'result':fields.String(required=True,description ="slik result")
    })

class Pdmodel:
    api = Namespace('pdscoring',description='PD Scoring for Digital Loans')
    res = api.model('PD Output', {
        "ApplicationNumber": fields.String(required=True,description= "application number from LOS"),
        "GUID": fields.String(description= "GUID from LOS"),
        "Name": fields.String(description= "Customer Full Name"),
        "MarketingCode": fields.String(description= "Marketing Code from LOS"),
        "CustomerType": fields.String(required=True, description= "Is new or existing Customer"),
        "CIF": fields.String(required=True, description= "CIF data for existing customer"),
        "KTP": fields.String(required=True, description= "Customer's KTP"),
        "PD_Original": fields.Float(required=True, description="Original PD Score"),
        "PD_Recodification": fields.Float(required=True, description="Recodification Score")
    })
