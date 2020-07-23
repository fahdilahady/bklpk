import requests

def test1A_getUsersData():
    resp = requests.get('https://jsonplaceholder.typicode.com/posts')
    respDict = resp.json()

    if resp.status_code != 200:
        #This means something went wrong on the end point.
        raise ApiError('GET /users/ {}'.format(resp.status_code))

    for elem in range(len(respDict)):
        _userId = respDict[elem].get('userId')
        _id = respDict[elem].get('id')
        _title = respDict[elem].get('title')
        _body = respDict[elem].get('body')
        assert type(_userId) is int, "userId data type must int on object index:%d" % elem 
        assert type(_id) is int , "Id data type must int  on object index:%d" % elem 
        assert type(_title) is str, "title data type must string on object index:%d" % elem 
        assert type(_body) is str, "body data type must string on object index:%d" % elem 


def test1B_postUsersData(_title, _body, _userId):
    dataExpect = {
        "title": _title,
        "body": _body,
        "userId": _userId
    }
    resp = requests.post('https://jsonplaceholder.typicode.com/posts',dataExpect)
    respDict = resp.json()
    for key in dataExpect:
        assert type(respDict.get(key)) == type(dataExpect.get(key)), "unmatch data type on %s, %s vs %s" %(key,type(respDict.get(key)), type(dataExpect.get(key)))
        assert respDict.get(key) == dataExpect.get(key), "expected title is %s, Given %s" %(dataExpect.get(key), respDict.get(key))
   
if __name__ == "__main__":
    test1A_getUsersData()
    print("User Data type testing passed")


    test1B_postUsersData("recommendation", "motorcycle", 12) #AssertionError: unmatch data type on userId, <class 'str'> vs <class 'int'>
    print("Post User Data testing passed")
