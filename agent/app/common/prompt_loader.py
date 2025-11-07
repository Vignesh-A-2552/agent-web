from typing import Any, Dict
import os
import yaml

def load_prompt_config(config_path: str) -> Dict[str, Any]:
    """
    Load a prompt configuration from a YAML file in the prompts directory.

    Args:
        config_path: Name of the YAML configuration file.

    Returns:
        Dictionary containing the parsed YAML configuration.

    Raises:
        FileNotFoundError: If the configuration file cannot be found.
        yaml.YAMLError: If the YAML file is malformed or cannot be parsed.
    """
    config_path = os.path.join("prompts", config_path)
    return load_config(config_path)

def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load the ticket classifier configuration from a YAML file.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        Dictionary containing the parsed YAML configuration.

    Raises:
        FileNotFoundError: If the configuration file cannot be found.
        yaml.YAMLError: If the YAML file is malformed or cannot be parsed.
    """

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"configuration file not found at: {config_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML configuration: {str(e)}")