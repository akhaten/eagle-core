# Welcome to eagle-core

## Presentation

eagle-core is a python package for signal processing.


## Package structure

```mermaid
flowchart TD
    
    EagleCore[eagle-core] --> Filters[filters]
    EagleCore --> Signal[signal]
    EagleCore --> Differential[differential]
    EagleCore --> IO[io]
    EagleCore --> Metrics[metrics]
    EagleCore --> Noise[noise]
    EagleCore --> PSF[psf]
    EagleCore --> Thresholding[thresholding]
    EagleCore --> Types[types]
    EagleCore --> Utils[utils]

    Filters --> Linear[linear]
    Filters --> NoLinear[no linear]

    Signal --> Measure[measure]
    Signal --> Processing[processing]

    click Differential "http://127.0.0.1:8000/Eaglecore/Differential/" _blank
```

<!-- # Welcome to eagle-core

## Presentation

eagle-core is a python package for signal processing.


## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files. -->