# Music Flash Cards
<!-- Brief description of what you can do with this program -->

## Hardware Requirements

- Working Microphone

## Installation

### Windows Installation Instructions

### MacOS Installation Instructions

Before installing `music_flash_cards` you will need to install
[PortAudio][1], which is easily accomplished with the [brew][2]
package manager:

```console
$ brew install portaudio
$ python3 -m pip install music_flash_cards
```

### Linux Installation Instructions


## Usage
<!-- Short explanation of how to run the tool -->

## Development
<!-- Describe the development process and tools -->

The general development process is:

- Edit 
- Test
- Bump version
- Publish 

### Packaging

Packaging and prerequisites are managed using the [Poetry][3] tool.

#### Versioning

```console
$ cd /path/to/music_flash_cards
$ poetry version
...
```

#### Building
```console
$ python3 -m pip install -U pip poetry
$ cd /path/to/music_flash_cards
$ poetry build
...
$ ls dist/
...
```

#### Release

Assuming the user has their [PyPI][4] credentials, `poetry` can be
used to publish the package. Credentials can be supplied at the
command-line or managed via poetry (creds are not stored in the
repository).

```console
$ poetry publish
...
```


#### Testing

<!-- stuff about testing with ptyest will go here -->


## ToDo List
<!-- list of future features/enhancments -->


<!-- End Links -->

[1]: http://people.csail.mit.edu/hubert/pyaudio/
[2]: https://brew.sh
[3]: https://python-poetry.org/docs/
