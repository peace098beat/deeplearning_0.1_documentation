
# Pylearn2をインストール

## 環境

- macbook

	$ uname -a

	Darwin nohara-no-MacBook-Air.local 13.4.0 
	Darwin Kernel Version 13.4.0:
	Sun Aug 17 19:50:11 PDT 2014; 
	oot:xnu-2422.115.4~1/RELEASE_X86_64 x86_64

- merveric

- Python

Pythonは2.7系を利用する
	
	$ python --version
	Python 2.7.5

- gcc

macbookのgccの環境を調べる

	$ gcc -v
	Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/usr/include/c++/4.2.1 Apple LLVM version 6.0 (clang-600.0.56) (based on LLVM 3.5svn)Target: x86_64-apple-darwin13.4.0
	Thread model: posix

appleのコンパイラclangが設定されている。
今回はgccの必要があるため、後ほど設定する。

- homebrew

homebrewのインストール

	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	$ brew --version0.9.5


## 参考

はじめるDeep Learning
http://qiita.com/icoxfog417/items/65e800c3a2094457c3a0

Pylearn2のインストール(OS:Mac10.9 Marvericks）
http://nonbiri-tereka.hatenablog.com/entry/2014/11/10/104621

MacbookにPylearn2をインストールする
http://deeplearning.jp/?p=196

## 前提

0からPylearn2を動かすまでを前提にします。

>「Pylearn2のMaxout Networkを、手元のMacbookで動かす」ことを目標に、解説します。
(LinuxとWindowsは、この記事の対象外です。)


## Theanoの内部利用パッケージのインストール

インストールするパッケージ
http://deeplearning.net/software/theano/install.html

- Python >=2.6

	(今回はPython2.7系が入っているので省略します)

- g++

homebrewを使ってgccをインストールします。

	% gcc -v

	$ brew install gcc48
	// Error が発生

	$ brew info gcc
	// not installed 4.9があるけどインストールされていない

再インストール
	
	$ brew reinstall gcc

このままではapple標準のclangが優先されてしまいエラーが発生するので、gccの優先度をあげます

	ln -s /usr/local/bin/gcc-4.8 /usr/local/bin/gcc

- python-dev

	(省略)インストール作業自体はおこなっていない

- Numpy >=1.5

http://gihyo.jp/dev/serial/01/machine-learning/0006

	mkdir ~/tmp
	cd ~/tmp
	git clone git://github.com/numpy/numpy.git numpy
	cd numpy
	sudo python setup.py install

	// (今回)1.6.2

- Scipy >=0.8

	(インストール済みのため省略)

- BLAS

	(OSXの場合は不要)

あると便利なツール

- nose (Theano's test-suite)

	sudo easy_install nose
	// version 1.3.4

- Sphinx >=0.5.1 (ドキュメント作成ツール)
	
	今回は省略

- pygments (ドキュメント作成ツール)
	
	今回は省略

- Git
	
	pip 省略(インストール済み)

- pydot (make picture of Theano compuration graph)

ソースをダウンロード
https://code.google.com/p/pydot/

	$ sudo easy_install http://cheeseshop.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz
	$ sudo easy_install pydot

	sudo pip uninstall pydot pyparsing
	sudo pip install pyparsing==1.5.7
	sudo pip install pydot

- NVIDIA CUDA drivers and SDK
- libgpuarray


### 依存パッケージのインストール

事前にインストールするパッケージ

- PIL
- PyYAML
- IPython
- Cython
- Theano

pipを利用してインストール

	sudo pip install PIL PyYAML IPython Cython

失敗した場合

	sudo pip install --allow-external PIL PyYAML IPython Cython

### Theanoのインストール

Theanoは別コマンド

	sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

Theanoのインストールが成功したか確認
	
	$ python
	>>> import theano

### Pylearn2のインストール

	mkdir ~/tmp
	cd ~/tmp
	git clone git://github.com/lisa-lab/pylearn2.git
	cd pylearn2
	python setup.py develop


## データセットの構築




## 可視化

### pylearn2のインストール時にこけたとき

	clang: error: no such file or directory: 'pylearn2/utils/_window_flip.c'
	clang: error: no input files

_windows_flip.cファイルがないみたい。そのかわりに_windows_filip.pyxが存在している。この.pyxはCythonのコンパイル結果らしく、コンパイルのタイミング?が変らしい。?windows_flip.cをコピペで外部環境で持ってくると動くそうだが。  
https://github.com/lisa-lab/pylearn2/issues/862

setup.pyの中身でCythonのエクステンションの部分をコメントアウトする
https://groups.google.com/forum/#!topic/pylearn-users/uLFGQw2he4E

修正されたsetup.py  
https://github.com/lisa-lab/pylearn2/blob/09dd4a3879934ea02dcca57aada197304e5ae6e2/setup.py


