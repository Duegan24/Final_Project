from FDPDatabasePsycopg2 import FDPDatabasePsycopg2

database = FDPDatabasePsycopg2()

print("Testing get_orig_states")
print(database.get_origin_states())
print("")

print("Testing get_orig_airports")
print(database.get_origin_airports("CA"))
print("")

print("Testing get_dest_states")
print(database.get_dest_states("ORD"))
print("")

