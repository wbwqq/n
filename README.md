# nnotes

## Installation

```bash
pip install nnotes
```

## Main commands help

Features:
- multiple notebooks
- add notes
- delete notes (single, multiple, range)
- create notebook
- delete notebook


```
Usage (nnotes can be launched by typing 'n' or 'nnotes'):
    n [command]
    nnotes [command]

Available commands:
    add [note]                                  add note to active notebook
    ls                                          list / view notes from active notebook
    rm                                          delete note(s)
    rm range                                    delete range of notes
    
    add @[notebook] [note]                      add note [note] to notebook [notebook]
    ls @[notebook]                              show notes from [notebook]

    add @[notebook]                             create notebook [notebook]
    ls @                                        list all notebooks
    ls @ path                                   list notebooks with their path

    set active [notebook]                       set active notebook [notebook]
    get active                                  show active notebook

    get notebooks path                          show notebooks directory
    set notebooks path [notebooks path]         set notebooks directory
```

## Example usage

```bash
$ n add new note
```
is the same as:
```bash
$ nnotes add new note
```
`n` and `nnotes` can both be used.

```bash
$ n ls
```

```bash
$ n add @main another note
```

```bash
$ n ls @
```
etc.