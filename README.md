# CubeSolver
Be able to solve a Rubik's Cube

## Install Directions:
1. Install [PyCube](https://github.com/adrianliaw/pycuber) Library using pip. 
2. tbd.

## Agent Deffinition Template:
[345-04-Rubik's cube](https://docs.google.com/document/d/1Ok0JpGvLng5pIUpZt0fMN-UXKfT7klf67IW1YbpiWUs/edit?usp=sharing)

## Testing and Interface:
As I am working in python an interface it kind of hard to define. In order to make a new agent all a class needs is a .solve(cube) that after it is called the cube is solved.
I did mostly maunal testing. This involved creating a cube in a specific state (ie taking a solved cube and turning certian faces a certain number of times) to test whether code worked for specific edges. It also was a lot of taking random scrambled cubes and looking at them before and after the solve was colled to see if the algorithums worked while not messing up other solved states.

## Jupyter Notebook
[Here](https://colab.research.google.com/drive/1n_vuSKWAHGIn49ixkv6jYbnlynGgynDT?usp=sharing) is a link to my notebook on google Colab where I am using pytorch to create a neural network to solve a cube.
