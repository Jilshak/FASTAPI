# path parameters

# to get route
# app.get('/items)
# async def get_list_items():
    # return {"Message":"this is the list items"}


# @app.get('/items/{item_id}')
# async def get_item(item_id : int):
#     return {"item_id": item_id}

# >>> A PATH PARAMETER IS ADDED IN THE app.get('/items/{item_id}) ---> this is a path parameter
        # > it also has to be mentioned in the async def get_item(item_id: id) --> for it to be accessible
# >>> on the other hand a query parameter is not added in teh app.get() it is only added in the function

# > here what we are doing is that we are getting a particular item id
#  > we then pass it tot the function as a parameter
# > and then we return the item_id 
#  >> Now we have to note here that by default we will get a string as the output for the item id. so the pydantic plays a role here
#  >> instead of string we explicitly mentioned a int here ie; (item_id: int) --> this will return an int
# > now if we were to pass an string here it will throw an error


# NOTE:
    # YOU HAVE TO PUT AN SPECIFIC END POINT BEFORE AN DYNAMIC END POINT OTHERWISE IT MIGHT GO TO THE DYNAMIC ENDPOINT MATCHING THE DATA GIVEN
    # IT STRATS FROM THE TOP AND CHECKS WHETHER THE ROUTE IS MATCHING THE CURRENT ROUTE IF IT MATCHES IT WILL GIVE OUTPUT OF THAT ROUTE INSTEAD OF THE DESIRED ROUTE