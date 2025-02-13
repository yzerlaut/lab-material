# Laboratory Material & Workflows

A repository hosting some common material and workflow guidelines for the team.

## Basic System Setup

## 1) Install a `python` distribution (through [Miniforge](https://github.com/conda-forge/miniforge))

- MsWin:
    ```
    curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe
    start /wait "" Miniforge3-Windows-x86_64.exe /InstallationType=JustMe /RegisterPython=1 /S /D=%UserProfile%\Miniforge3 # use as default
    ```

- UNIX (Linux / OSX)
    ```
    curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
    bash Miniforge3-$(uname)-$(uname -m).sh
    ```

## 2) Install the packages for scientific computing

```
conda install numpy scipy matplotlib pandas
```

## 3) Some system-specific setup instructions

Links to the instructions (depending on your operating system):

|     |     |     |
| --- | --- | --- |
| [Linux](./Tools/Setup/Linux.md) | [OS X](./Tools/Setup/OSX.md) | [Windows](./Tools/Setup/Windows.md) |


## Access the Network-Attached Storage (NAS)

...

## Working collaboratively on a Manuscript

Clone this repository with:
```
git clone https://github.com/yzerlaut/lab-material
```
And rename the `lab-material` folder according to the name of the study.

### Figures

Content for figures is stored in the folder: [./Figures](./Figures)

- Figures should be stored as plain `svg` files in the `./Figures` folder.

- For Affinity users. Start from the svg files, save your Affinity file in the `./Figures/affinity/` folder, and systematically export to plain `svg` in the `./Figures` folder.

- Build a pdf summary with: `python scripts/build_pdf_summary.py`

- Export all figures to `png` and `tiff` using: `bash scripts/export_svgFigures_to_bitmap.sh`


### Text 

Content for the main text is stored in the folder: [./Manuscript](./Manuscript)

#### Guidelines:

- Work with references in *J. Neuroscience* style in the text as `(Author et al., 2025)`
- Add single references with such lines in the `References` section:
```
    [Author et al., 2025] Author A, Author2 B, Author3 C. Manuscript title. Journal of Nothing. 2025;2(1):123-125.
```

#### Fetch a manuscript for a Google document:

- ask the current `google_API_key.txt` file to the admin

- put the ID of your document in a `manuscript_ID.txt` file.

Then run:

```
python scripts/fetch_GoogleDocs.py
```

#### Process References:

```
python scripts/fetch_GoogleDocs.py
```

#### Make Plain Text Backups (`*.md` files) from Google Docs

```
python scripts/backup.py
```

The text will be stored as a markdown text file 
`YY-MM-DD-hh:mm:ss.md` (e.g. `2025-01-24-17-34-02.md`) in the `./backups/` folder.



