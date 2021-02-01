import os
import pandas as pd
import json
#os.environ['R_HOME'] = 'C:/Users/david.sirait/Documents/R/R-4.0.3'
#R_HOME is set at install_r.sh
filepath = os.path.dirname(__file__)

import rpy2.robjects as robj
from rpy2.robjects import r, pandas2ri
import numpy as np
r_source = robj.r['source']
r_source(filepath + "/functions.R")
pandas2ri.activate()

def test_func(x):
    hasil = robj.globalenv['hitung'](x)
    hasil_2 = np.array(hasil)
    return hasil_2

class pdScoringHelper:
    def __init__(self, json_input,):
        self.json_input = json_input
        self.demog_data = json_input['DemographicData']

    def slik_ntb(self):
        input_data= robj.r['fromJSON'](json.dumps(self.json_input))

        pd_slik = robj.globalenv['pdscore_bureau_slik'](input_data)
        hasil_slik = robj.conversion.rpy2py(pd_slik)
        hasil_slik_df = pd.DataFrame(hasil_slik)
        hasil_slik_df['bureau'] = "SLIK"
        hasil_slik_R = pandas2ri.py2rpy_pandasdataframe(hasil_slik_df)
        pd_demog = robj.globalenv['feature_engineering_demog'](input_data)
        hasil_demog = robj.conversion.rpy2py(pd_demog)

        pd_final = robj.globalenv['NTB_PDScore_final'](hasil_slik_R, hasil_demog)
        hasil_ntb = robj.conversion.rpy2py(pd_final)

        return hasil_ntb

    # def demog_score(self):
    #     pd_demog = robj.globalenv['feature_engineering_demog'](json.dumps(self.json_input))
    #     pd_demog_2= robj.conversion.rpy2py(pd_demog)
    #     return ""


def slik_handler(input_data):
    input = json.dumps(input_data)
    input_to_json = robj.r['prettify'](input)
    input_data1 = robj.r['fromJSON'](input_to_json)
    scored_data_bureau_final_slik = robj.globalenv['pdscore_bureau_slik'](input_data1)
    hasil_slik = robj.conversion.rpy2py(scored_data_bureau_final_slik)
    print(type(hasil_slik))
    hasil_slik_df = pd.DataFrame(hasil_slik)
    return hasil_slik,hasil_slik_df
