# MangaNotifier
This is a widget for manga fans. Instead of RSS notifiers from different sites, this polls from multiple sites.

Currently, we are trying to use Android visual studio to build this for android users.

We are using Python for the back end.

#Environment

We are using [Oracle VM VirtualBox](https://www.virtualbox.org) to run our virtual machines.

Development is being done on both [Ubuntu](https://www.ubuntu.com) and [Fedora](https://getfedora.org)

We are using the [Atom](https://atom.io/) text editor.

We are using eve for our REST API.

#Installation

##Prerequisites
* Python 3
* Pip
* MongoDB
* Git
* Eve
* feedgen

##Setup

1. Install virtualenv

    ```sudo pip install virtualenv```

2. Clone the repository

    ```git clone https://github.com/roberthluo/MangaNotifier.git```

3. Change to the project directory

    ```cd MangaNotifier```

4. Setup a new virtual environment

    ```virtualenv venv```

5. Activate the virtual environment

    ```source venv/bin/activate```

6. Install dependencies

    ```pip install -r setup/requirements.txt```


##Finishing up

When done working, you can exit the virtual environment using:

    
    deactivate
    

##Use MongoDB (Needs venv to run)

1. Install MongoDB(I used ubuntu, choose the steps for the machine you are using)

    [link](https://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)

2. Activate the mongo environment
    ```
    mongo
    ```

3. Go into manganotifier db
    ```
    use manganotififer
    ```

4. List records in manganotifier

    ```
    db.manga.find()
    ```
5. When done working, you can exit db using:
    ```
    ^c
    ```

6. Go back to Manganotifier folder

    ```
    python HTMLParser.py
    
    ```

##Use Eve

1. It quite simple, but you may be prompted to upgrade pip 

    ```
    sudo pip install eve 
    ```




