import json
from typing import Union, List, Dict
from pathlib import Path

current_path = Path(__file__)


def read_json(
    filename: str,
) -> Dict[str, Union[Dict[str, Dict[str, Dict[str, int]]], List[str]]]:
    filepath = current_path.parent / filename
    with filepath.open() as f:
        return json.load(f)


def list_tables() -> Dict[str, List[str]]:
    """

    :return: Dict of table, columns
    :rtype: List[Dict[str,List[str]]]
    """
    return read_json("tables_config.json")


def list_roles() -> Dict[str, Dict[str, Dict[str, Dict[str, int]]]]:
    """
    get all the roles for a user
    :return: Dict["table_name":{"standard":{},"specific":{}}
    :rtype:Dict[str, Dict[str, Dict[str, Dict[str, int]]]]
    """
    return read_json("roles_config.json")
