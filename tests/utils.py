import logging
import os
from datetime import datetime, timedelta
from typing import List, Dict

import boto3

from analytics_worker.config import Config

logger = logging.getLogger(__name__)

def get_aws_access_key_id() -> str:
    return os.environ.get('AWS_ACCESS_KEY_ID')

def get_aws_secret_access_key() -> str:
    return os.environ.get('AWS_SECRET_ACCESS_KEY')

def get_region() -> str:
    return os.environ.get('AWS_REGION')

def get_s3_client() -> boto3.client:
    aws_access_key_id = get_aws_access_key_id()
    aws_secret_access_key = get_aws_secret_access_key()
    region_name = get_region()
    return boto3.client('s3', aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key,
                        region_name=region_name)

def get_boto3_client(service_name: str, region_name: str = None) -> boto3.client:
    if region_name:
        return boto3.client(service_name, region_name=region_name)
    else:
        return boto3.client(service_name)

def get_config() -> Config:
    return Config()

def get_config_value(key: str, default_value: str = None) -> str:
    config = get_config()
    return config.get(key, default_value)

def get_today() -> datetime:
    return datetime.now()

def get_yesterday() -> datetime:
    return get_today() - timedelta(days=1)

def get_date_str(date: datetime, format: str = '%Y-%m-%d') -> str:
    return date.strftime(format)

def get_list_from_string(input_str: str, delimiter: str = ',') -> List[str]:
    return input_str.split(delimiter)

def get_dict_from_json(json_str: str) -> Dict:
    import json
    return json.loads(json_str)

def get_json_from_dict(input_dict: Dict) -> str:
    import json
    return json.dumps(input_dict)