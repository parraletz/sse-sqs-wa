
## Requirements

- docker
- Enable ```"storage-driver": "overlay2"``` on /etc/docker/daemon.json

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```


Optional: Once the virtualenv is activated, you can install the required develoment dependencies.

```
$ pip install -r requirements-dev.txt


At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```
