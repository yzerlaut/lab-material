# Laboratory Material & Workflows

A repository hosting some common material and the workflow instructions for the team.

clone with:
```
git https://github.com/yzerlaut/lab-material
```

## System Setup

Links to the instructions (depending on your operating system):

|     |     |     |
| --- | --- | --- |
| [Linux](./Setup/Linux.md) | [OS X](./Setup/OSX.md) | [Windows](./Setup/Windows.md) |

## Access the Network-Attached Storage (NAS)

...

## Working collaboratively with Figures

...

## Working collaboratively on a Manuscript

- Copy the folder: [./Manuscript](./Manuscript)
- Work with references in *J. Neuroscience* style in the text as `(Author et al., 2025)`
- Add single references with such lines in the `References` section:
```
    [Author et al., 2025] Author A, Author2 B, Author3 C. Manuscript title. Journal of Nothing. 2025;2(1):123-125.
```

### 1) Fetch a manuscript for a Google document

- ask the current `google_API_key.txt` file to the admin

- put the ID of your document in a `manuscript_ID.txt` file.

    e.g. for 

Then run:

```
python scripts/fetch_GoogleDocs.py
```

### 2) Process References

```
python scripts/fetch_GoogleDocs.py
```

### 3) Make Text Backups from Google Docs

```
python scripts/backup.py
```

The text will be stored as a markdown text file 
`YY-MM-DD-hh:mm:ss.md` (e.g. `2025-01-24-17-34-02.md`) in the `./backups/` folder.



