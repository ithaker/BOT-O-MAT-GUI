# BOT-O-MAT-GUI


## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Installation](#installation)
* [Project Details](#project-details)

## General Info
This was the second, Plan-B attempt at completing the Bot-O-Mat Project for Red Ventures. The code still needs to be fully fleshed out, but aims to provide a graphical interface in which users can name their robot, declare its type, and complete chores by clicking on them in a list.

## Technologies
The program is built in python using Kivy, an open source Python library which helps rapidly develop of applications

## Installation
1. Clone the repository

2. Install [Kivy](https://kivy.org/#download)

3. Once installed the program can be run from the terminal as any other python file 
`python main.py`

## Project Details

### Robot
Robot completes tasks and removes them from the list when they are done (i.e. enough time has passed since starting the task).

### Tasks
Tasks have a description and an estimated time to complete.

```
[
  {
    description: 'do the dishes',
    eta: 1000,
  },{
    description: 'sweep the house',
    eta: 3000,
  },{
    description: 'do the laundry',
    eta: 10000,
  },{
    description: 'take out the recycling',
    eta: 4000,
  },{
    description: 'make a sammich',
    eta: 7000,
  },{
    description: 'mow the lawn',
    eta: 20000,
  },{
    description: 'rake the leaves',
    eta: 18000,
  },{
    description: 'give the dog a bath',
    eta: 14500,
  },{
    description: 'bake some cookies',
    eta: 8000,
  },{
    description: 'wash the car',
    eta: 20000,
  },
]
```

### Types
```
{ 
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```


## Authors
- Scott Hoffman <https://github.com/scottshane>
- Olivia Osby <https://github.com/oosby>
- Ishan Thaker <https://github.com/ithaker>
