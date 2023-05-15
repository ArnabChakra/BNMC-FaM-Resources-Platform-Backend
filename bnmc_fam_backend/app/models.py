from app import app,collection
from app.utils import get_zips

def get_categories():
    set_cat=set(())
    for cat in collection.find({},{'_id':0,'Category':1}):
        if cat['Category']!="":
            set_cat.add(cat['Category'])
    return list(set_cat)

def get_resources(category,resource,zip,distance):
    query={'CoalitionMember': False}
    query_coalition={'CoalitionMember': True}
    if category!="":
        query['Category'] = category
        query_coalition['Category'] = category
    if zip!="":
        if distance==0:
            query['Zipcode'] = zip
        else:
            zip_list=get_zips(zip,distance)
            query['Zipcode'] = {"$in": zip_list}

    try:
        return list(collection.find(query)),list(collection.find(query_coalition))

    except Exception as e:
        return e