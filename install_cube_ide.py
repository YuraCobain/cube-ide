import os
import subprocess
import os

HOME_DIR = os.path.expanduser('~')

class AwesomeVimrc():
    git_clone_cmd = 'git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime'
    install_cmd = "sh ~/.vim_runtime/install_awesome_vimrc.sh"

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime')

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        subprocess.check_call("cp my_configs.vim ~/.vim_runtime/", shell=True)

class VimYCM:
    git_clone_cmd = 'git clone https://github.com/ycm-core/YouCompleteMe.git'
    git_submodule_cmd ='git submodule update --init --recursive'
    install_cmd = "python3 install.py --clangd-completer  "

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime/my_plugins/YouCompleteMe')

    def clone(self):
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/')
        subprocess.check_call(self.git_clone_cmd, shell=True)
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/YouCompleteMe')
        subprocess.check_call(self.git_submodule_cmd, shell=True)

    def install(self):
        install_cmd = self.install_cmd
        if HOME_DIR == "/root":
            install_cmd += " --force-sudo"

        subprocess.check_call(install_cmd, shell=True)

    def post_configure(self):
        pass

class VimClangFormat:
    git_clone_cmd = 'git clone https://github.com/rhysd/vim-clang-format.git'
    install_cmd = "sudo apt install clang-format -y"

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime/my_plugins/vim-clang-format')

    def clone(self):
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/')
        subprocess.check_call(self.git_clone_cmd, shell=True)
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/vim-clang-format')

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        pass

class VimSwap:
    git_clone_cmd = 'git clone https://github.com/machakann/vim-swap.git'
    install_cmd = ""

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime/my_plugins/vim-swap')

    def clone(self):
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/')
        subprocess.check_call(self.git_clone_cmd, shell=True)
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/vim-swap')

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        pass

class VimIndentLine:
    git_clone_cmd = 'git clone https://github.com/Yggdroot/indentLine.git'
    install_cmd = ""

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime/my_plugins/indentLine')

    def clone(self):
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/')
        subprocess.check_call(self.git_clone_cmd, shell=True)
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/indentLine')

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        pass


class VimInspector:
    git_clone_cmd = 'git clone https://github.com/puremourning/vimspector.git'

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime/my_plugins/vimspector')

    def clone(self):
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/')
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        pass

    def post_configure(self):
        pass

class VimGTest:
    git_clone_cmd = 'git clone https://github.com/alepez/vim-gtest.git'

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.vim_runtime/my_plugins/vim-gtest')

    def clone(self):
        os.chdir(f'{HOME_DIR}/.vim_runtime/my_plugins/')
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        pass

    def post_configure(self):
        pass


class Fzf:
    git_clone_cmd = 'git clone https://github.com/junegunn/fzf.git ~/.fzf'
    install_cmd = "yes | ~/.fzf/install"

    def is_installed(self):
        return os.path.exists(f'{HOME_DIR}/.fzf')

    def clone(self):
        subprocess.check_call(self.git_clone_cmd, shell=True)

    def install(self):
        subprocess.check_call(self.install_cmd, shell=True)

    def post_configure(self):
        pass

packages = [AwesomeVimrc(), VimYCM(), VimClangFormat(), VimClangFormat(), Fzf(), VimGTest(), VimSwap(), VimIndentLine()]

def setup_package(package):
    print(package.__class__.__name__)
    if package.is_installed():
        print("already is installed. pass.")
        return

    package.clone()
    package.install()
    package.post_configure()

def main():
    [setup_package(package) for package in packages]

if __name__ == '__main__':
    main()
