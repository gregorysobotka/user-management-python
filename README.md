# user-management-python

## Requirements

- Python version (3.7)


## Getting Started

1. Using [pipenv](https://github.com/pypa/pipenv), run the following command ... 
```
pipenv shell
```
2. Run one of the following commands (see below)


### List Users

```
python listusers.py --h=user@ec2-55-555-555-555.compute-1.amazonaws.com
```

### Add User

```
python adduser.py --h=user@ec2-55-555-555-555.compute-1.amazonaws.com --c="Example coment 1" --u=exu1 --pk="..."
```

### Remove User

```
python removeuser.py --h=user@ec2-55-555-555-555.compute-1.amazonaws.com --u=exu1
```
