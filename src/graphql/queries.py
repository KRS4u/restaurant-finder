from src.graphql.client import run_query

def get_restaurants_by_cell_ids(cell_ids):
    query = '''
                query getRestaurantsByCellIds($cell_ids: [Int!]!){
                    restaurants (where: {
                        geometric_cell_id: { _in: $cell_ids}
                        }
                    ){
                            id
                            name
                            address
                            latitude
                            longitude
                            restaurant_rating {
                                rating
                            }
                    }
                }
            '''
    variables = {
        'cell_ids': cell_ids
    }
    restaurants = run_query(query, variables)
    return restaurants
