cp ~/.minikube/ca.key .
cp ~/.minikube/ca.crt .

openssl genrsa -out shivam.key 2048

openssl req -new -key shivam.key -subj "/CN=shivam/O=system:nodes" -out shivam.csr

openssl x509 -req -in shivam.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out shivam.crt -days 365

cp ~/.kube/config  shivam.kubeconfig


openssl genrsa -out vinay.key 2048

openssl req -new -key vinay.key -subj "/CN=vinay/O=system:nodes" -out vinay.csr

openssl x509 -req -in vinay.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out vinay.crt -days 365



# UI group 
openssl genrsa -out swedha.key 2048

openssl req -new -key swedha.key -subj "/CN=swedha/O=UI" -out swedha.csr

openssl x509 -req -in swedha.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out swedha.crt -days 365