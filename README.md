# get start 

## 1. Setup Virtual Machine (oracle virtual box)
set network adapter to bridge mode
## 2. Install Software
Install docker in VM 1,2,3
```bash
https://docs.docker.com/engine/install/ubuntu/
```
Install java in VM 1,2,3
```bash
sudo apt install openjdk-11-jre
```
install robot framework in VM 2
```bash
sudo python3 -m pip install robotframework
```
install flask in VM 2,3
```bash
sudo python3 -m pip install flask
```
## 3. Set up Docker
set permission for docker
```bash
sudo chmod 666 /var/run/docker.sock
```
## 4. Install jenkins
Install genkins with docker in virtual machine 1 (master)
```bash
https://www.jenkins.io/doc/book/installing/docker/
```
## 5. Install git
Install git in VM 1,2,3
```bash
sudo apt install git
```
## 6. SSH from window
ip network adapter setting && ip address in line "enp0s3" and "inet" in VM 1,2,3
```bash
ifconfig
```
ssh from window

```bash
ssh <username>@<ip>
```
## 7. Access jenkins from local machine
```bash
http://<ip vm1>:<port jenkins>
```
## 8. Unlock jenkins
cat the initial password from inside the jenkins container
```bash
docker exec -it jenkins && cat /var/jenkins_home/secretsinitialAdminPassword
```
## 9. Update jenkins plugins
Update the suggested plugins

## 10. Create Nodes in Jenkins (slave VM 2,3) 
in web browser, 
```bash
go to manage jenkins -> System Configuration -> node -> new node -> fill in name and select permanent agent
```
configure the node
```bash
fill Number of executors = 1
fill Remote root directory = /home/<vm user>
fill Labels = <label>
fill Launch method =  Lanch agent via SSH -> 
host = <ip vm> -> 
credentials = <add> -> kind = username with password -> username = <vm user> -> password = <vm password>
Host Key Verification Strategy = non verifying verification strategy
```

## 11. Create a pipeline in Jenkins
in web browser, 
```bash
Dashboard go to new item -> fill in name -> select pipeline -> ok
```
configure the pipeline
```bash
Build Triggers -> Poll SCM -> * * * * *
Pipeline -> Definition -> Pipeline script from SCM -> SCM = Git -> Repository URL = <git url> -> Credentials = <add> -> kind = username with password -> username = <git user> -> password = <git password>
branch = */main
Script Path = Jenkinsfile
```
## 13. Build the pipeline
In the pipeline, click build now

## 14. Configure if the pipeline fails
Configure all as you want