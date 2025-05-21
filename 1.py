class MurderStatsManager:
    def __init__(self):
        self.data = {}
        
    
    def add_data(self, continent, country, city, count):
        self.data[continent][country][city]["murders"].append(count)
        
    
    def get_stats(self):
        pass
        
    
    
    
    
    
allMurders = {
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
manager=MurderStatsManager()

print(allMurders["Europe"]["Estonia"]["Tallinn"]["murders"])