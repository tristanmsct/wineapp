# Wineapp



A wine quality prediction app (mostly a mlflow + fastapi in docker tutorial).



# How to deploy



From the root folder.

```bash
docker compose up
```



# Set-up the project



## Set-up the script environent



From the `script` directory.

```bash
python -m venv .venv
source .venv/bin/activate
poetry install --no-root
```



Fill up the database.

```bash
python fill_db.py
```



Train a model.

```bash
python train_model.py
```



Test the api (might need to restart the api).

```bash
python test_api.py 10
```





