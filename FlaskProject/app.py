from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)


model = joblib.load('emlak_fiyat_model.pkl')
df = pd.read_csv('emlakveriegitimehazir.csv')


district_list = df['District'].unique().tolist()
district_list.sort()

neighborhood_dict = {}
for dist in district_list:
    neighborhoods = df[df['District'] == dist]['Neighborhood'].unique().tolist()
    neighborhoods.sort()
    neighborhood_dict[dist] = neighborhoods


@app.route('/')
def home():
    return render_template('index.html',
                           districts=district_list)


@app.route('/get_neighborhoods/<district>')
def get_neighborhoods(district):
    if district in neighborhood_dict:
        return jsonify(neighborhoods=neighborhood_dict[district])
    return jsonify(neighborhoods=[])


@app.route('/predict', methods=['POST'])
def predict():
    try:

        district = request.form.get('district')
        neighborhood = request.form.get('neighborhood')
        size = float(request.form.get('size'))
        room_count = int(request.form.get('room_count'))
        building_age = float(request.form.get('building_age'))


        input_data = pd.DataFrame({
            'Size (m²)': [size],
            'Building Age': [building_age],
            'Room_Numeric': [room_count],
            'District': [district],
            'Neighborhood': [neighborhood]
        })


        prediction = model.predict(input_data)[0]


        formatted_prediction = f"{prediction:,.2f} TL"

        return jsonify({"success": True, "prediction": formatted_prediction})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)