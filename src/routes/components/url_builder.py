class UrlBuilder:

    def __init__(self) -> None:
        self.__base_uri = "/"
        self.__api_uri = self.__base_uri + "api/"
        self.__health_uri = self.__api_uri + "health/"
        self.__planet_uri = self.__api_uri + "planet/"
        self.__planet_by_name_uri = self.__api_uri + "planet_name/"
        self.__planet_by_id_uri = self.__planet_uri + "{planet_id}/"

    @property
    def health_uri(self) -> str:
        return self.__health_uri

    @property
    def planet_uri(self) -> str:
        return self.__planet_uri

    @property
    def planet_by_id_uri(self) -> str:
        return self.__planet_by_id_uri

    @property
    def planet_by_name_uri(self) -> str:
        return self.__planet_by_name_uri
