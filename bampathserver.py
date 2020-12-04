from flask import Flask, request
application = Flask(__name__)

delim = "\t"

responseHeader = "##FILE_TYPE=bam##"+"\n"+delim.join(["id","path"])+"\n"

def loadBamLocationTable():
    with open("bamfileTable.txt", "r") as f:
        res = {k:v for (k,v) in [l.strip().split(delim) for l in f]}
    return res

bamLocs = loadBamLocationTable()

@application.route('/bam')
def getBam():
    sampleId = request.args.get("sample")
    if not sampleId in bamLocs:
        return responseHeader
    bamPath = bamLocs.get(sampleId)
    return responseHeader + delim.join([sampleId, bamPath])

if __name__ == "__main__":
  application.run(host='0.0.0.0')
