# 有的终端不显示颜色，这是为终端配置颜色方案
export TERM=xterm-color

# 这是设置终端输入光标前的显示内容
# export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;36m\]\w\[\033[00m\]\$ '
export PS1='\n\e[1;37m[\e[m\e[1;32m\u\e[m\e[1;33m@\e[m\e[1;35m\H\e[m \e[4m`pwd`\e[m\e[1;37m]\e[m\e[1;36m\e[m\e[33mfairy\e[m\n\$' 

# 这是一个配置环境变量的例子
export JAVA_HOME=/usr/local/Cellar/openjdk/13.0.2+8_2/libexec/openjdk.jdk/Contents/Home
export PATH="$JAVA_HOME/bin:$PATH"
