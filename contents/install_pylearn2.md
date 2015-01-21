
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

	sudo pip install PyYAML IPython Cython

PILのインストールに失敗した場合

	sudo pip install pillow

なぜかわからないが`pillow`ってのをインストールすると代用できた。

### Theanoのインストール

Theanoは別コマンド

	sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

Theanoのインストールが成功したか確認
	
	$ python
	>>> import theano

### Pylearn2のインストール

ここでは`~/tmp`にダウンロードします。`~/`はユーザフォルダをしめします。
この後もこのフォルダを使っていきます。

	mkdir ~/tmp
	cd ~/tmp
	git clone git://github.com/lisa-lab/pylearn2.git
	cd pylearn2
	python setup.py develop


## データセットの構築

MNIST database  
http://yann.lecun.com/exdb/mnist/

CIFAR-10 & 100  
http://www.cs.toronto.edu/~kriz/cifar.html

The Oxford-IIIT Pet dataset  
http://www.robots.ox.ac.uk/~vgg/data/pets/

deeplearning.net datasets  
http://deeplearning.net/datasets/

kaggle
https://www.kaggle.com/

Microsoft Azure Marketplace
https://datamarket.azure.com/browse/data


# チュートリアル

Quick-start exmaple
http://deeplearning.net/software/pylearn2/tutorial/index.html#tutorial

## Step0: download dataset

今回解析するCIFAR-10をダウンロードします。  
http://www.cs.toronto.edu/~kriz/cifar.html


そして、Pylearn2の解析データを格納するディレクトリのパスを設定します(重要)。ここでは適当に`=/data/lisa/data'以下にファイルをおいてます。

	export PYLEARN2_DATA_PATH=~/MachineLearning/data/
	source ~/.bashrc
	source ~/.bash_profile

データのダウンロード

datasetsフォルダにあるdownload_cifar10.shというシェルスクリプトをたたくとダウンロードされます。(このときダウンロード先は先ほど.bashrcに登録した`PYLEARN2_DATA_PATH`に保存されます)

	~/MachineLearning/pylearn2/scripts/datasets/download_cifar10.sh

## Step1: Create the dataset

	cd ~/MachineLearning/pyleran2/pylearn2/scripts/tutorials/grbm_smd
	python make_dataset.py

## Step2: Train the model

train.pyは/pyleran2/pylearn2/scripts/内にあります。

	~/MachineLearning/pylearn2/pylearn2/scripts/train.py cifar_grbm_smd.yaml

## Step3: Inspect the model

可視化用のオプションを設定(大事)

	export PYLEARN2_VIEWER_COMMAND="open -Wn"
	source ~/.bashrc (なくても動く)
	source ~/.bash_profile (なくても動く)

データの表示コマンドをたたく。

RBMにより学習したフィルタを表示します

	python show_weights.py cifar_grbm_smd.pkl

よくわからない。学習による誤り率の低下を表しているそうです。ここらは今後ということで。

	plot_monitor.py cifar_grbm_smd.pkl



# エラー対処

### pylearn2のインストール時にこけたとき

	clang: error: no such file or directory: 'pylearn2/utils/_window_flip.c'
	clang: error: no input files

_windows_flip.cファイルがないみたい。そのかわりに_windows_filip.pyxが存在している。この.pyxはCythonのコンパイル結果らしく、コンパイルのタイミング?が変らしい。?windows_flip.cをコピペで外部環境で持ってくると動くそうだが。  
https://github.com/lisa-lab/pylearn2/issues/862

setup.pyの中身でCythonのエクステンションの部分をコメントアウトする
https://groups.google.com/forum/#!topic/pylearn-users/uLFGQw2he4E

修正されたsetup.py  
https://github.com/lisa-lab/pylearn2/blob/09dd4a3879934ea02dcca57aada197304e5ae6e2/setup.py

## その他

>pipでパッケージのコンパイルが失敗する場合、一度uninstallすると動く場合があります。
また、--upgradeが効くこともあります。

	pip uninstall <package-name>
	pip install --upgrade <package-name>


>matplotlibがpipでinstall出来ない場合、brew経由だと成功する場合もあります。(要tap)

	brew search matplotlib
	brew tap homebrew/python
	brew install matplotlib

## .bashrcの作成

http://rewish.jp/blog/misc/mbp_mid_2009

>デフォルトの設定ではターミナルログイン時に.bashrc_が読み込まれないので、.bash_profile_を以下のように作成。

	echo source ~/.bashrc >> ~/.bash_profile

>これでターミナルログイン時に.bashrcが読み込まれるようになる。

## /pylearn2/scriptsにpathを通す

	export PATH=~/pylearn2/pylearn2/scripts/:$PATH
	source ~/.bashrc
	source ~/.bash_profile

## シェルスクリプト

http://d.hatena.ne.jp/zariganitosh/20100206/1265436726

## Step1: でこけたとき (注意)

	Mac OS X
	========

	Environment variables on Mac OS X work the same as in Linux, except you should
	modify and run the "source" command on ~/.profile rather than ~/.bashrc.


	Original exception:
		KeyError: PYLEARN2_DATA_PATH

ここまで、解析データの保存先が下のようになっているとするとき。

	~/data/cifar1-0/cifar-10-batches-py/data_batch_1

`PYLEARN2_DATA_PATH`に設定するのは`/data`まで。つまり

	export PYLEARN2_DATA_PATH=~/data

これだけ。


PYLEARN2_DATA_PATHに設定するパスは

	export PYLEARN2_DATA_PATH=~/data


## Step3: Inspect the modelでこけたとき

以下のコマンドで結果を表示しようとした際にエラー

	show_weights.py cifar_grbm_smd.pkl

	Mac OS X
	========
	Environment variables on Mac OS X work the same as in Linux, except you shouldmodify and run the "source" command on ~/.profile rather than ~/.bashrc.

	Original exception:
		KeyError: PYLEARN2_VIEWER_COMMAND

`PYLEARN2_VIEWER_COMMAND`が設定されてないと、エラーが発生

その２

	$ ~/MachineLearning/pylearn2/pylearn2/scripts/show_weights.py cifar_grbm_smd.pkl
	making weights report
	loading model
	loading done
	loading dataset...
	...done
	smallest enc weight magnitude: 1.46641060449e-07
	mean enc weight magnitude: 0.0581363279697
	max enc weight magnitude: 1.03551020748
	min norm: 0.840715049853
	mean norm: 1.37598831115
	max norm: 1.90010889382
	Traceback (most recent call last):
	  File "/Users/noharatomoyuki/MachineLearning/pylearn2/pylearn2/scripts/show_weights.py", line 52, in <module>
	    show_weights(args.path, args.rescale, args.border, args.out)
	  File "/Users/noharatomoyuki/MachineLearning/pylearn2/pylearn2/scripts/show_weights.py", line 31, in show_weights
	    pv.show()
	  File "/Users/noharatomoyuki/MachineLearning/pylearn2/pylearn2/gui/patch_viewer.py", line 366, in show
	    show(self.image)
	  File "/Users/noharatomoyuki/MachineLearning/pylearn2/pylearn2/utils/image.py", line 141, in show
	    ensure_Image()
	  File "/Users/noharatomoyuki/MachineLearning/pylearn2/pylearn2/utils/image.py", line 39, in ensure_Image
	    raise RuntimeError("You are trying to use PIL-dependent functionality"
	RuntimeError: You are trying to use PIL-dependent functionality but don't have PIL installed.







