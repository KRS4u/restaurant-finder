from geopy import distance
from flask import jsonify
from faker import Faker

from src.graphql.queries import get_restaurants_by_cell_ids

fake = Faker()

def _get_cell_id(lat, long):
    return 0


def _find_nearby_cells(cell_id, depth):
    return fake.random_elements(elements=[x for x in range(17,30) ])


def _get_nearby_cells(lat, long):
    cell_id = _get_cell_id(lat, long)
    return _find_nearby_cells(cell_id, 5)


def _filter_restaurants(restaurants, element, val):
    if element == 'distance':
        return list(filter(lambda x: x['distance']<=float(val), restaurants))
    elif element == 'rating':
        return list(filter(lambda x: x['rating']>=float(val), restaurants))
    return restaurants


def _sort_restaurants(restaurants, element):
    if element == 'rating':
        restaurants.sort(key = lambda x: x.get(element), reverse=True)
    else:
        restaurants.sort(key = lambda x: x.get(element), reverse=False)
    return restaurants



def _enrich_restaurants(restaurants, lat, long):
    coords_1 = (lat, long)
    for res in restaurants:
        coords_2=(res.get('latitude'), res.get('longitude'))
        res['distance']=round(distance.distance(coords_1, coords_2).km, 2)
        res['rating'] = res['restaurant_rating']['rating']
        del res['restaurant_rating']
    return restaurants

def get_nearby_restaurants(args):
    filter_element = args.get('filter')
    filter_value = args.get('filter_value')
    sort_element = args.get('sort')
    lat = float(args.get('lat'))
    long = float(args.get('long'))
    cells = _get_nearby_cells(lat, long)
    restaurants = get_restaurants_by_cell_ids(cells).get('restaurants')
    if lat is None or long is None:
        raise Exception('Invalid location')
    restaurants = _enrich_restaurants(restaurants, lat, long)
    if filter_element is not None:
        if filter_value is None:
            raise Exception('Invalid Filter Value')
        restaurants = _filter_restaurants(restaurants, filter_element, filter_value)
    if sort_element is not None:
        restaurants = _sort_restaurants(restaurants, sort_element)
    return jsonify({'restaurants': restaurants })
