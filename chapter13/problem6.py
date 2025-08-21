# run  pip freeze for the system interpreter. Take the content and create a similar virtual env.


"""

pip freeze > requirements.txt #to show loaded libraries in requirement.txt

python -m venv myenv1 # to create new environment

.\myenv1\Scripts\Activate.ps1 # activating the enironment

pip install -r  .\requirements.txt # to install all libraries


"""