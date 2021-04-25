import requests
import json

def getAssetPairs(url):
    #assetUrl = "https://api.kraken.com/0/public/AssetPairs"
    assetResponse = requests.get(url)
    assetData = assetResponse.text
    assetFeed = json.loads(assetData)
    keyList = assetFeed["result"].keys()
    return keyList


def getPrices(pair):
    url = "https://api.kraken.com/0/public/Ticker?pair=" + pair
    priceResponse = requests.get(url)
    priceData = priceResponse.text
    priceFeed = json.loads(priceData)

    askPrice = priceFeed["result"][pair]["a"]
    bidPrice = priceFeed["result"][pair]["b"]
    dayLow = priceFeed["result"][pair]["l"]
    dayHigh = priceFeed["result"][pair]["h"]
    dayOpen = priceFeed["result"][pair]["o"]

    #print("Trading pair: " + pair)
    #print("Ask price: " + askPrice[0])
    #print("Bid price: " + bidPrice[0])
    return [askPrice[0], bidPrice[0]]

def printList(input):
    input = list(input)
    for i in range(len(input)):
        print(input[i])
    return

def main():
    pairList = getAssetPairs("https://api.kraken.com/0/public/AssetPairs")
    #printList(pairList)
    print(getPrices("ETHDAI"))
    return


main()