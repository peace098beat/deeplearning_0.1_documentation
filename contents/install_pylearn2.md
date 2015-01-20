
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
	
	$ python --version
	Python 2.7.5

- gcc

	$ gcc -v
	Configured with: --prefix=/Library/Developer/CommandLineTools/usr --with-gxx-include-dir=/usr/include/c++/4.2.1 Apple LLVM version 6.0 (clang-600.0.56) (based on LLVM 3.5svn)Target: x86_64-apple-darwin13.4.0
	Thread model: posix

- homebrew

	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


## 参考

はじめるDeep Learning
http://qiita.com/icoxfog417/items/65e800c3a2094457c3a0

Pylearn2のインストール(OS:Mac10.9 Marvericks）
http://nonbiri-tereka.hatenablog.com/entry/2014/11/10/104621

MacbookにPylearn2をインストールする
http://deeplearning.jp/?p=196

## 前提

>「Pylearn2のMaxout Networkを、手元のMacbookで動かす」ことを目標に、解説します。
(LinuxとWindowsは、この記事の対象外です。)


## Theanoの内部利用パッケージのインストール

インストールするパッケージ
http://deeplearning.net/software/theano/install.html

- Python >=2.6

- g++

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
	
	今回は省略(インストール済み)

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

## gccコンパイラの設定

- gcc4.8をインストール

	brew install gcc48

- gccをclangより優先度をあげる

	ln -s /usr/local/bin/gcc-4.8 /usr/local/bin/gcc


### 依存パッケージのインストール

事前にインストールするパッケージ

- PIL
- PyYAML
- IPython
- Cython
- Theano

pipを利用してインストール

	sudo pip install PIL PyYAML IPython Cython

Theanoは別コマンド

	sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

Theanoのインストールが成功したか確認
	
	import theano

(コンパイルにはclangではなくgcc)

### Pylearn2のインストール

	git clone git://github.com/lisa-lab/pylearn2.gt
	cd pylearn2
	python setup.py develop

## データセットの構築

## 可視化

