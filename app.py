from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    api_key = "8X0LZ4D15CWVhq15gqenjXFrTwdZXUVrHe8nnSy4Bj8"
    base_url = f"https://trefle.io/api/v1/plants?token={api_key}"
    
    response = requests.get(base_url)
    data = response.json()
    
    if data["data"]:
        plants = data["data"]  # Get all plants
        return render_template('home.html', plants=plants)

    else:
        return "No plants found", 404

@app.route('/plant', methods=['GET'])
def get_plant_info():
    plant_name = request.args.get('plant_name')
    api_key = "8X0LZ4D15CWVhq15gqenjXFrTwdZXUVrHe8nnSy4Bj8"
    base_url = f"https://trefle.io/api/v1/plants/search?token={api_key}&q={plant_name}"
    
    response = requests.get(base_url)
    data = response.json()
    
    if data["data"]:
        plant_info = data["data"][0]  # Get first plant that matches the query
        return render_template('plant_info.html', plant=plant_info)
    
    else:
        return "No plant found with that name", 404

if __name__ =='__main__':
    app.run(debug =True)