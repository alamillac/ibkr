# IBKR

## Description

Example of connection to IBKR

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Credentials

Create a file called `.env` in the root directory of the project with the following content:

```bash
TWS_USERID=your_username
```

Create a file called `pass/tws_password.txt` in the `pass` directory of the project with the following content:

```bash
your_password
```

## Usage

```bash
# Run ib-gateway
docker compose up

# Run main.py
source venv/bin/activate
python3 main.py
```
