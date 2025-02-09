from flask import Flask, jsonify
from flask_cors import CORS 
import beach_data_scraper as scraper
import requests
from tabulate import tabulate

app = Flask(__name__)
CORS(app) #enable CORS for react access

#latitude and longitude for each beach
beach_locations = {
    #West Vancouver
    "Ambleside": {"latitude": 49.323516823160986, "longitude": -123.14995679677853},
    "Dundarave": {"latitude": 49.332779, "longitude": -123.183318},
    "Sandy Cove": {"latitude": 49.340563, "longitude": -123.226685},
    "Eagle Harbour": {"latitude": 49.353861, "longitude": -123.269168},
    "Whytecliff Park": {"latitude": 49.372045, "longitude": -123.291015},

    #English Bay
    "Third": {"latitude": 49.303926, "longitude": -123.156709},
    "Second": {"latitude": 49.294439, "longitude": -123.150158},
    "English Bay": {"latitude": 49.286642, "longitude": -123.143575},
    "Sunset": {"latitude": 49.279190, "longitude": -123.139105},
    "Kitsilano Point": {"latitude": 49.278755, "longitude": -123.143250},
    "Kitsilano Beach": {"latitude": 49.275244, "longitude": -123.153964},
    "Jericho": {"latitude": 49.272492, "longitude":  -123.192597},
    "Locarno": {"latitude": 49.275846, "longitude":  -123.206308},
    "Spanish Banks": {"latitude": 49.277258, "longitude":  -123.215874},

    #Wreck Beach
    "Foreshore East": {"latitude": 49.279440, "longitude":  -123.236707},
    "Foreshore West, Acadia Beach": {"latitude": 49.279835, "longitude":  -123.242233},
    "Trail 4, Towers": {"latitude": 49.273253, "longitude":  -123.257512},
    "Trail 6, Breakwater": {"latitude": 49.261910, "longitude":  -123.262278},
    "Trail 7, Oasis": {"latitude": 49.255841, "longitude":  -123.255910},

    #Burrard Inlet: Indian Arm
    "Cates Park": {"latitude": 49.300421, "longitude":  -122.956006},
    "Deep Cove": {"latitude": 49.328353, "longitude":  -122.948701},

    #Trout Lake
    "Trout Lake": {"latitude": 49.254360, "longitude":  -123.061797},

    #Richmond
    "Iona": {"latitude": 49.219089, "longitude":  -123.215054},

    #Bowen Island
    "Sandy Beach": {"latitude": 49.381602, "longitude":  -123.331222},
    "Pebbly Beach": {"latitude": 49.385635, "longitude":  -123.333382},
    "Mothers Beach": {"latitude": 49.382323, "longitude":  -123.334173},
    "Tunstall Bay": {"latitude": 49.352371, "longitude":  -123.419142},
    "Bowen Bay": {"latitude": 49.364874, "longitude":  -123.423553},

    #Lions Bay
    "Brunswick Beach": {"latitude": 49.470869, "longitude":  -123.243732},
    "Kelvin Grove Beach": {"latitude": 49.450317, "longitude":  -123.239888},
    "Lions Bay Beach": {"latitude": 49.455559, "longitude":  -123.239514},

    #Sea to Sky
    "Alpha Lake Beach": {"latitude": 50.094595, "longitude":  -123.000270},
    "Alta Lake Blueberry Beach": {"latitude": 50.117973, "longitude":  -122.974937},
    "Alta Lake Hostel Beach": {"latitude": 50.119865, "longitude":  -122.983374},
    "Alta Lake Lakeside Park Beach": {"latitude": 50.107753, "longitude":  -122.980431},
    "Alta Lake Wayside Park Beach": {"latitude": 50.104536, "longitude":  -122.986398},
    "Alta Lake Rainbow Beach": {"latitude": 50.120068, "longitude":  -122.983175},
    "Lost Lake Beach": {"latitude": 50.127053, "longitude":  -122.935307},
    "One Mile Lake": {"latitude": 50.312186, "longitude":  -122.801563},

    #Sechelt
    "Benner Beach": {"latitude": 49.463278, "longitude":  -123.739806},
    "Edgewater": {"latitude": 49.488765, "longitude":  -123.751524},
    "Porpoise Bay": {"latitude": 49.505163, "longitude":  -123.754071},
    "Sandy Hook": {"latitude": 49.523384, "longitude":  -123.774099},
    "Tuwanek": {"latitude": 49.546023, "longitude":  -123.764344},
    "Davis Bay - Sandbar": {"latitude": 49.439371, "longitude":  -123.724793},
    "Davis Bay - Pier": {"latitude": 49.445305, "longitude":  -123.729789},

    #Gibsons
    "Hopkins": {"latitude": 49.428350, "longitude":  -123.478935},
    "Soames": {"latitude": 49.415496, "longitude":  -123.488352},
    "Granthams": {"latitude": 49.412671, "longitude":  -123.493478},
    "Armours": {"latitude": 49.404840, "longitude":  -123.501526},
    "Breakwater Park": {"latitude": 49.397432, "longitude":  -123.504379},
    "Franklin": {"latitude": 49.391561, "longitude":  -123.509545},
    "Georgia": {"latitude": 49.393489, "longitude":  -123.501649},

    #Other
    "Keats Camp": {"latitude": 49.393535, "longitude":  -123.485476},

    #Powel River
    "Mowat Bay": {"latitude": 49.879268, "longitude":  -124.527270},

    #Reference Sites
    "West False Creek": {"latitude": 49.273884, "longitude":  -123.135334},
    "Central False Creek": {"latitude": 49.270339, "longitude":  -123.119173},
    "East False Creek": {"latitude": 49.273753, "longitude":  -123.106195},
    "Crab Park": {"latitude": 49.285372, "longitude":  -123.102368},
    "Brockton Point": {"latitude": 49.300931, "longitude":  -123.117076},
    "Garry Point": {"latitude": 49.124939, "longitude":  -123.196200},
    "Gibsons Harbor": {"latitude": 49.400678, "longitude":  -123.504908},
    "Snug Cove": {"latitude": 49.379602, "longitude":  -123.331591}
}



@app.route('/beach_ecoli_data', methods=['GET'])
def get_beach_data():

    #scrape beach data
    raw_beach_data = scraper.scrapeData()

    #calculate saftey based on ecoli level
    def calculate_saftey(EcoliCount) :
        if EcoliCount == "Pending":
            return "pending"
        if int(EcoliCount) <= 100:
            return "safe"
        elif int(EcoliCount) <= 200:
            return "caution"
        else:
            return  "unsafe"
        
    #get all beach saftey levels
    beach_data = []
    for beach in raw_beach_data:
        beach_ecoli_level = beach["ecoli_level"]
        beach["status"] = calculate_saftey(beach_ecoli_level)
        location = beach_locations.get(beach["name"], {})
        beach["longitude"] = location.get("longitude", -123.1207) #-123.1207
        beach["latitude"] = location.get("latitude", 49.2827)#49.2827
        beach_data.append(beach)
           
    
    #print(tabulate(beach_data, headers="keys", tablefmt="grid"))


    return jsonify(beach_data)

if __name__ == '__main__':
    app.run(debug=True)