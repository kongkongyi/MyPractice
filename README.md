# MyPractice

1.命令行添加代码
第一次使用：         
centos：       
  yum install git       
  
  
Ubuntu：       
  apt-get install git
  
MacOS:
  brew install git
  
git clone https://github.com/kongkongyi/MyPractice.git

更新本地代码 git pull

查看代码状态 git status

后面添加代码，只需要下面三行即可：     
  git add .     
  git commit -m "first commit" //第一次提交      
  git push -u origin master //同步到远程服务器      

用命令行操作，要添加ssh的公钥到github里，操作方法

创建SSH key的方法很简单，执行如下命令就可以： ssh-keygen 生成的SSH key文件保存在中～/.ssh/id_rsa.pub

然后用文本编辑工具打开该文件，我用的是cat,所以命令是： cat ~/.ssh/id_rsa.pub

接着拷贝出现在屏幕上的内容，将它粘帖到github帐号管理中的添加SSH key界面中。 打开github帐号管理中的添加SSH key界面的步骤如下：

登录github 点击右上方的Accounting，再点击settings图标 选择 SSH and GPGkeys， 点击 New SSH key 在出现的界面中填写SSH 
