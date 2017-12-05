# ImageNet(ILSVRC2012) Converter for Chainer

```shell-session
$ cd /where/you/put/these/scripts

# Download images
$ wget [imagenet_url]/ILSVRC2012_img_train.tar
$ wget [imagenet_url]/ILSVRC2012_img_val.tar

# Extract tarball
$ mkdir train
$ pushd train
$ pv ../tar/ILSVRC2012_img_train.tar | tar xf -
$ ls *.tar | parallel --bar -a - "mkdir -p {.} && tar xf {} -C {.} && rm {}"
$ popd
$ mkdir val
$ pushd val
$ pv ../tar/ILSVRC2012_img_val.tar | tar xf -
$ popd

# Convert images
$ pushd train
$ ls | parallel --bar -a - ../preprocess.sh
$ popd
$ pushd val
$ ../preprocess.sh .
$ popd

# Generate table
$ python2 labeling.py train val
```

## License

This project is multi-licensed.
You can select the license of your choice from as following:

* [Creative Commons Attribution 4.0 International (CC-BY 4.0)](http://creativecommons.org/licenses/by/4.0/)
  * author (attribution) : Fixstars http://github.com/fixstars
* [The MIT License](https://opensource.org/licenses/mit-license.php)
  * year: 2017
  * copyright holders: Fixstars

## Desclaimer

Anyone including Fixstars is not responsible for any damages or corrupts by this project.
Download and use this project at your own risk.

Any questions or pull-resquests or other contribution are welcome and we're trying to respond as soon as possible.
But no one is responsible to respond them.
Any responses are not responsible by anyone including Fixstars.

## Acknowledgement

本ソフトウェアは、国立研究開発法人新エネルギー・産業技術総合開発機構(NEDO)の委託事業「IoT推進のための横断技術開発プロジェクト」の先導調査研究テーマ「実社会ビッグデータ処理基盤を実現する大規模データセンター構築・運用技術の研究開発」（代表提案者：さくらインターネット株式会社）の一部として開発されました。
