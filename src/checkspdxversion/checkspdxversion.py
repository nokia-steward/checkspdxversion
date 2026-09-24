#!/bin/python3

# © 2026 Nokia
# Author: Marc-Etienne Vargenau
# Licensed under the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0

__version__ = "0.1.2"

"""Utility checking whether a given file is an SPDX 2 JSON, SPDX 3 JSON, or neither."""

import json
import argparse
import os

def identify_spdx_json_type(filepath: str) -> str:
    """
    Identifies whether a given file is an SPDX 2 JSON, SPDX 3 JSON, or neither.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        str: "SPDX 2.X", "SPDX 3.0.1", or an error message.
    """
    if not os.path.exists(filepath):
        return f"Error: File '{filepath}' not found"
    if not os.path.isfile(filepath):
        return f"Error: Path '{filepath}' is not a file"

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return f"Error: File '{filepath}' is not a valid JSON format"
    except Exception as e:
        return f"Error reading file: {e}"

    # Check for SPDX 2.x
    # SPDX 2.x typically has "spdxVersion" starting with "SPDX-2."
    if isinstance(data, dict) and \
       "spdxVersion" in data and data["spdxVersion"].startswith("SPDX-2."):
        version = data["spdxVersion"]
        return version.replace("-", " ")

    # Check for SPDX 3.x
    # SPDX 3.x typically has "specVersion" starting with "3."
    if isinstance(data, dict) and '@graph' in data:
        for elem in data['@graph']:
            if 'specVersion' in elem:
                version = elem['specVersion']
                if version.startswith("3."):
                    return f"SPDX {version}"

    return f"File '{filepath}' is not an SPDX SBOM"

def main():
    """
    Main function checking whether a given file is an SPDX 2 JSON, SPDX 3 JSON, or neither.
    """
    parser = argparse.ArgumentParser(
        description="Identify if a file is an SPDX 2 JSON, SPDX 3 JSON, or neither."
    )
    parser.add_argument(
        "-v", "--version", # Accepts both -v and --version
        action="version",
        version=__version__,
        help="Show program's version number and exit."
    )
    parser.add_argument(
        "file",
        type=str,
        help="The path to the JSON file to analyze."
    )

    args = parser.parse_args()
    result = identify_spdx_json_type(args.file)
    print(result)

if __name__ == "__main__":
    main()
