# Page loader

[![Maintainability](https://api.codeclimate.com/v1/badges/0f10d4df5001658af2bd/maintainability)](https://codeclimate.com/github/Andrka/python-project-lvl3/maintainability) <a href="https://codeclimate.com/github/Andrka/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/0f10d4df5001658af2bd/test_coverage" /></a> [![Github Actions Status](https://github.com/Andrka/python-project-lvl3/workflows/Python%20CI/badge.svg)](https://github.com/Andrka/python-project-lvl3/actions)

"Page loader" is a written in Python utility which downloads requested web page with local resources.
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install "Page loader".
```bash
pip install --user -i https://test.pypi.org/simple andrka-page-loader --extra-index-url https://pypi.org/simple
```
[![asciicast](https://asciinema.org/a/1HF9qCWahgOaLvKeKL5tvK6VQ.svg)](https://asciinema.org/a/1HF9qCWahgOaLvKeKL5tvK6VQ)
## Usage
As a script:
```bash
page-loader [-h] [--output path] full_url_with_schema
# By default output path is the current directory

page-loader --output /tmp https://andrka.github.io/page-loader-test/
/tmp/andrka-github-io-page-loader-test-.html # saved file`s path
```

As a library:
```python
from page_loader import download

file_path = download('https://andrka.github.io/page-loader-test/', '/tmp')
print(file_path)  # => '/tmp/andrka-github-io-page-loader-test-.html'
```
## A Simple Example
[![asciicast](https://asciinema.org/a/GJsTW4gkHDqbwNtY2Mw4CUcXT.svg)](https://asciinema.org/a/GJsTW4gkHDqbwNtY2Mw4CUcXT)
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
## License
[MIT](https://choosealicense.com/licenses/mit/)