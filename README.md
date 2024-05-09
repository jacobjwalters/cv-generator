# cv-generator
This project automatically generates a CV given a YAML description of one's career.

## Usage
First, install PyYAML if not already available.
This is probably best done either through pip, or through your distro's package manager.

An example YAML file is given in `cv-example.yaml`.
Edit this to your liking, and rename it to `cv.yaml`.
Then, run `python3 generate.py` in this directory. An output folder will be created, containing `Your Name CV.tex`.
Pass this file through your favourite LaTeX compiler.

## Acknowledgements
The document styling was originally created by Trey Hunner.