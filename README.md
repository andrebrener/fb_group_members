# Facebook Group Members

Get all the names of the members of a facebook group. The scripts are written and intended to use with Python 3.7.

To use this app, you should be able to see the group members. This means that in a closed or secret group, you'll have to be a member.

## Getting Started

### 1. Clone Repo

`git clone https://github.com/andrebrener/football_data.git`

### 2. Install Packages Required

Go in the directory of the repo and run:
```pip install -r requirements.txt```

### 3. Insert constants

In [constants.py](https://github.com/andrebrener/fb_group_members/blob/master/constants.py) insert:
- `USER`: Facebook mail or username.
- `PASS`: Password.
- `NUMBER_OF_SCROLLS`: Number of scrolls to the bottom of the page. This is done
  because members are loaded as the web is navigated.
- `GROUP_MEMBERS_LINK`: The link of the group members. Eg: `https://www.facebook.com/groups/<group_id>/members/`.

### 3. Get names of group members :)

- Run [get_members.py](https://github.com/andrebrener/fb_group_members/blob/master/get_members.py).
- A directory named `results` will be created in the repo with a csv file named `group_members.csv`.


