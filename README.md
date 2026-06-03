# Facebook Group Members

Get all the names of the members of a facebook group. The scripts are written and intended to use with Python 3.7.

To use this app, you should be able to see the group members. This means that in a closed or secret group, you'll have to be a member.

> **Known limitation — likely non-functional today (archival/educational).**
> This tool was written in 2019 against Facebook's then-current page layout
> and the Selenium 3 API. Since then Facebook has changed its login flow
> (cookie-consent interstitials, checkpoints/2FA) and continuously rotates the
> obfuscated CSS class names this scraper depends on (e.g. `_60rh`). The code
> has been updated to the Selenium 4 API for correctness, but it will almost
> certainly **not** successfully log in or extract members against today's
> Facebook. It is kept here for reference, not as a working scraper.

> **Legal / Terms of Service.** Automating login and scraping content from
> Facebook violates Facebook's Terms of Service. This project is provided for
> educational purposes only. Use it at your own risk and responsibility.

## Getting Started

### 1. Clone Repo

`git clone https://github.com/andrebrener/fb_group_members.git`

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

> **Security warning.** `constants.py` is tracked in this repository with
> placeholder values only. **Never commit your real Facebook credentials.**
> If you fill in real values locally, do not push them — consider keeping a
> local-only copy and treat your password as a secret.

### 4. Get names of group members :)

- Run [get_members.py](https://github.com/andrebrener/fb_group_members/blob/master/get_members.py).
- You will see an automated browser entering to Facebook, logging in, entering the group and scroll down.
- A directory named `results` will be created in the repo with a csv file named `group_members.csv`.
