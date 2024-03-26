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

if there is error "asyncpg.exceptions.InvalidPasswordError: password authentication failed for user "test_user"
"

change file "locate pg_hba.conf"
```
# "local" is for Unix domain socket connections only
local   all             all                                     md5 
```

`sudo systemctl restart postgresql`