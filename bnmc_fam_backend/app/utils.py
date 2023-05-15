from uszipcode import SearchEngine
from thefuzz import fuzz

def get_zips(zip,radius):
    search = SearchEngine()
    results = search.by_zipcode(zipcode=zip)
    result = results.to_dict()
    if result is not None:
        lat = result['lat']
        lng = result['lng']
        print(zip)
        print(lat)
        print(lng)
        print(radius)
        nearby_zipcodes = search.by_coordinates(lat=lat, lng=lng, radius=int(radius), returns=100)#, ascending=True)
        return [zip.to_dict()['zipcode'] for zip in nearby_zipcodes]
    return []

def fuzzy_match_resource(res_name,res_list,threshold):
    final_res_list=[]
    for res in res_list:
        if fuzz.token_set_ratio(res_name, res['ResourceName'].lower()) >= threshold:
            final_res_list.append(res)

    return final_res_list
