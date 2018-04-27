

## Virtual Environments
To get started with virtual environments, simply download virtualenv using `pip install virtualenv`

Then do the following:

#### Initialization
1. Navigate to the folder you would like to work from
2. Run `virtualenv demo_env` where `demo_env` is what you would like to call the environment

#### Activation
1. Assuming you are in the folder where the virtualenv was intialized, run `source demo_env/bin/activate` to activate the environment

Now all the packages you install using `pip` will be local to this folder!


#### Deactivation
1. Type `deactivate`

#### Virtual Environments with iPython/Jupyter Notebooks
In order to make use of a virtual environment that you have created when running a Jupyter notebook:
1. Make sure that your virtual environment has been activated
2. Run `ipython kernel install --user --name "demo_env" `, where `demo_env` is the name of the environment you wish to use
3. In your Jupyter notebook, click *Kernel -> Change Kernel* and select your environment (in this example, `demo_env`), from the list.

