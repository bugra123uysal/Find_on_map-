import requests

key=""
def find_place(query ,location=None , radius=None ):


   url="https://maps.googleapis.com/maps/api/place/textsearch/json"
   
   istekler={
       "query":query ,
       "key":key , 

   }
   """ enlem boylam """
   if location:
     istekler["location"] = location
   if radius:
     istekler["radius"] = radius
 
   response=requests.get(url , params=istekler)
   result=response.json()
 
   if result["status"] == "OK":
     for place in result["results"]:
         name=place["name"]
         addres= place.get("formatted_address", "bilgi yok")
         print(f"yer: {name}, Adres: {addres}" )
   else:
     print("tekrar deneyiniz sonuç bulunamadı: ", result["status"])
query="amerika wasington deki white house"
find_place(query)
