#
myList = [1,2,3,4]
myDic = {"key":"value","key2":"value"}
myPhones = {"Iphone X":1000,"Sumsang S9":900}
print(myPhones)
Iphone_Prices = myPhones["Iphone X"]
#access dic keys
print("Iphone price: " + str(Iphone_Prices))
#change key values]
myPhones["Iphone X"] = 500
print(myPhones)
myPhones.clear()
print(myPhones)
print(dir(myPhones))



























