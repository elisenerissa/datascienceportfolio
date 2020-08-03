#import relevant libraries
from flask import Flask, jsonify, request, render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

model = pickle.load(open('final_rfc_model.pkl', 'rb')) #load model
#train data mean
X_train_mean = [41.84652006374442, -87.69640778339804, 0.23795761078998073, 0.47157996146435455, 0.2904624277456647, 0.002890173410404624, 0.16053490246771204, 81.39788053949904, 63.67019910083494,
72.53403982016698, 59.23763648041105, 63.438021836865765, 0.6680314707771355, 8.451027617212588, 0.13024405908798933, 29.12196933204912, 29.685441554270966, 6.680916827231927, 15.943641618497109,
8.072567437379597, 4.774571826161384, 19.028730464568824, 0.005459216441875401, 0.31053307642903016, 0.050417469492614005, 0.005459216441875401, 0.017662170841361593, 0.011881824020552344, 0.0,
0.22318561335902376, 0.005459216441875401, 0.38792549775208734, 0.0, 0.0, 0.17405266538214514, 0.04367373153500321]
#train data standard deviations
X_train_std = [0.10664086207024093, 0.0843669490303093, 0.42583304974729974, 0.49919164797665466, 0.45397577668171, 0.05368258850001615, 0.34978343890126645, 8.100852060998339, 7.517711787447401,
 7.4708345200627075, 7.873812090002852, 8.458805656383772, 2.081315210030896, 6.346073579409657, 0.3210141006728541, 1.5546271689430664, 2.023980461078635, 3.1038064109249985, 9.057089132442115,
 2.588955459945822, 0.4286068508329708, 0.5039213683894529, 0.07368455331829564, 0.4627118810583596, 0.2188048177316289, 0.07368455331829564, 0.13172022837261382, 0.10835426285337, 1e-99, 0.4163817903662126,
  0.07368455331829564, 0.48727744247594534, 1e-99, 1e-99, 0.3791547639889701, 0.20436814015107957]

@app.route('/')
def home():
    return render_template('form_upload.html') #page to upload csv file


@app.route('/upload.html',methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':

        # Create variable for uploaded file
        f = request.files['fileupload']

        #convert the csv file to dataframe
        data = pd.read_csv(f)
        data_sc = ((data - X_train_mean)/X_train_std) #scale the data
        prediction = model.predict(data_sc) #predict the data
        predict_proba = model.predict_proba(data_sc) #generate predict proba
        wnv_prob = [ele[1] for ele in predict_proba]
        data['probability'] = wnv_prob
        data['WNV Present'] = prediction
        X_holdout_final = data.loc[:,['latitude','longitude','probability','WNV Present']] #slice the dataframe so that we show only the important columns
        pred_html = X_holdout_final.to_html(col_space=100) #convert dataframe to html 

    return pred_html




if __name__ == "__main__":
    app.run(debug=True)
