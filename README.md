## Feeder Watch :bird:

### Project Description

This project is based on the [Project FeederWatch](https://feederwatch.org/about/project-overview/).

<br/>

> "Project FeederWatch turns your love of feeding birds into scientific discoveries. FeederWatch is a November-April survey of birds that visit backyards, nature centers, community areas, and other locales in North America. You don’t even need a feeder! All you need is an area with plantings, habitat, water or food that attracts birds. The schedule is completely flexible. Count your birds for as long as you like on days of your choosing, then enter your counts online. Your counts allow you to track what is happening to birds around your home and contribute to a continental data-set of bird distribution and abundance." - Project FeederWatch

<br/>

### Project Goals

The goal of this project is to visualize the data with Tablau and to discover interesting patters:

- Can the seasonal change of migratory birds be observed?
- Are some bird species declining or increasing over time?
- What are the most commen and rarest birds in North America?

Because also information about the observation site are given, additional questions can be asked:

- Where are the birds typically observed?
- Do some species prefere some habitats over others?

<br/>

### Data Sources and Processing

The [Raw Data](https://feederwatch.org/explore/raw-dataset-requests/) was downloaded from the Project FeederWatch page for all availible years (1988-2021). Because of the large amount of entrys (in total over 30 million rows) the files were read and passed to a database by a [python script](feed_db.py).

<br/>

In the next step, the different tables were merged into one large with a [jupyter file](merge_tables.ipynb).

<br/>

Then the data will be cleaned with another [jupyter file](cleaning.ipynb)

<br/>

Finally the data will be visualized and analyzed with  python.

### Project Files

| Name | Description |
| ------------- | ------------- |
| [README.md](README.md)  | Project Description  |
| [feed_db.py](feed_db.py)  | Script, which passes the .csv files provided by Project FeederWatch to a database for further processing  |
|[merge_tables.ipynb](merge_tables.ipynb)| merging tables with data from different years into one |
| [cleaning.ipynb](cleaning.ipynb) | cleaning and transformation of the data |