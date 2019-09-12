![alt text](img/igz-h.jpg)
# Intelygenz talent test

##_v1.0.0_

### What you’ll need
* A favorite text editor or IDE
* [Python 2.7](https://www.python.org/)
* [pip](https://pypi.org/project/pip/)
* [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
* Minimum knowledge about [Flask Framework](http://flask.pocoo.org/)

### What you'll do
1. Download and unzip this source repository, or clone it using [Git](https://git-scm.com):  
  `git clone git@gitlab.com:intelygenz/igz-python-talent-test.git`
2. **Read the issue** that has been assigned to you.
3. **Create a merge request from the issue** from the issue detail screen, you can create a merge request to work on. When you create a merge request, a branch is also created.
5. **Work on the branch** until you feel you have resolved the issue.
6. Remove the **WIP** status on the merge request screen
7. You are ready to go!

More info: https://about.gitlab.com/2016/03/08/gitlab-tutorial-its-all-connected/

#### Create virtualenv
This is required once before installing dependencies
##### Windows
```
virtualenv.exe -p python2.exe venv
```
##### UNIX
```
virtualenv -p python2.7 venv
```
#### Activate virtualenv
This is required before installing dependencies or running the project.
##### Windows
```
venv\Scripts\activate
```
##### UNIX
```
source venv/bin/activate
```
Once virtualenv is activated, your prompt will change. To deactivate it, run
```
deactivate
```
#### Install dependencies
With virtualenv enabled, run
```
pip install -r requirements.txt
```
#### Run the Project
With virtualenv enabled, run
```
python main.py
```

#### Test the services
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ "matrix": [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ] }' \
  http://localhost:5000/api/matrix/sum
```
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ "matrix": [ [ 1, 2, 3], [4, 5, 6], [7, 8, 9] ] }' \
  http://localhost:5000/api/matrix/diagonal_sum
```
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{ "string": "aaAabaccCBb" }' \
  http://localhost:5000/api/string/encode
```
### Mandatory
**Push the create branch to remote for evaluate the solution.**

### Important
_Please, feel free to contact us if you need more information by writting a comment in the asigned issue and we will respond asap._
