
class boat:
    #constructor
    def __init__ (self, ID, latitude, longitude):
        """
        Docstring for __init__
        
        :param ID: boatID
        :param latitude: Latitude coordinate
        :param longitude: Longitude coordinate
        """

        self.__id = ID
        self.__latitude = latitude
        self.__longitude = longitude

    def get_id(self) -> int:
        """
        Docstring for get_id
        :return: boatID [positive integer]
        """

        return self.__id
    
    def get_latitude(self) -> float:
        """
        Docstring for get_latitude
        :return: Latitude coordinate [return values between -90 and 90]
        """

        return self.__latitude
    
    def get_longitude(self) -> float:
        """
        Docstring for get_longitude
        :return: longitude coordinate [return values between -180 and 180]
        """

        return self.__longitude
    
    def get_location(self) -> tuple:
        """
        Docstring for get_location
        :return: Latitude & longitude coordinates in a tuple
        """

        return (self.__latitude, self.__longitude)
    
    def set_latitude(self, latitude: float):
        """
        Docstring for set_latitude
        
        :param latitude: latitude coordinate [must be between -90 and 90]
        :type latitude: float
        """

        if latitude < -90.00 or latitude > 90.00:
            raise ValueError("Latitude must be between -90 and 90.")
        else:
            self.__latitude = latitude

    def set_longitude(self, longitude: float):
        """
        Docstring for set_longitude
        
        :param longitude: longitude coordinate [must be between -180 and 180]
        :type longitude: float
        """

        if longitude < -180.00 or longitude > 180.00:
            raise ValueError("Longitude must be between -180 and 180.")
        else:
            self.__longitude = longitude
    

    #method override
    def __eq__ (self, other: 'boat') -> bool:
        """
        Docstring for __eq__
        
        :param other: Other boat object to compare
        :type other: 'boat'
        :return: Returns True if both boat objects have the same ID, False otherwise
        :rtype: bool
        """

        if isinstance(other, boat):
            return self.__id == other.__id  # Compare based on boat ID
        return False

    def __str__ (self) -> str:
        """
        Docstring for __str__
        
        :return: String representation of the boat object
        :rtype: str
        """

        return f"Boat ID: {self.__id}, Latitude: {self.__latitude}, Longitude: {self.__longitude}"