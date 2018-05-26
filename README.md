# gym-dart [![Build Status](https://travis-ci.org/dartsim/gym-dart.svg?branch=develop)](https://travis-ci.org/dartsim/gym-dart)
[OpenAI Gym](https://github.com/openai/gym) environments for [DART](https://github.com/dartsim/dart) and [dartpy](https://github.com/personalrobotics/dartpy)

## Environments

* `DartReacher-v0`

## Build from Source

### OpenAI Gym

* Using `pip`

```console
$ pip3 install gym
```

* Build from source

```console
$ git clone https://github.com/openai/gym
$ cd gym
$ pip install -e .
```

### dartpy

```console
$ sudo apt-add-repository ppa:dartsim/ppa
$ sudo apt-add-repository ppa:personalrobotics/ppa
$ sudo apt update
$ suao apt install python3-dartpy
```

### gym-dart

```console
$ git clone https://github.com/dartsim/gym-dart
$ cd gym-dart
$ pip install -e .
```

## License

gym-dart is licensed under a BSD license. See [LICENSE](./LICENSE) for more information.
