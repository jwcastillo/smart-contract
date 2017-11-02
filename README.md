<p align="center">
  <img 
    src="https://cdn.dribbble.com/users/1150751/screenshots/3560077/circle19.gif" 
    width="300px"
  >
</p>

<h1 align="center">smart-contract</h1>

<p align="center">
  <a href="https://neo.org/">NEO</a> smart contract for 
  <a href="https://blockauth.cc">BlockAuth</a>.
</p>

## Contract Address

The smart contract has not yet been deployed to the NEO TestNet.

## Compile

The smart contract can be compiled using the `coz/neo-boa-compiler` Docker image
from [neo-compiler-docker](https://github.com/CityOfZion/neo-compiler-docker):

```
make compile
```

## Parameters

The smart contract takes two arguments:

- **verification_values**: a GUID and a challenge value, joined by a period.
  - string
  - NEO parameter value: `07`
  - Example: `ae6d0adc-5168-4cc4-8ba0-741380e68e35.2843-3583`
- **address**: NEO public address of sender.
  - string
  - NEO parameter value: `07`
  - Example: `AXcQE8W8RzazrB8yq4nfUio8eusRLfSHCF`

## Error codes

The smart contract returns a single **integer** value, which repesents if the 
invocation was a success. The following values can occur:

- `200` - Success.
- `101` - Error, as **verification_values** parameter is invalid.
- `102` - Error, as GUID (first part) in **verification_values** parameter is invalid.
- `103` - Error, as challenge value (second part) in **verification_values** parameter is invalid.
- `104` - Error, as **address** parameter does not match the NEO public address of the sender.

---

<p align="center">
  Use <a href="https://blockauth.cc">BlockAuth</a> for simple passwordless authentication.
  <br>
  🔐
</p>
