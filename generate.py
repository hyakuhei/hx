import sys, copy

import yaml

# Go through the yaml, look for any values starting with $ and then try to replace
# them with a corresponding environment variable of the same name.
def searchAndReplaceStatics(parent: dict, vars: dict):
    for k,v in parent.items():
        if isinstance(v, str):
            if v in vars:
                parent[k] = vars[v]
            for vk in vars.keys():
                if vk in v:
                    parent[k] = v.replace(vk,vars[vk])
                    print(f"Replaced with {vars[vk]}")
        
        if isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    searchAndReplaceStatics(i, vars)

        if isinstance(v, dict):
            searchAndReplaceStatics(v, vars)


if len(sys.argv) !=3:
    print(f"Usage: python3 generate.py domains.txt templates/deployment.yaml")
    sys.exit(1)

outYaml = None

# Read the domains.yaml


# Read the given template yaml
# Check user has set corresponding environment variables

subjects = None
outDocs = []
staticDoc = None

with open(sys.argv[1]) as f:
    subjects = yaml.load(f, Loader=yaml.FullLoader)
    print(subjects)

with open(sys.argv[2]) as f:
    data = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in data:
        #Update doc to create a static template with replaced vars
        searchAndReplaceStatics(doc, subjects["staticVars"])
        staticDoc = doc
        #print(doc)

if "iterableVars" in subjects:
    for iv in subjects["iterableVars"]:
        for x in subjects[iv]:
            print(x)
            tempDoc = copy.deepcopy(staticDoc)
            searchAndReplaceStatics(tempDoc, {iv:x})
            outDocs.append(tempDoc)

    print(yaml.dump_all(outDocs))
else:
    print(yaml.dump(staticDoc))


###
if False:
    d = {}
    d['iterableVars'] = ['$DOMAINS']
    d['$DOMAINS'] = ["example.org", "example.com"]
    d['vars'] = {
        "$IMAGENAME": "kali-linux",
        "$VOLUME-ID": "0xff33-eeeeadf-adfadfa-adfafdsa"
    } 

    print(yaml.dump(d))