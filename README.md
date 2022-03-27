[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/dead-tech/pre-commit-cmake/main.svg)](https://results.pre-commit.ci/latest/github/dead-tech/pre-commit-cmake/main)
# pre-commit-cmake

pre-commit hook to build your cmake projects

# Configuration
Basic configuration:
```yaml
repos:
  - repo: https://github.com/dead-tech/pre-commit-cmake
    rev: 'v0.0.3'
    hooks:
      - id: cmake-build
```

Optional arguments are:
 - --build-dir to change default build directory (build/)
 - --release to call cmake in release mode

Those arguments can be set like so:
```yaml
repos:
  - repo: https://github.com/dead-tech/pre-commit-cmake
    rev: 'v0.0.3'
    hooks:
      - id: cmake-build
        args: [--release, '--build-dir <path>']

```
