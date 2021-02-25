import yaml

class Config:
    def __init__(self, path):
        try:
            with open(path, 'r') as file:
                self.config = yaml.full_load(file)
        except:
            raise FileNotFoundError(f"Cannot access {path}")
    
    def get(self, component):
        output = []
        if(isinstance(self.config[component], (str, float))):
            return self.config[component]
        else:
            for iter in range(len(self.config[component])):
                output.append(list(self.config[component][iter].values()))
            return output
        
# Debug
if __name__ == "__main__":
    conf = Config('config.yml')
    meals = conf.get("meals")
    starters = conf.get("starters")
    mealDeals = conf.get("mealDeals")
    deliveryFees = conf.get("deliveryFees")
    taxRate = conf.get("taxRate")
    splash = conf.get("splash")

