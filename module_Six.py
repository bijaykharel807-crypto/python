a=["sudan","khan"]
print(len(a))
data={
    "Fname":"Sudan",
    "Lname":"Khan",
}
print(data)
print(type(data))
print(len(data))
print(data["Fname"])
print(data["Fname"])
print(data.keys())
print(data.values())


test ={
    "name":"sudan",
    "address":["nepal","india","china"],

    
}
test["number"]="1"
test["address"]=1
print(test)


data1={
    "message":"hello world"

}
data1.update({"message":"ali ","age":22, "city":"peshawar", "weight":70, "religion":"islam" } )
print(data1)



#data deleting ways form dict
del data1["message"]
print(data1)

#pop
data1.pop("age")
print(data1)
#popitem
data1.popitem()
print(data1)    

person={
    "name":"sudan",
    "age":22,
    "city":"peshawar",
    "skill":"python",
    "is_employed":False,
    "phone":[{
        "type":"ntc",
        "number":"1234567890"
    }
    ,{
        "type":"ncell",
        "number":"0987654321"
    }]
}
print(person["name"],person["phone"][0]["type"],"number is",person["phone"][0]["number"])
print(person["name"],person["phone"][1]["type"],"number is",person["phone"][1]["number"])


teachers=["Nasir","Ali","Ahmed" ,"Omer",  "Saeed","Zia","Salman","Usman"]
teachers.sort(reverse=True)
print(teachers)



