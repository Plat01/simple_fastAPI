# FastAPI exampl

## Run without docker

### Create and install requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Create postgres database

```bash
sudo -u postgres psql
```

```postgresql
CREATE USER test_user WITH ENCRYPTED PASSWORD 'qwerty';
CREATE DATABASE test_db OWNER test_user;
```
