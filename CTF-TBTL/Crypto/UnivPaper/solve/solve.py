from sympy import sqrt, mod_inverse

# Constants
N = 13113180816763040887576781992067364636289723584543479342139964290889855987378109190372819034517913477911738026253141916115785049387269347257060732629562571
value1 = 11295696938311339473824077083449119515455766620804723271417795055153345707595152245303924808555919718654126902417279389829240793581636850443514989727075129
value2 = 25255532621039290870985214051278041571596463385115156541846401100873975663406085683775323107488

# Calculate value2^3
value2_cubed = value2**3

# Check if value2^3 modulo N matches value1
calculated_value1 = value2_cubed % N

# If the condition matches, calculate the possible values for name_int
if calculated_value1 == value1:
    name_int_possibilities = (sqrt(value2_cubed), -sqrt(value2_cubed))
    result = f"Calculated name_int possibilities: {name_int_possibilities}"
else:
    result = "The conditions do not match; please verify the values or approach."

print((sqrt(value2_cubed) -sqrt(value2_cubed)))
