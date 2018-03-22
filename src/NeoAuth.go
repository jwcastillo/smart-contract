package neoauth

import (
	"github.com/CityOfZion/neo-go/pkg/vm/smartcontract/runtime"
	"github.com/CityOfZion/neo-go/pkg/vm/smartcontract/storage"
)

func Main(alpha string, beta string) int {
	if !isUUID(alpha) {
		runtime.Log("'alpha' parameter has an invalid RFC UUID format")
		runtime.Log(alpha)
		return 101
	}

	if !isUUID(beta) {
		runtime.Log("'beta' parameter has an invalid RFC UUID format")
		runtime.Log(beta)
		return 102
	}

	ctx := storage.GetContext()
	storage.Put(ctx, alpha, beta)

  return 200
}

func isDash(str string, index int) bool {
	return str[index] == '-'
} 

func isUUID(uuid string) bool {
	if !isDash(uuid, 8) {
		return false
	}
	
	if !isDash(uuid, 13) {
		return false
	}
	
	if !isDash(uuid, 18) {
		return false
	}
	
	if !isDash(uuid, 23) {
		return false
	}
	
	return true
}
