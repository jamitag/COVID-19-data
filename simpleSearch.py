from baseClasses import Category as C

class Cuisine(C):
    """Defines search by cuisine
    """

    def __init__(self, api):
        C.__init__(self, api, "cuisine")

class Diet(C):
    """Defines search by cuisine
    """
    
    def __init__(self, api):
        C.__init__(self, api, "diet")

