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
    resDict = {}
    for iPos, oCoin in enumerate(dataList):
        iRecommend = 0
        # recommand first element
        if iPos == 0:
            iRecommend = 1
        if bIsBuy:
            resDict[oCoin.getName()] = {"buyPrice": oCoin.getBuyPrice(), "recommend": iRecommend}
        else:
            resDict[oCoin.getName()] = {"sellPrice": oCoin.getSellPrice(), "recommend": iRecommend}
    return resDict
