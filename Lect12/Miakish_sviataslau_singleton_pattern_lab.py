class Singelton:
    __instance = None

    def __init__(self):
        if Singelton.__instance is None:
            Singelton.__instance = self
        else:
            raise Exception("The class is a singleton")
    

    @staticmethod
    def get_instance():
        if Singelton.__instance is None:
            return Singelton()
        return Singelton.__instance
    
    @staticmethod
    def useful_function():
        return 42

if __name__ == "__main__":
    singelton_obj = Singelton()
    print(singelton_obj)

    print(singelton_obj.get_instance())
    print(singelton_obj.get_instance())
    print(singelton_obj.get_instance().useful_function)
    print(Singelton())