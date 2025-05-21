class MurderStatsManager:
    def __init__(self):
        self.data = {
    "Europe":{
        "Estonia":{
            "Tallinn":{
                "murders":[5]
                }
            }
        },
    "Europe2":{
        "Finland":{
            "Helsinki":{
                "murders":[3]
                }
            }
        },
    "Asia":{
        "Japan":{
            "Tokyo":{
                "murders":[8]
                }
            }
        }
    }
        
    
    def add_data(self, continent, country, city, count):
        keys = [continent, country, city]
        current =self.data
        
        for key in keys:
            if key not in current:
                current[key]={}
                current=current[key]
            if "murders" not in current:
                current["murders"]=[]
                current["murders"].append(count)
                
        
        
    
    def get_stats(self):
        return self.data
        
    
    
    
    
    

manager=MurderStatsManager()
manager.add_data( "Europe","Estonia","Tallinn",4)
print(manager.get_stats())