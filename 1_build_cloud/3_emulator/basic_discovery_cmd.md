
* Pysical RaspberryPi
```
python basic_discovery.py \
  --thing_name GreengrassClientDevice1 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client Device 1!' \
  --ca_file ./certificates/rootCA.pem \
  --cert ./certificates/thingCert.crt \
  --key ./certificates/privKey.key \
  --region us-east-1 \
  --verbosity Warn
```

* vehicle_0 inside docker

```
python basic_discovery.py \
  --thing_name vehicle_0 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client vehicle_0!' \
  --ca_file ./certificates/rootCA.pem \
  --cert ./certificates/vehicle_0_cert.pem \
  --key ./certificates/vehicle_0_private.key \
  --region us-east-1 \
  --verbosity Warn
```

* vehicle_1 inside docker

```
python basic_discovery.py \
  --thing_name vehicle_1 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client vehicle_1!' \
  --ca_file ./certificates/rootCA.pem \
  --cert ./certificates/vehicle_1_cert.pem \
  --key ./certificates/vehicle_1_private.key \
  --region us-east-1 \
  --verbosity Warn
```

* vehicle_2 inside docker

```
python basic_discovery.py \
  --thing_name vehicle_2 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client vehicle_2!' \
  --ca_file ./certificates/rootCA.pem \
  --cert ./certificates/vehicle_2_cert.pem \
  --key ./certificates/vehicle_2_private.key \
  --region us-east-1 \
  --verbosity Warn
```

* vehicle_3 inside docker

```
python basic_discovery.py \
  --thing_name vehicle_3 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client vehicle_3!' \
  --ca_file ./certificates/rootCA.pem \
  --cert ./certificates/vehicle_3_cert.pem \
  --key ./certificates/vehicle_3_private.key \
  --region us-east-1 \
  --verbosity Warn
```

* vehicle_4 inside docker

```
python basic_discovery.py \
  --thing_name vehicle_4 \
  --topic 'clients/GreengrassClientDevice1/hello/world' \
  --message 'Hello World from Client vehicle_4!' \
  --ca_file ./certificates/rootCA.pem \
  --cert ./certificates/vehicle_4_cert.pem \
  --key ./certificates/vehicle_4_private.key \
  --region us-east-1 \
  --verbosity Warn
```
