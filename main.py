import requests
import json
import sys

r=requests.get("https://api.github.com/repos/"+sys.argv[1]+"/"+sys.argv[2]+"/branches", headers={"Accept": "application/vnd.github+json" ,"X-GitHub-Api-Version":"2022-11-28", "Authorization": "Bearer "+sys.argv[3]})

obj = (r.text)
objeto = json.loads(obj)

print("\n"+sys.argv[2]+ " repo branches:")
for v in objeto:
    print(v)
    print(v['name'])

print("\nBranches Details:")
json_formatted_str = json.dumps(objeto, indent=2)
print(json_formatted_str)
