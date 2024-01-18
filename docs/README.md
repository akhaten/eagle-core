# Welcome to eaglecore

---

Note that README.md file is in /docs folder

---

## Presentation

eaglecore is a python package for signal processing.
Documentation is available [here](https://akhaten.github.io/eaglecore/).

---

## Package structure

```mermaid
flowchart TD
    
    EagleCore[eaglecore] --> Filters[filters]
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

    click EagleCore "https://akhaten.github.io/eaglecore/Eaglecore/" _blank

    click Linear "https://akhaten.github.io/eaglecore/Eaglecore/Filters/Linear" _blank
    click NoLinear "https://akhaten.github.io/eaglecore/Eaglecore/Filters/NoLinear" _blank
    
    click Measure "https://akhaten.github.io/eaglecore/Eaglecore/Signal/Measure" _blank
    click Processing "https://akhaten.github.io/eaglecore/Eaglecore/Signal/Processing" _blank

    click Differential "https://akhaten.github.io/eaglecore/Eaglecore/Differential/" _blank
    click IO "https://akhaten.github.io/eaglecore/Eaglecore/IO/" _blank
    click Metrics "https://akhaten.github.io/eaglecore/Eaglecore/Metrics/" _blank
    click Noise "https://akhaten.github.io/eaglecore/Eaglecore/Noise/" _blank
    click PSF "https://akhaten.github.io/eaglecore/Eaglecore/PSF/" _blank
    click Thresholding "https://akhaten.github.io/eaglecore/Eaglecore/Thresholding/" _blank
    click Types "https://akhaten.github.io/eaglecore/Eaglecore/Types/" _blank
    click Utils "https://akhaten.github.io/eaglecore/Eaglecore/Utils/" _blank

```


---

## Installation

### Nix package manager

The [default.nix](https://github.com/akhaten/eaglecore/blob/main/default.nix) file defines the configuration to build this package
with nix.


By title of example, in your own `shell.nix` file, you can do :
```nix
{ pkgs ? import <nixpkgs> {} }:

let 

  eaglecore = pkgs.fetchFromGitHub {
    owner = "akhaten";
    repo = "eaglecore";
    rev = "the/full/id/of/commit";
    sha256 = "sha256-0000000000000000000000000000000000000000000=";
  };
        
in pkgs.mkShell {

    buildInputs = with pkgs; [
      eaglecore
      # Yours others packages
      # ...
    ];
}
```

### Pip

```sh
python3 -m venv venv
souce ./venv/bin/activate # To disable virtual environment => ./deactivate
pip3 install git+https://www.github.com/akhaten/eaglecore.git
```

---



<!-- The homomorphism $f$ is injective if and only if its kernel is only the 
singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such 
that $f(a)=f(b)$. -->

<!-- ``` mermaid
classDiagram
  Person <|-- Student
  Person <|-- Professor
  Person : +String name
  Person : +String phoneNumber
  Person : +String emailAddress
  Person: +purchaseParkingPass()
  Address "1" <-- "0..1" Person:lives at
  class Student{
    +int studentNumber
    +int averageMark
    +isEligibleToEnrol()
    +getSeminarsTaken()
  }
  class Professor{
    +int salary
  }
  class Address{
    +String street
    +String city
    +String state
    +int postalCode
    +String country
    -validate()
    +outputAsLabel()  
  }
```

```mermaid
gitGraph LR:
    commit
    commit
    branch develop
    commit
    commit
    checkout main
    commit
    commit
    merge develop
    commit
    commit
``` -->

<!-- ```mermaid
%%{ init: { "flowchart" : { "useMaxWidth": 10 } } }%%
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
``` -->
