# Cheabsi

Automate your boring online presence and survey at [this site](siakad.polinema.ac.id)

it will automatically choose `NO` for all the survey question

## How to use

1. Open `main.py`
2. Change `Username` & `Password`
3. Save it

### Automatic

In this tutorial i will use Github Actions, if you prefer use something else like Travic CI, Circle CI, etc. then maybe there will need some configuration

1. Create new repository in your new account (public or private will be okay)
2. Download / clone this repository (remember to delete `.git` folder if you clone the repository, `git init`, and add remote url again)
3. In folder `.github/workflows` there will be file called `main.yml` open that file
4. Change `YOUR_EMAIL` & `YOUR_USERNAME` to your github `EMAIL` & `USERNAME`

example:

```yml
git config --local user.email "natlus@rocketmail.com"
git config --local user.name "SultanKs4"
```

then everytime you push or pull request to branch master `main.yml` will be run

#### Schedule Run

You can create a schedule when `main.yml` will be run using schedule cron

Example:

```yml
on:
  schedule:
  - cron: "0 22 * * *"
  ...
```

Schedule above means the `main.yml` will be execute everyday at 22:00

If you not familiar to create schedule cron you can create at [crontab.guru](https://crontab.guru/)

Reminder: Github Actions use UTC time so convert first your desire schedule local time to UTC and then create cron format for that time

#### Skip Run

when your config still have like this:

```yml
push:
    branches: [ master ]
```

that means everytime you push to branch `master` `main.yml` will be run, but how if you want push to branch `master` but you don't want to run `main.yml`, then just add `[ci skip]` to commit message

```commit
[ci skip] <your commit message>
```

Example

```commit
[ci skip] change resolution headless browser
```

if your commit message like above then `main.yml` will not run

### Manual

#### Requirements

1. Python 3.8 or newer
2. PIP
3. Virtualenv (Optional but i highly recommend use it)
4. Firefox Browser
5. [Geckodriver](https://github.com/mozilla/geckodriver/releases)

:heavy_exclamation_mark: I ASSUME YOU ALREADY CREATE A NEW VIRTUAL ENVIRONTMENT AND ACTIVATE IT :heavy_exclamation_mark:

1. Open Terminal / cmd / ps and then navigate to this project
2. Install depedencies

   ```zsh
   pip install -r requirements.txt
   ```

3. run main.py

   ```zsh
   python main.py
   ```

   don't forget to input your username and password

4. wait until you see `Job done! see log for further information` and then navigate to folder `log` there will be `log_absen.txt` and screenshot that you can double check it.

Tested on : Linux & Windows 10

P.S : DWYOR :slightly_smiling_face:
