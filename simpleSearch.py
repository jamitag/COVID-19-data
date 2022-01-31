from baseClasses import Category as C
"""
Searching by cuisine
"""
class Cuisine(C):
    def __init__(self, api):
        C.__init__(self, api, "cuisine")

"""
Searching by diet
"""
class Diet(C):
    def __init__(self, api):
        C.__init__(self, api, "diet")

