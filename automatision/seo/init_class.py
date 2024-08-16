from position import GetPosition

class Init_class(GetPosition):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)  # Appelle le constructeur de GetPosition
        self.website_url = kwargs.get("website_url", None)
    
    def repeate(self):
        pass

    def getPageKeywordFromPlugins(self):
        pass
