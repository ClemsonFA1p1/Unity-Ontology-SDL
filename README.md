# Unity-Ontology-SDL
This repository is an application created as part of the VIPR-GS FA 1.1 Task 6. The application helps create scenarios using a pre-defined scenario description language. The scenarios are created in the Unity engine. Various sensors can be incorporated into the scenarios, which is achieved by cloning the existing [Unity ROS sensor](https://github.com/Field-Robotics-Japan/UnitySensors) repository. 

Clone this repository
```bash
git clone --recursive https://github.com/shailendranpoyyamozhi/Unity-Ontology-SDL.git
```
### Important 
Many files are missed while cloning from GitHub to a local PC. This is because of unsupported file formats in Git Hub (meta format files in unity). If the file doesn't open in Unity, I would recommend downloading the Unity file from this [google drive file](https://drive.google.com/drive/folders/19rzfCP89u-Lyg5wCfJ2ipFJI-J1qKtI3?usp=drive_link)


## Table of contents
* [Pre-requistes](#Pre-requistes)
* [ROS setup](#ROS-setup)
* [Unity setup](#Unity-setup)
* [Model library](#Model-library)
* [Application process](#Application-process)

## Pre-requistes
This section covers the various Prerequistes required to run the application. 

### Python setup 
Here various Python libraries communicate with the Ontology layer, Input ,and Unity simulation code. These libraries include:
* Owlready
* RDFlib
* Socket

run the command for installing the required python libraries.
```bash
pip3 install -r requirements.txt
```
### Ubuntu Version
In order to use the application. I would recommend trying the application with Ubuntu 20.04. The application was not tested with other Ubuntu versions or Windows. 
### Unity hub installation and Editor version
Unity Hub is an application used to run the Unity simulation software. It also helps communicate with the community and import various assets created by the community. I have attached a [link](https://docs.unity3d.com/2020.1/Documentation/Manual/GettingStartedInstallingHub.html) to install the Unity hub on Linux.

Inside Unity Hub, We have to choose an editor version to run the simulation. It usually recommends the version based on which file you open. For our repository, kindly install `2022.2.15f1` if it doesn't recommend it.

## ROS setup
[Unity Robotics](https://github.com/Unity-Technologies/Unity-Robotics-Hub) package is created for connecting various robotics hardware inside unity. There are two subprocesses in Unity ROS integration. The links to the respective installations are mentioned in the below links, and a full installation video is also added to this [link](https://www.youtube.com/watch?v=pdMxLxolQuo&ab_channel=hrithikverma)
* [Importing ROS packages in Unity](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/quick_setup.md)
* [Creating a ROS package to communicating with unity](https://github.com/Unity-Technologies/ROS-TCP-Endpoint/tree/main) 
## Unity setup
## Model library
## Application process
