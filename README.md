# gym-dart [![Build Status](https://travis-ci.org/dartsim/gym-dart.svg?branch=develop)](https://travis-ci.org/dartsim/gym-dart) [![Build Status](https://dev.azure.com/dartsim/gym-dart/_apis/build/status/dartsim.gym-dart?branchName=develop)](https://dev.azure.com/dartsim/gym-dart/_build/latest?definitionId=2&branchName=develop)
[OpenAI Gym](https://github.com/openai/gym) environments for [DART](https://github.com/dartsim/dart) and [dartpy](https://github.com/dartsim/dart/tree/master/python)

> :warning: **Warning:** `gym-dart` is under heavy development. See the open issues on [`gym-dart`](https://github.com/dartsim/gym-dart/issues) for insight into the current state of the project. Please report any issues you encounter on the appropriate repository. We will use `develop` branch (instead of `master`) as the default branch without worrying about the commit history until the API becomes stable.

## Environments

* `DartCartPole-v0`
* `DartParticle-v0`
* `DartReacher-v0`

## Installation

### OpenAI Gym

* Using `pip`

```console
$ python3 -m pip install -U gym
```

* Build from source

```console
$ git clone https://github.com/openai/gym
$ cd gym
$ python3 -m pip install -e .
```

### dartpy

```console
$ sudo apt-add-repository ppa:dartsim/ppa
$ sudo apt update
$ suao apt install python3-dartpy
```

### gym-dart

```console
$ git clone https://github.com/dartsim/gym-dart
$ cd gym-dart
$ python3 -m pip install -e .
```

## License

`gym-dart` is licensed under a BSD license. See [LICENSE](./LICENSE) for more information.
