# BUILDING LEXER

## Install python-devel
Ubuntu
```
sudo apt install python-dev
```

Fedora
```
sudo dnf install python-devel
```

## Install pipenv

Pip
```
pip install -user pipenv
```

Ubuntu
```
sudo apt install pipenv
```

Fedora
```
sudo dnf install pipenv
```

## Install dependencies

```
pipenv install -e .
```

## Start developing

Use the shell
```
pipenv shell
```

## Using CLI

Commands
-d --data
-f --files

```
./cli.py -d "data to analyse with lexer"
```

```
./cli.py -f "file path, default data.rb"
```
