# Badge Generator

Generate a latex file to generate tickets

# Installation
Python 3.7 or highter + texlive distribution with texlive-ticket package installed

## Usage:

```bash
generate_latex.py [-h] logo conf_name subtitle csv_participant date filename_out
```
```bash
Positional arguments:
  logo:             Logo to use
  conf_name:        Conference name
  subtitle:         Conference subtitle
  csv_participant:  CSV of participants. Format:
                   `<Name>;<Lastname>;<institution>`
  date:             Conference date
  filename_out:     Conference name

Optional arguments:
  -h, --help       show help message and exit
```

## Example:

```bash
python badge_generator/generate_latex.py example/conf_logo.png "Awesome Conference" "In dreamland" example/list_of_participants.csv "1st october 2019" badges.tex
```

This generate the badges.tex file.
You can compile it to obtain the pdf of all your participants.
In our case it gives me: ![badges](./example/badges.pdf)


