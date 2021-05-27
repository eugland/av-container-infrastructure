# Container Infrastructure
[![DOI](https://zenodo.org/badge/216539298.svg)](https://zenodo.org/badge/latestdoi/216539298)
Proof of work for "Autonomous Vehicle container infrastructure" at https://doi.org/10.1109/CCWC47524.2020.9031129

## logs
- [raw logs](./log/)
    - [five fold nested containers](./log/5foldnested.csv)
    - [Existing containers](./log/existingcontainer.csv)
    - [native](./log/native.csv)
    - [newcontainer.csv](./log/newcontainer.csv)
- [analyzed logs](./log/analysisbook.xlsx)


## Test
To run on native machine, go into this directory and: 
```python
python . 
```
then when menu shows up select accordingly the environment in which you want to run the test.
If you want to run any of the situation directly, run `python gausse` for native run vs new container and or `python main.py` in flask application or 5 nested containers

## Use and License
This project is licensed under MIT license. You are free to share and use findings in this repository.
