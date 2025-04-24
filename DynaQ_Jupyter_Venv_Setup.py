
py -3.11 -m venv ./RLvenv

./RLvenv/Scripts/activate

python.exe -m pip install --upgrade pip

#impimporter vs zipimporter error
pip install --upgrade setuptools

pip install ipykernel

py -m ensurepip --upgrade

#The below step must be completed before nvidia-pyindex
pip install wheel

#Required for installation of nvidia-nccl-cu12 otherwise a fake package 0.0.1.dev5 will pop up
pip insatll nvidia-pyindex


#nvidia-nccl-cu12 is for Linux only 
#(NCCL = NVIDIA Collective Communications Library, used mostly for multi-GPU communication on Linux).
pip install nvidia-nccl-cu12
pip install nvidia-nccl-cu12 --extra-index-url https://pypi.ngc.nvidia.com

# triton is for Linux only and can only be built on WSL for windows (Even then with specified index from pytorch)
# pip install triton==3.2.0 --extra-index-url https://download.pytorch.org/whl/nightly/cu121
# If you're installing PyTorch or common packages: Don't install triton manually.

#For both the above errors
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

#Cuda121 is only compatible until torch 2.5.1 and there is no triton dependencies installed automatically.
pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0+cu124 --index-url https://download.pytorch.org/whl/cu124

#Errors from import and the github elevator env will disappear
pip install opencv-python


#Ensures that %matplotlib inline is at the start of each cell for liveplotting

#Install the venv as kernel option in jupyter
python -m ipykernel install --user --name=RLvenv
#Activate the venv before starting jupyter notebook in venv

'''
Removing the kernel and virtual environment¶
To remove the test RLvenv virtual environment, it first needs to be removed as a Jupyter kernel. 
First, make sure that the virtual environment has been activated.

The following command will remove Jupyter kernel that refers to the RLvenv virtual environment.
'''
Jupyter kernelspec remove my_markdown

#Then run the deactivate command.

#References for kernel
https://docs.support.arc.umich.edu/python/jupyter_virtualenv/