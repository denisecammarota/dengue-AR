## Analysis of the Dengue and Zika Data in Argentina (work in progress)

**Author: Denise Stefania Cammarota**

### Dengue and Zika in Argentina
The aim of this repository is to provide the user with the timeseries of Dengue and Zika cases in Argentina, based on the information provided by the Ministry of Health, updated annually at: http://datos.salud.gob.ar/dataset/vigilancia-de-dengue-y-zika

### Structure of this repository
This is the corresponding folder structure, updated as of the day of the last commit to the project.

```
project/
*    ├── Data/
*    │   ├── raw
*    │   └── processed
*    ├── Python/
*    ├── fct/
*    └── README.md
```

-  The `Data` folder contains two subfolders with raw and processed data. Raw data corresponds to the data on cases downloaded from the site, as well as some auxiliary conventions on provinces and departments names and IDs. Processed data contains outputs of cleaning and separating the data at various steps. 
- The `Python` folder contains the Python scripts to do data cleaning and organization of the raw and processed data.
- The `fct` folder contains functions that can be used by the user to get epidemic curves at different levels of spatial aggregation, after having processed and cleaned the raw data. 


### How to cite this repository
I would appreciate giving credit to this repository should you use it. If want to cite it, you can do so as:

```
@software{dengueAR,
  author = {Cammarota, Denise},
  title = {dengue-AR},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/denisecammarota/dengue-AR}}
}
```

### Contact 
If you have any doubt about the use of this repository, as well as any bugs, feel free to open an issue here on Github, or send an email at: denisescammarota@gmail.com. 
