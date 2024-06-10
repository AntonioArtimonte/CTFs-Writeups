import math
from Crypto.Util.number import long_to_bytes, inverse


# Define the constants
N = 13113180816763040887576781992067364636289723584543479342139964290889855987378109190372819034517913477911738026253141916115785049387269347257060732629562571
value1 = 11295696938311339473824077083449119515455766620804723271417795055153345707595152245303924808555919718654126902417279389829240793581636850443514989727075129
value2 = 25255532621039290870985214051278041571596463385115156541846401100873975663406085683775323107488

# Calculate the square of value2, this gives us an approximate value for name_int^2
approx_name_int_squared = value2 ** 3

# Calculate the range to check for name_int values based on the given conditions
lower_bound_sqrt = int(math.sqrt(approx_name_int_squared))
upper_bound_sqrt = int(math.sqrt((value2 + 2) ** 3))

# Find name_int by checking which value squared modulo N equals value1
for i in range(lower_bound_sqrt, upper_bound_sqrt + 1):
    if (i ** 2) % N == value1:
        break

print(long_to_bytes(i))
print(lower_bound_sqrt)
print(upper_bound_sqrt)
