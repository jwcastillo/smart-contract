<p align="center">
  <img 
    src="https://res.cloudinary.com/vidsy/image/upload/v1509658596/circle19_viaray.gif" 
    width="300px"
  >
</p>

<h1 align="center">smart-contract</h1>

<p align="center">
  <a href="https://neo.org/">NEO</a> smart contract for 
  <a href="https://blockauth.cc">BlockAuth</a>.
</p>

<p align="center">
  <a href="https://github.com/blockauth/smart-contract/releases">
    <img src="https://img.shields.io/github/tag/blockauth/smart-contract.svg?style=flat">
  </a>
</p>

## Contract Address

Please see [releases](https://github.com/blockauth/smart-contract/releases) for full details:

```
2f228c37687d474d0a65d7d82d4ebf8a24a3fcbc
```

## Compile

The smart contract can be compiled using the `coz/neo-boa-compiler` Docker image
from [neo-compiler-docker](https://github.com/CityOfZion/neo-compiler-docker):

```
make compile
```

## Parameters

The smart contract takes two arguments:

1. **alpha**: a UUID, used as the first part of the key for `Storage.Put()`.
    - string
    - NEO parameter value: `07`
    - Example: `50801e46-a161-4297-8771-61dbebe9f19d`
2. **beta**: a UUID, used as the second part of the key for `Storage.Put()`.
    - string
    - NEO parameter value: `07`
    - Example: `f88d2cda-2da2-4c6a-95d5-b31f06433604`

## Error Codes

The smart contract returns an **integer** (parameter value `02`), which repesents if the 
invocation was a success. The following values can occur:

- `200` - Success.
- `101` - Error, as **alpha** parameter has an invalid [RFC UUID format](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format).
- `102` - Error, as **beta** parameter has an invalid [RFC UUID format](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format).
- `103` - Error, the hash of the current transaction is invalid.

## Testing

The smart contract can be tested locally using 
[neo-python](https://github.com/CityOfZion/neo-python). The following command can be used:

```
build /path/to/blockauth/smart-contract/src/BlockAuth.py test 0707 02 True ae6d0adc-5168-4cc4-8ba0-741380e68e35 f88d2cda-2da2-4c6a-95d5-b31f06433604
```

---

<p align="center">
  Use <a href="https://blockauth.cc">BlockAuth</a> for simple passwordless authentication.
  <br>
  🔐
</p>
