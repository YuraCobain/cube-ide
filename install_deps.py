import os
import subprocess
import os

class AwesomeVimrc:
    git_clone_cmd = 'git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime'
    install_cmd = "sh ~/.vim_runtime/install_awesome_vimrc.sh"

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        subprocess.check_call("cp my_configs.vim ~/.vim_runtime/", shell=True)

class VimYCM:
    git_clone_cmd = 'git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime/my_plugins'
    git_submodule_cmd ='git submodule update --init --recursive'
    install_cmd = "python3 install.py --clangd-completer  "

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)
        os.chdir("~/.vim_runtime/my_plugins/YouCompleteMe")
        subprocess.check_call(self.git_submodule_cmd, shell=True)

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        subprocess.check_call("cp my_configs.vim ~/.vim_runtime/", shell=True)

class VimClangFormat:
    git_clone_cmd = 'git clone https://github.com/rhysd/vim-clang-format.git ~/.vim_runtime/my_plugins'
    install_cmd = "python3 install.py --clangd-completer"

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        pass

class VimInspector:
    git_clone_cmd = 'git clone https://github.com/puremourning/vimspector.git ~/.vim_runtime/my_plugins'

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        pass

    def post_configure(self):
        pass

class VimGTest:
    git_clone_cmd = 'git clone https://github.com/alepez/vim-gtest.git'

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        pass

    def post_configure(self):
        pass



packages = [AwesomeVimrc, VimYCM, VimClangFormat, VimClangFormat, VimGTest]

def setup_package(package):
    package.clone()
    package.install()
    package.post_configure()

def main():
    if os.path.exists(".deps"):
        print("deps directory already exist, remove it manually to force install!!!")
        exit(1)

    os.makedirs('.deps', exist_ok=True)
    os.chdir('.deps/')
    deps_root = os.getcwd()

    [setup_package(package) for package in packages]

if __name__ == '__main__':
    main()
