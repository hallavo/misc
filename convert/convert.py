import json, sys, codecs, copy

# 2017-07-24
# A script that takes a json file and outputs a modified json file
# (changes the structure and replaces null values with proper strings)

# sys.argv[0]   --   name of the python script
# sys.argv[1]   --   arg1
# sys.argv[2]   --   arg2
inputFile = sys.argv[1]
outputFile = sys.argv[2]

# read json file
with codecs.open(inputFile, 'r', encoding='utf8') as infile:
    data=infile.read()

# load json into a dict
dump = json.loads(data)
voucherDict = dump["vourcherList"] # Note: vou_R_cher (typo)

# create a modified json string
outJsonString = '{"vouchers":['
for voucher in voucherDict:
    lineList = voucher["voucherLines"]
    for transactionDict in lineList:
        newVoucher = copy.deepcopy( {**transactionDict, **voucher} )
        del newVoucher["voucherLines"]
        json_string = json.dumps(newVoucher)
        outJsonString += json_string
        outJsonString += ","
outJsonString += " {}]}"
outJsonString = outJsonString.replace(' null',' "thenullval"') #replace null values

# create a new dict
outJsonDict = json.loads(outJsonString)    

# write json file
with codecs.open(outputFile, 'w', encoding='utf8') as outfile:
    data = json.dumps(outJsonDict, ensure_ascii=False)
    outfile.write(data)
