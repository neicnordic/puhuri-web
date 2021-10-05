#!/usr/bin/env bash


client_id=""
client_secret=""



iss="https://proxy.myaccessid.org"
# acc environment
# iss="https://proxy.acc.myaccessid.org"

redirect_uri="http://localhost/cb"
scope="openid%20email%20profile%20eduperson_entitlement%20ssh_public_key%20offline_access"
nonce="wNQicdGYJFqILslhL9QMoFIl5cmu_yRwqBbu-L__Ce0"
state="sYNxtQgGxtQM1KV0mvXaMBKAenE"

if [ "x$client_id" = "x" ]; then
  echo "Please set the client_id"
  exit 1
fi

if [ "x$client_secret" = "x" ]; then
  echo "Please set the client_secret"
  exit 1
fi

clear
echo ""
echo "Copy the following URL and paste it in your browser:"
echo ""
echo "${iss}/OIDC/authorization?response_type=code&scope=${scope}&client_id=${client_id}&state=${state}&redirect_uri=${redirect_uri}&nonce=${nonce}&prompt=consent"
echo ""
echo "You will have to complete the authentication flow and a the end you will see an empty page."
echo "Copy the URL from the browser and paste below."
read -ep "URL: " url

code=`echo $url |awk -F"code=" '{print $2}' | awk -F"&" '{print $1}'`

curl $iss/OIDC/token -u "${client_id}:${client_secret}" -d "grant_type=authorization_code" -d "code=${code}" -d "redirect_uri=${redirect_uri}"
echo ""
