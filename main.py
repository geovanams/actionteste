import requests
import json
#import argparse
import os

#parser = argparse.ArgumentParser(description="List Branches")
#parser.add_argument('--repos', help='This is parameter1', required=True)
#parser.add_argument('--owner', help='This is parameter1', required=True)


# r=requests.get("https://api.github.com/repos/"+parser.parse_args().owner+"/"+parser.parse_args().repos+"/branches", headers={"Accept": "application/vnd.github+json" ,"X-GitHub-Api-Version":"2022-11-28", "Authorization": "Bearer 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"})

#r=requests.get("https://api.github.com/repos/geovanams/hello-world-docker-action/branches", headers={"Accept": "application/vnd.github+json" ,"X-GitHub-Api-Version":"2022-11-28", "Authorization": "Bearer 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"})

# print(r.request.path_url)

# obj = (r.text)
# objeto = json.loads(obj)

# json_formatted_str = json.dumps(objeto, indent=2)
# print(json_formatted_str)

# for v in objeto:
#     print(v['name'])

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='Name of the user')
args = parser.parse_args()

print(f'Hello, {args.name}!')
