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

## Contract Address

Please see [releases](https://github.com/blockauth/smart-contract/releases) for full details:

```
5e4011a7c98a204bfe86e37f59ec278de85a75cb
```

## Compile

The smart contract can be compiled using the `coz/neo-boa-compiler` Docker image
from [neo-compiler-docker](https://github.com/CityOfZion/neo-compiler-docker):

```
make compile
```

## Parameters

The smart contract takes two arguments:

1. **key**: a UUID, used in the Storage key.
    - string
    - NEO parameter value: `07`
    - Example: `50801e46-a161-4297-8771-61dbebe9f19d`
2. **challenge**: a UUID, used both in the Storage key and value.
    - string
    - NEO parameter value: `07`
    - Example: `f88d2cda-2da2-4c6a-95d5-b31f06433604`

## Error Codes

The smart contract returns an **integer** (parameter value `02`), which repesents if the 
invocation was a success. The following values can occur:

- `200` - Success.
- `101` - Error, as **key** parameter has an invalid [RFC UUID format](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format).
- `102` - Error, as **challenge** parameter has an invalid [RFC UUID format](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format).

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
