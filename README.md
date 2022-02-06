# restaurant-finder
  ### APIs ###
  1. #### /restaurants <br>
      #### query-params:  
        a. **filter**: column based on which we need to filter  
        b. **filter_value**: threshold value for the filter  
        c. **sort**: column based on whcih we need to sort  
        d. **lat**: latitude of the user  
        e: **long**: longitude of the user  
        
          
             
      #### response:
      **list of restaurants:**  
      `{
            "restaurants": [
              {  
                "address": {  
                  "city": "BLR"  
                },  
                "distance": 1070.73,  
                "id": "61eef6e2-397d-4a8c-a28b-d035ebd7fb7d",  
                "latitude": 15.9071006,  
                "longitude": 87.686002,  
                "name": "Xochi",  
                "rating": 3.6  
              },  
              {  
                "address": {  
                  "city": "BLR"  
                },  
                "distance": 0,  
                "id": "83fa2151-f023-4ed8-a472-f5752c0907cf",  
                "latitude": 15.9071006,  
                "longitude": 77.686002,  
                "name": "Brew",  
                "rating": 3.5  
              }  
            ]  
          }`
