import os
from box.exceptions import BoxValueError
import yaml
from customCNNClassifier import logger
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any, List, Dict
import base64


def read_yaml(path_to_yaml: str) -> ConfigBox:
    """
    Reads yaml file and returns a Box object. Consider box object as a dictionary.

    Args:
        path_to_yaml - yaml file path

    Raises:
        ValueError - if Yaml file is Empty

    Returns:
        ConfigBox: Box object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            yaml_content = yaml.safe_load(yaml_file)
            logger.info("Configuations from yaml file loaded")
            return ConfigBox(yaml_content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e


def create_directories(path_to_directories: List[str], verbose: bool = True) -> None:
    """
    This function creates directories provided in a list.

    Args:
        path_to_directories - list of strings containing path variables
        verbose(default: True) - Log this information
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")


def save_json(path: str, data: Dict) -> None:
    """
    Save data into a json file.

    Args:
        path - location at which this json will be saved
        data - data to be save to json file
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"File saved to disk - present at {path}")


def load_json(path: str) -> ConfigBox:
    """
    Load data from a JSON file.

    Args:
        path: json file path 

    Raises:
        ValueError - if json file is empty
    
    Returns:
        ConfigBox object type
    """
    try:
        with open(path, 'r') as f:
            content = json.load(f)
            logger.info("Json file succesfully loaded.")
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Json file is Empty")


def save_bin(data: Any, path: str) -> None:
    """
    Save data into a binary file.

    Args:
        data - any data 
        path - file path
    """
    joblib.dump(value=data, filename=path)
    logger.info("Saving data into binary file format.")


def load_bin(path: Path) -> Any:
    """
    Load data from binary file format.

    Args:
        path - Path of the binary file
    
    Returns:
        data stored in binary file
    """
    data = joblib.load(path)
    logger.info("Binary file loaded.")
    return data


def get_size(path: Path) -> int:
    """
    Get Size of the file in KB.

    Args:
        path - Path of the file
    
    Returns:
        size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return size_in_kb


def decode_image(imgStr: str, filename: str) -> None:
    """
    This function decodes a base64 image and writes it into a file.

    Args:
        imgStr - base64 image string
        filename - destination file location
    """
    image_data = base64.decode(imgStr)
    with open(filename, 'w') as f:
        f.write(image_data)
        f.close()


def encode_image(image_path: str) -> base64.encode:
    """
    This function encodes data into base64 format.

    Args:
        image_path - path to the image file

    Returns:
        return the base64 encoded string
    """
    with open(image_path, 'r') as f:
        return base64.encode(f.read())


if __name__ == "__main__":
    create_directories(["artifacts"])
