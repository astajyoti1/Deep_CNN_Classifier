echo [$(date)] "Starting init_setup.sh"
echo [$(date)] "creating env with python 3,8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)] "Activating Environment"
source activate ./env
echo [$(date)] "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)] "Ending init_setup.sh"