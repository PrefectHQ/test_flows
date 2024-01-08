FROM prefecthq/prefect:2.14.12-python3.10
COPY . /opt/prefect/test_flows/
WORKDIR /opt/prefect/test_flows/
