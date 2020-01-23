import json


def get_card_useful_payload(**kwparams):
    card_useful_payload = {
        "userId": "646",
        "cardId": "1",
        "rating": 1,
        "platform": 0,
        "suggestion": "Test Suggestion Api",
        "mapTo": "CARDUSEFULSUGGESTION"
    }

    for key in kwparams.keys():
        card_useful_payload[key] = str(kwparams[key])

    return card_useful_payload


def get_regional_performance_payload(params):
    inp = "tenantId: 1, regionTypeId: 1, regionId: 1, parentRegionId: null,  tenantLocationId: -2, " \
          "locationGroupId: -2, productId: -2, userId: 10195, isCardService: true, isCompare: false, " \
          "masterLocationSelected: true, metricsDateType: Departure, groupBy: DateRange, dimensionSet: [1, 2], " \
          "contestReportId: -2, contestReportIntervalId: 0, discussionTopicId: -2, discussionSubTopicId: -2, " \
          "performanceLeaderId: -2, regionByTypeDataID: -1, compareRegionByTypeDataID: null, marketSegment1: null, " \
          "marketSegment2: null, reservationType: null, FPGUserToggle: 0, platformFilter: all, " \
          "actualAverageCurrencyConversion: null, compareAverageCurrencyConversion: null, useMondrian: false, " \
          "isPreview: null, status: 0, searchWord: null, displayDimension: Region, filterDimension: [TenantLocation], " \
          "regionFilter: null, quotedCurrency: \"USD\", from: \"2019-10-01\", to: \"2019-10-22\", " \
          "fromDateTime: \"1569868200000\", toDateTime: \"1571731323335\", " \
          "cardVariance: MTD, reportCodes: [\"REGIONAL_IR\", \"BLUEPRINT_SCORE_REGION\"]"
    inp_list = inp.split(',')

    for item in params:
        x=[y.strip() for y in item.split(':')]
        for i in range(len(inp_list)):
            if x[0] in inp_list[i]:
                inp_list[i] = item
    #print(','.join(inp_list))

    rp_payload = {
        "query": "query {getRegionalPerformanceData(input: {"
                 + ','.join(inp_list) +
                 "}){regionId, regionName, avgBlueprintScore, minimumStandard, "
                 "incrementalRevenue, revenueConverted, month, year, regionList}}"
    }

    return rp_payload

