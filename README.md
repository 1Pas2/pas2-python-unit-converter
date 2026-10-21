# pas2-python-unit-converter

Convert a small explicit set of length, mass and temperature units.

Part of **Pas2 Polyglot** by [1Pas2](https://github.com/1Pas2): independent small projects in PHP, Python, Go and C#. No runtime dependencies outside the language standard library. Initial version: 0.1.0.

## Requirements and installation

Python 3.11+. Install a checkout using `python -m pip install .`. The import name is `pas2_unit_converter`. PyPI publication was not performed.

## Example

```python
import pas2_unit_converter as api

print(api.convert(32, "F", "C"))
print(api.convert(1, "ft", "cm"))
```

## API and limits

convert(value,source,target) supports m/km/cm/in/ft, kg/g/lb and K/C/F. Units are case-sensitive. Incompatible dimensions, non-finite values and temperatures below absolute zero throw. Uses floating-point arithmetic, not metrology-grade uncertainty propagation.

## Tests and example

From the repository root:

```sh
python -m pip install -e .
python -m unittest discover -s tests -v
python examples/basic.py
```

Tests use the standard library or a dependency-free executable check harness. A failing assertion exits nonzero. The example is self-contained and uses local in-memory or temporary data. CI runs the same checks on Linux. No registry releases, downloads, users or production deployments are claimed.

## Contributing

Open a focused issue or pull request with reproduction steps and a behavioral test. Run the commands above before submitting. Do not include credentials or private data in reports.

## Ecosystem

[Browse Pas2 projects](https://github.com/1Pas2?tab=repositories&q=pas2-). Each repository is usable independently. The earlier TypeScript series and this polyglot series have distinct repository names.

## License

[MIT](LICENSE) © 2026 1Pas2.

1Pas2
