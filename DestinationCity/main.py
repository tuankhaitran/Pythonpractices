class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # Our destination will be one of the value in the index 1. Other places will have a pair with them accept the very start point which will be at index [0]
        # So the destination will be the one that exist inside the list of index [1] and does not have a pair in the list of index [0] 
        
        endSet=set([ i[1] for i in paths]) # Take all the second element of the lists and put into endList
        startSet=set([ i[0] for i in paths]) # Take all the first element of the lists and put into startList
        
        resultset=endSet-startSet # This is a set so I need to change back to list so that we can return a string value

        return list(resultset)[0]
       