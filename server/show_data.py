import get_data


def showData():
    dataList = get_data.get_rates()
    bitcoinList = []
    ethList = []
    for oCoin in dataList:
        if oCoin.getType() == "bitcoin":
            bitcoinList.append(oCoin)
        elif oCoin.getType() == "eth":
            ethList.append(oCoin)
        else:
            print("error occured, no suitable type and type is", oCoin.getType())
    resDict = {}
    resDict["BitcoinBuy"] = extractInfo(bitcoinList, True)
    resDict["EthBuy"] = extractInfo(ethList, True)
    resDict["BitcoinSell"] = extractInfo(bitcoinList, False)
    resDict["EthSell"] = extractInfo(ethList, False)
    return resDict



def extractInfo(dataList, bIsBuy):
    # cheaper buy price is better, higher sell price is better
    bReverse = False
    if not bIsBuy:
        bReverse = True
    dataList.sort(key=lambda x: x.compare(bIsBuy), reverse=bReverse)
    resList = []
    for iPos, oCoin in enumerate(dataList):
        sRecommend = "No"
        # recommand first element
        if iPos == 0:
            sRecommend = "Yes"
        if bIsBuy:
            resList.append({"source": oCoin.getName(), "buyPrice": oCoin.getBuyPrice(), "recommend": sRecommend})
        else:
            resList.append({"source": oCoin.getName(), "sellPrice": oCoin.getSellPrice(), "recommend": sRecommend})
    return resList
