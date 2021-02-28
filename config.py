import yaml     # Import PyYAML to parse the config

class Config:
    def __init__(self, path):
        self.path = path
        try:
            with open(self.path, 'r') as file:
                self.config = yaml.full_load(file)              # Parse the config file into a large dictionary
        except:
            raise FileNotFoundError(f"Cannot access {path}")    # Return a FileNotFoundError error if the config file can't be accessed 
    
    def get(self, component):
        output = []
        try:
            for iter in range(len(self.config[component])):
                output.append(list(self.config[component][iter].values()))
            return output
        except KeyError:                                        # If the component can't be found in the parsed data, return an error message
           f"Cannot find '{component}' in '{self.path}'"        
        except:
            return self.config[component]