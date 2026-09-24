# checkspdxversion

A utility checking whether a given file is an SPDX 2 JSON, SPDX 3 JSON, or neither.

# Usage

```
usage: checkspdxversion [-h] [-v] file

Identify if a file is an SPDX 2 JSON, SPDX 3 JSON, or neither.

positional arguments:
  file           The path to the JSON file to analyze.

options:
  -h, --help     show this help message and exit
  -v, --version  Show program's version number and exit.
```

It will print the SPDX version of the SBOM, e.g. "SPDX 2.3" or "SPDX 3.0.1", or an error message.
