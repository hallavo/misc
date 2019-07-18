import json, sys, codecs, copy

# sys.argv[0]   --   name of the python script
# sys.argv[1]   --   arg1
# sys.argv[2]   --   arg2

inputFile = sys.argv[1]
outputFile = sys.argv[2]


# read file
with codecs.open(inputFile, 'r', encoding='utf8') as infile:
    data=infile.read()

# parse file
dump = json.loads(data)
voucherDict = dump["vourcherList"] # Note: vou_R_cher

outJsonString = '{"vouchers":['
for voucher in voucherDict:
    lineList = voucher["voucherLines"]
    for transactionDict in lineList:
        newVoucher = copy.deepcopy( {**transactionDict, **voucher} )
        del newVoucher["voucherLines"]
        #del newVoucher["reference"]
        #del newVoucher["addressid"]

        json_string = json.dumps(newVoucher)
        outJsonString += json_string
        outJsonString += ","
        #print(json_string)
        #print(newVoucher)
        #print('\n')

outJsonString += " {}]}"
outJsonString = outJsonString.replace(' null',' "thenullval"')
outJsonDict = json.loads(outJsonString)    
#obj2 = json.dumps( obj["vourcherList"] )
#print(obj["vourcherList"])


# write file
with codecs.open(outputFile, 'w', encoding='utf8') as outfile:
    data = json.dumps(outJsonDict, ensure_ascii=False)
    outfile.write(data)
