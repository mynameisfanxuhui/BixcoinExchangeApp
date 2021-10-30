class CCoin(object):

    def __init__(self, sSourceName, sType, fBuyPrice, fSellPrice):
        self.m_Name = sSourceName
        self.m_Type = sType
        self.m_BuyPrice = fBuyPrice
        self.m_SellPrice = fSellPrice

    def getName(self):
        return self.m_Name

    def getType(self):
        return self.m_Type

    def getBuyPrice(self):
        return self.m_BuyPrice

    def getSellPrice(self):
        return self.m_SellPrice

    def compare(self, bIsBuy):
        if bIsBuy:
            return self.m_BuyPrice
        else:
            return self.m_SellPrice


