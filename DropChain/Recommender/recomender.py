import datetime
import numpy as np
import pandas as pd
import re
import math
from pyproj import Proj
from sklearn.linear_model import LinearRegression



class RecommenderManager:
    '''

        Class of RecommenderManager, this manage all of challenges

    '''

    consumos = pd.read_csv('../../../datasets/consumos.csv',sep=';')
    tuberia = pd.read_csv('../../../datasets/tuberia.csv',sep=';')
    slice1 = pd.read_csv('../../../datasets/slice1.csv', sep=";")
    slice2 = pd.read_csv('../../../datasets/slice2.csv', sep=";")
    presencia_bcn = pd.read_csv('../../../datasets/presencia_bcn.csv',sep=';')

    slice1.ANYMES_CAL = pd.to_datetime(slice1.ANYMES_CAL, format = '%Y%m')
    slice2.ANYMES_CAL = pd.to_datetime(slice2.ANYMES_CAL, format = '%Y%m')
    consumos = pd.DataFrame(consumos)
    tuberia = pd.DataFrame(tuberia)
    slice1 = pd.DataFrame(slice1)
    slice2 = pd.DataFrame(slice2)
    presencia_bcn = pd.DataFrame(presencia_bcn)


    def recommend_challenges(self,num_contract):
        ''' This is the recommender '''

        print datetime.date.today()
        return ({'type': '3'})

    def mantenimiento_challenges(self, num_contract):
        date = datetime.date.today()
        #date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        end_date = date + datetime.timedelta(days=7)
        self.presencia_bcn.data = pd.to_datetime(self.presencia_bcn.data, format = '%d/%m/%y')
        user = self.slice2[self.slice2.ContratoCOD==num_contract]
        distrito = user.DES_DISTRIC
        distrito = distrito.to_frame()
        self.revision = self.presencia_bcn[self.presencia_bcn.source_n_distri == distrito.iloc[1,0]]
        dias_reto = self.revision[(self.revision.data >= date)&(self.revision.data <= end_date)].data.unique()

        date2 = datetime.datetime.strptime("2017-06-01", "%Y-%m-%d").date()
        model = LinearRegression()
        y = np.asarray(user['CONSUM'])
        user['ANYMES_CAL']=user['ANYMES_CAL'].map(datetime.datetime.toordinal)
        X = user[['ANYMES_CAL']]
        model.fit(X, y)
        model.score(X, y)
        coefs = zip(model.coef_, X.columns)
        result = model.predict(date2.toordinal())

        objetivo = result/60*750

        tipo = "mant"
        freq = 1

        return ({"type": tipo, "freq": freq, "objetivo": objetivo})
