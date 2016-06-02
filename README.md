# loc-counter

##Purpose
* Counting the lines of code in commit email.

##Usage
* Prerequiste: Python installed, with pre-installed packages : <python-dateutil, ...>
* In command line interface, type

```python
  python cr.py [-r=reviewed.txt] [-n=nonreviewed.txt] 
                [-s=start date(dd/mm/yyyy)] [-e=end date (dd/mm/yyyy)] 
                  [-i=list,of,included,authors] [-u=list,of,excluded,authors]
```

##How it works

* Firstly, it starts parsing file nonreviewed.txt, try to grab all the commit, then put them into the *non-reviewed* list that indexed by commit number
* ...then, it starts parsing file reviewed.txt, similarly to nonreviewed.txt, it put all the data into list *reviewe*. But when it finds a reivewed commit that exits in the *non-reviewed* list, it removes that commit from *non-reviewed* list
* Finally, it print out how many line of code were reviewed, how many line of code were not
