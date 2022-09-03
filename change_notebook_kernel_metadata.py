import json
from pathlib import Path


def update_notebook_metadata(path):
    content = path.read_text()
    json_content = json.loads(content)
    json_content["metadata"]["kernelspec"] = {
        "name": "xeus-python",
        "display_name": "Python (XPython)",
        # "language": "python",
    }
    path.write_text(json.dumps(json_content))


notebooks = Path("scikit-learn-mooc/").glob('**/*.ipynb')


if __name__ == '__main__':
    for n in notebooks:
        update_notebook_metadata(n)
