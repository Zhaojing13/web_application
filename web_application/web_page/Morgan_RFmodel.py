from flask import Flask,render_template,url_for,request
from flask_bootstrap import Bootstrap
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MACCSkeys
from rdkit.Chem import DataStructs
from rdkit.Chem.AllChem import GetMorganFingerprintAsBitVect
from rdkit.DataStructs.cDataStructs import ConvertToNumpyArray

app = Flask(__name__, template_folder='templates', static_folder="static")
bootstrap = Bootstrap(Morgan_RFmodel)
 
@app.route('/')
def home():
    return render_template('home.html')
 
@app.route('/predict',methods=['POST','GET'])



def predict():
    def FingerPrint1(i,j):
        FingerPrint=AllChem.GetMorganFingerprintAsBitVect(mol,radius=int(j),nBits=int(i))
        VectorFingerPrint=np.zeros((1,int(i)))
        for z in range(0,1):
            ConvertToNumpyArray(FingerPrint,VectorFingerPrint[z])
        return pd.DataFrame(VectorFingerPrint)

    morgan_RF_model = open('Morgan_RFmodel.pkl','rb')
    RF = joblib.load(morgan_RF_model)
 
    if request.method == 'POST':
        SMILE = request.form.get("message")
        mol = Chem.MolFromSmiles(SMILE)
        pred_x=FingerPrint1(int(3534.7573264539774),int(4.0))
        pred_y = RF.predict(pred_x)
    return render_template('result.html',prediction = pred_y)
 
 
 
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)