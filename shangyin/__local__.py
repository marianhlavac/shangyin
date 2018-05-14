import shangyin.storage as storage
from shangyin.server import server

# Connect database
db = storage.Storage()
db.setup()

# Start up the statistics server
srun = server.ServerRunner()
srun.assign_db(db)
srun.start()